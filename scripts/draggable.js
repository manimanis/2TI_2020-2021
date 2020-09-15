class ExerciceOrderItems {
  static counter = 0;

  constructor(exNode) {
    ExerciceOrderItems.counter++;
    this.exNode = exNode;
    this.id = `order-items-exercise_${ExerciceOrderItems.counter}`;
    this.num_id = ExerciceOrderItems.counter;
    this.itemsOrder = [];
    this.is_verified = false;
    this.is_numbered = exNode.dataset.isnumbered.toLowerCase() === 'true';
    this.buildUI();
    this.placeDefaults();
  }

  buildUI() {
    const exercice = document.createDocumentFragment();
    const exerciceDiv = $('<div>')
      .addClass('ordered-items-exercise')
      .attr('id', this.id);
    const exDiv = exerciceDiv[0];

    // drag n drop handlers
    exDiv.addEventListener('dragstart', e => {
      if (e.target.classList.contains('draggable-item')) {
        e.dataTransfer.setData("Text", e.target.id);
      }
    });
    exDiv.addEventListener('dragover', e => { e.preventDefault(); });
    exDiv.addEventListener('drop', e => {
      e.preventDefault();
      const target = $(e.target);
      const parentDropTarget = target.closest('.drop-target');
      if (parentDropTarget) {
        if (parentDropTarget.hasClass('list-group-item')) {
          if (parentDropTarget[0].childNodes.length > 0) {
            parentDropTarget[0].childNodes.forEach(node => {
              $(node)
                .appendTo(choix_div);
              this.refreshButtons();
            });
          }
        }
        if (parentDropTarget[0].childNodes.length >= +parentDropTarget.data('slots')) {
          return;
        }
        const data = e.dataTransfer.getData("Text");
        if (data.substr(0, data.lastIndexOf('_')) === `item_${this.num_id}`) {
          $(`#${data}`)
            .appendTo(parentDropTarget);
          this.refreshButtons();
        }
      }
    });

    // énoncé
    $('<p>')
      .text(this.exNode.dataset.enonce)
      .appendTo(exerciceDiv);

    // choix
    const choix_div = $('<div>')
      .addClass('drop-target proposed-items border p-2')
      .appendTo(exerciceDiv);
    this.choix_div = choix_div;

    // élément à ordonner
    const thisObj = this;
    $(this.exNode)
      .find('[data-ordre]')
      .each(function (index) {
        const item = $(this);
        const itemId = `item_${thisObj.num_id}_${index}`;
        const data = {
          id: itemId,
          ordre: +item.data('ordre'),
          place: false
        };
        const place = item.data('place');
        if (typeof place === 'boolean') {
          data.place = place;
        }
        thisObj.itemsOrder.push(data);

        $('<span>')
          .attr('id', itemId)
          .addClass('badge badge-secondary p-2 m-1 draggable-item')
          .text(item.text())
          .prop('draggable', true)
          .appendTo(choix_div);
      });

    const items = this.exNode.querySelectorAll('[data-ordre]');
    choix_div.data('slots', items.length)

    // éléments ordonnées
    const ordered_div = $('<div>')
      .addClass('ordered-items')
      .appendTo(exerciceDiv);
    const ol = $('<ul>')
      .addClass('list-group')
      .appendTo(ordered_div);
    $(this.exNode)
      .find('[data-ordre]')
      .each(function (index) {
        const item = $(this);
        const li = $('<li>')
          .addClass('list-group-item drop-target')
          .data('slot', 1)
          .appendTo(ol);
        if (thisObj.is_numbered) {
          li.addClass('numbered');
        }
      });

    // Boutons
    const btn_div = $('<div>')
      .addClass('my-2 d-print-none')
      .appendTo(exerciceDiv);
    const btnVerify = $('<button>')
      .addClass('btn btn-primary')
      .text('Vérifier')
      .appendTo(btn_div)
      .on('click', e => {
        e.preventDefault();
        thisObj.verify();
      });
    this.btn_verify = btnVerify;

    const btnReset = $('<button>')
      .addClass('btn btn-dark ml-2')
      .text('Reset')
      .appendTo(btn_div)
      .on('click', e => {
        e.preventDefault();
        thisObj.reset();
      });
    this.btn_reset = btnReset;

    this.exNode.parentNode.insertBefore(exDiv, this.exNode.nextSibling);
    this.node = exDiv;
    this.exercice_div = exerciceDiv;
  }

  placeDefaults() {
    const thisObj = this;
    this.itemsOrder.forEach((item, index) => {
      if (item.place) {
        this.place(index, item.ordre - 1);
      }
    });
    this.refreshButtons();
  }

  hasAllItemsPlaced() {
    return this.node.querySelectorAll('.ordered-items ul li span').length === this.itemsOrder.length;
  }

  refreshButtons() {
    this.btn_verify.attr('disabled', this.is_verified || !this.hasAllItemsPlaced());
    this.btn_reset.attr('disabled', !this.is_verified);
  }

  place(index, position) {
    const elem = $(`#item_${this.num_id}_${index}`);
    const container = this.exercice_div
      .find(`.ordered-items .list-group li:eq(${position})`);
    elem.appendTo(container);
  }

  verify() {
    const thisObj = this;
    if (!this.hasAllItemsPlaced()) {
      alert(`Veuillez ordonner tous les éléments avant de vérifier!`);
      return;
    }
    $('.ordered-items ul li span')
      .each(function (index) {
        const span = $(this);
        const ordreObj = thisObj.itemsOrder.find(obj => obj.id === span[0].id);
        span.prop('draggable', false);
        if ((index + 1) === ordreObj.ordre) {
          span
            .removeClass('badge-secondary badge-danger')
            .addClass('badge-success');
        } else {
          span
            .removeClass('badge-secondary', 'badge-success')
            .addClass('badge-danger');
        }
      });
    this.choix_div.css({ display: 'none' });
    this.is_verified = true;
    this.refreshButtons();
  }

  reset() {
    const thisObj = this;
    $('.ordered-items ul li span')
      .each(function () {
        const span = $(this);
        span
          .attr('draggable', true)
          .removeClass('badge-danger badge-success')
          .addClass('badge-secondary')
          .appendTo(thisObj.choix_div);
      });
    this.choix_div.css({ display: 'block' });
    this.is_verified = false;
    this.placeDefaults();
    this.refreshButtons();
  }
}

class BrickExercise {
  static counter = 0;

  constructor(canvas) {
    BrickExercise.counter++;
    this.num_ex = BrickExercise.counter;
    this.id = `brick-exercise-${this.num_ex}`;
    this.canvas = $(canvas);
    this.blocks = this.canvas.find('.brick');
    this.slots_count = this.canvas.data('slots');
    this.buildUI();
    this.dragDrop();
  }

  buildUI() {
    const thisObj = this;
    this.canvas
      .attr('id', this.id);
    // create a container
    const blk_container = $('<div>')
      .addClass('blk-container border drop-target')
      .appendTo(this.canvas);
    this.blocks
      .each(function (index) {
        const block = $(this);
        block
          .wrap('<span class="brick-container drop-target"></span>')
          .removeClass('brick')
          .addClass('internal-brick draggable-item badge badge-secondary')
          .attr('id', `block-${thisObj.num_ex}-${index}`)
          .attr('draggable', true);
      })
      .appendTo(blk_container);
    // Remove main brick container
    // they are not needed anymore 
    this.canvas
      .children('.brick-container')
      .remove();
    // The container where the user will drop
    const blk_drop = $('<div>')
      .addClass('blk-drop-bricks')
      .appendTo(this.canvas);
    this.blk_drop = blk_drop;
    const ul = $('<ul>')
      .addClass('list-group')
      .appendTo(blk_drop);
    // Add drop targets
    for (let i = 0; i < this.slots_count; i++) {
      const li = $('<li>')
        .addClass('list-group-item drop-target numbered')
        .appendTo(ul);
    }
    // Add control buttons
    const blk_control = $('<div>')
      .addClass('p-2')
      .appendTo(this.canvas);
    this.btn_verify = $('<button>')
      .addClass('btn btn-primary')
      .text('Vérifier')
      .appendTo(blk_control)
      .on('click', e => {
        e.preventDefault();
        this.verify();
      });
    this.btn_reset = $('<button>')
      .addClass('btn btn-dark ml-2')
      .text('Reset')
      .appendTo(blk_control)
      .on('click', e => {
        e.preventDefault();
        this.reset();
      });
  }

  dragDrop() {
    // drag n drop handlers
    this.canvas[0].addEventListener('dragstart', e => {
      if (e.target.classList.contains('draggable-item')) {
        e.dataTransfer.setData("Text", e.target.id);
      }
    });
    this.canvas[0].addEventListener('dragover', e => { e.preventDefault(); });
    this.canvas[0].addEventListener('drop', e => {
      e.preventDefault();
      const target = $(e.target);
      const parentDropTarget = target.closest('.drop-target');
      if (parentDropTarget) {
        const data = e.dataTransfer.getData("Text");
        if (data.substr(0, data.lastIndexOf('-')) === `block-${this.num_ex}`) {
          $(`#${data}`)
            .appendTo(parentDropTarget);
          //this.refreshButtons();
        }
      }
    });
  }

  verify() {
    this.blk_drop
      .find('.internal-brick')
      .each(function (index) {
        const brick = $(this);
        const brick_id = brick.attr('id');
        const id = +brick_id.substr(brick_id.lastIndexOf('-') + 1);
        console.log(id);
      });
  }

  reset() {

  }
}

document.querySelectorAll('.order-items-exercise')
  .forEach(item => new ExerciceOrderItems(item));

document.querySelectorAll('.bricks-canvas')
  .forEach(item => new BrickExercise(item));