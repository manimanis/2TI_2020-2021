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
    const thisObj = this;
    this.num_ex = BrickExercise.counter;
    this.id = `brick-exercise-${this.num_ex}`;
    this.canvas = $(canvas);
    this.blocks = this.canvas
      .find('.brick')
      .each(function (index) {
        const id = `block-${thisObj.num_ex}-${index}`;
        const child = $(this)
          .attr('id', id);
      });
    this.blk_success = this.canvas
      .find('.success')
      .addClass('d-none d-print-block')
      .removeAttr('hidden');
    this.slots_count = this.canvas.data('slots');
    this.structure = this.browseStructure(this.canvas, '.brick');
    this.buildUI();
    this.dragDrop();
    this.scramble();
    this.refreshButtons();
  }

  browseStructure(node, selector) {
    const tree = [];
    const thisObj = this;
    node.children(selector)
      .each(function () {
        const child = $(this);
        const id = child.attr('id');
        tree.push({ [id]: thisObj.browseStructure(child, selector) });
      });
    return tree;
  }

  /**
   * 
   * @param {HTMLNode} node 
   * @param {string} classname 
   */
  filterByClassname(node, classname) {
    let tree = [];
    node.childNodes.forEach(child => {
      if (child.nodeType !== Node.ELEMENT_NODE) {
        return;
      }
      if (child.classList.contains(classname)) {
        const id = child.getAttribute('id');
        tree.push({ [id]: this.filterByClassname(child, classname) });
      } else {
        tree = tree.concat(this.filterByClassname(child, classname));
      }
    });
    return tree;
  }

  buildUI() {
    const thisObj = this;
    this.canvas
      .attr('id', this.id);
    // create a container
    const blk_container = $('<div>')
      .addClass('blk-container d-print-none border drop-target')
      .appendTo(this.canvas);
    this.blk_container = blk_container;
    this.blocks
      .each(function (index) {
        const block = $(this);
        block
          .wrap('<span class="brick-container drop-target"></span>')
          .removeClass('brick')
          .addClass('internal-brick draggable-item badge badge-secondary')

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
      .addClass('blk-drop-bricks d-print-none')
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
      .addClass('blk_control p-2 d-print-none')
      .appendTo(this.canvas);
    this.blk_control = blk_control;
    this.btn_verify = $('<button>')
      .addClass('btn btn-primary')
      .text('Vérifier')
      .appendTo(blk_control)
      .on('click', e => {
        e.preventDefault();
        thisObj.verify();
      });
    this.btn_reset = $('<button>')
      .addClass('btn btn-dark ml-2')
      .text('Reset')
      .appendTo(blk_control)
      .on('click', e => {
        e.preventDefault();
        thisObj.reset();
      });
  }

  scramble() {
    const bricks = this.blk_container
      .find('.internal-brick');
    for (let i = 0; i < bricks.length / 2; i++) {
      const pos = Math.floor(Math.random() * bricks.length);
      $(bricks[i]).insertAfter($(bricks[pos]));
    }
  }

  dragDrop() {
    // drag n drop handlers
    this.canvas[0].addEventListener('dragstart', e => {
      if (e.target.classList.contains('draggable-item')) {
        e.dataTransfer.setData("Text", e.target.id);
      }
    });
    this.canvas[0].addEventListener('dragover', e => {
      e.preventDefault();
      const target = $(e.target);
    });
    this.canvas[0].addEventListener('dragenter', e => {
      e.preventDefault();
      const target = $(e.target);
      const parentDropTarget = target.closest('.drop-target');
      if (parentDropTarget.length) {
        parentDropTarget.addClass('drag-enter');
      }
    });
    this.canvas[0].addEventListener('dragleave', e => {
      e.preventDefault();
      const target = $(e.target);
      const parentDropTarget = target.closest('.drop-target');
      if (parentDropTarget.length) {
        parentDropTarget.removeClass('drag-enter');
      }
    });
    this.canvas[0].addEventListener('drop', e => {
      e.preventDefault();
      const target = $(e.target);
      const parentDropTarget = target.closest('.drop-target');

      if (parentDropTarget.length) {
        parentDropTarget.removeClass('drag-enter');
        if (parentDropTarget[0].childNodes.length > 0) {
          parentDropTarget[0].childNodes.forEach(node => {
            $(node)
              .appendTo(this.blk_container);
          });
          this.refreshButtons();
        }
        const data = e.dataTransfer.getData("Text");
        if (data.substr(0, data.lastIndexOf('-')) === `block-${this.num_ex}`) {
          $(`#${data}`)
            .appendTo(parentDropTarget);
          this.refreshButtons();
        }
      }
    });
  }

  sameTree(t1, t2) {
    let isEqual = t1.length === t2.length;
    for (let i = 0; i < Math.min(t1.length, t2.length); i++) {
      const n1 = t1[i];
      const n2 = t2[i];
      Object.keys(n1)
        .forEach(k1 => {
          if (n2[k1]) {
            const same = this.sameTree(n1[k1], n2[k1]);
            isEqual = isEqual && same;
            $(`#${k1}`)
              .removeClass('badge-secondary badge-danger')
              .addClass('badge-success');
          } else {
            isEqual = false;
            Object.keys(n2).forEach(k2 => {
              $(`#${k2}`)
                .removeClass('badge-secondary badge-success')
                .addClass('badge-danger');
            });
          }
        });
    }
    return isEqual;
  }

  hasAllItemsPlaced() {
    return this.blk_container
      .find('.internal-brick').length === 0;
  }

  refreshButtons() {
    const itemsPlaced = this.hasAllItemsPlaced();
    this.btn_verify
      .attr('disabled', !itemsPlaced);
    this.btn_reset
      .attr('disabled', !itemsPlaced);
  }

  verify() {
    const curr_struct = this.filterByClassname(this.blk_drop[0], 'internal-brick');
    const isOK = this.sameTree(this.structure, curr_struct);
    if (isOK) {
      this.blk_drop
        .find('.internal-brick')
        .removeAttr('draggable');
      this.blk_success
        .removeClass('d-none');
      this.blk_container.hide();
      this.blk_control.hide();
      this.blk_drop.hide();
    }
    this.refreshButtons();
  }

  reset() {
    const thisObj = this;
    this.blk_drop
      .find('.internal-brick')
      .each(function () {
        const brick = $(this);
        brick
          .removeClass('badge-success badge-danger')
          .addClass('badge-secondary')
          .attr('draggable', true)
          .appendTo(thisObj.blk_container);
      });
    this.scramble();
    this.refreshButtons();
  }
}

class QcmExercise {
  static counter = 0;
  constructor(node) {
    QcmExercise.counter++;
    this.num_id = QcmExercise.counter;
    this.exercise_id = `qcm-exercise-${this.num_id}`;
    this.node = $(node);
    this.prop_container = this.node.find('.propositions');
    let data_correct = this.node.data('correct') || '1';
    if (data_correct) {
      data_correct = data_correct.toString();
    }
    this.answers = (data_correct || '1')
      .split(',')
      .map(num => +num - 1);
    this.control_type = (this.answers.length == 1) ? 'radio' : 'checkbox';
    this.scrambled = !!this.node.data('scrambled');
    this.buildUI();
    console.log(this.scrambled);
    if (this.scrambled) {
      this.scramble();
    }
  }

  buildUI() {
    this.node
      .attr('id', this.exercise_id);
    this.prop_container
      .addClass('list-group');
    const thisObj = this;
    this.props = this.prop_container
      .find('li')
      .each(function (index) {
        const li = $(this);
        const li_text = li.html();
        const prop_id = `${thisObj.exercise_id}_${index}`;
        li
          .html('')
          .addClass('list-group-item');
        const prop_div = $('<div>')
          .appendTo(li);
        const control = $('<input>')
          .attr('type', thisObj.control_type)
          .attr('id', prop_id)
          .attr('name', `qcmex_${thisObj.num_id}`)
          .appendTo(prop_div);
        const label = $('<label>')
          .addClass('p-2')
          .attr('for', prop_id)
          .html(li_text)
          .appendTo(prop_div);
      });
    this.blk_control = $('<div>')
      .addClass('p-2 d-print-none')
      .appendTo(this.node);
    this.btn_verify = $('<button>')
      .addClass('btn btn-primary mr-2')
      .text('Vérifier')
      .appendTo(this.blk_control)
      .on('click', (e) => {
        e.preventDefault();
        thisObj.verify();
      });
    this.btn_reset = $('<button>')
      .addClass('btn btn-dark')
      .text('Reset')
      .appendTo(this.blk_control)
      .on('click', (e) => {
        e.preventDefault();
        thisObj.reset();
      })
      .hide();
    this.blk_message = $('<div>')
      .insertBefore(this.blk_control);
  }

  scramble() {
    const li_count = this.props.length;
    for (let i = 0; i < li_count; i++) {
      const pos = Math.floor(Math.random() * li_count);
      $(this.props[i])
        .insertAfter($(this.props[pos]));
    }
  }

  hasCheckedItems() {
    return this.props.find(':checked').length > 0;
  }

  verify() {
    if (!this.hasCheckedItems()) {
      alert('Veuillez cocher les bonnes réponses !');
      return;
    }

    let score = 0;
    const user_ans = [];
    const thisObj = this;
    this.props.find(`:${this.control_type}`)
      .each(function () {
        const id = $(this).attr('id');
        const num = +id.substr(id.lastIndexOf('_') + 1);
        const isChecked = $(this).is(':checked');
        const includes = thisObj.answers.includes(num);
        if (isChecked === includes) {
          score += 1;
        }
      });
    this.props.find(`:${this.control_type}`)
      .attr('disabled', true);
    this.btn_verify
      .hide();
    this.btn_reset
      .show();
    if (score === this.props.length) {
      this.blk_message
        .removeClass('badge-danger')
        .addClass('badge badge-success')
        .text('Bravo, correct!');
    } else {
      this.blk_message
        .removeClass('badge-success')
        .addClass('badge badge-danger')
        .text(`Incorrect, ${score} corrects parmi ${this.props.length}!`);
    }
  }

  reset() {
    this.btn_verify
      .show();
    this.btn_reset
      .hide();
    this.props.find(`:${this.control_type}`)
      .attr('disabled', false)
      .prop('checked', false);
    this.blk_message
      .removeClass('badge badge-success badge-danger')
      .text('');
  }
}

class PagePersistance {
  constructor() {
    this.page_id = location.pathname;
    this.listeners = [];
    this.tokens = [];
    this.token = {};
    this.loadData();
  }

  addListener(callback) {
    this.listeners.push(callback);
  }

  notifyClients(event_name) {
    this.listeners.forEach(listener => listener(event_name, this));
  }

  generateToken() {
    const generateRandomToken = (length) => {
      const ph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
      let token = '';
      for (let i = 0; i < length; i++) {
        token += ph[Math.floor(Math.random() * ph.length)];
      }
      return token;
    };
    let token;
    do {
      token = generateRandomToken(8);
    } while (this.hasToken(token));
    return token;
  }

  hasToken(token) {
    return this.tokens.findIndex(token_obj => token_obj.token === token) !== -1;
  }

  createToken() {
    const token = this.generateToken();
    this.addToken(token);
    this.notifyClients('create');
  }

  addToken(token) {
    if (this.hasToken(token)) {
      throw new Error(`Token ${token} is already in use!`);
    }
    this.token = {
      name: token,
      token: token,
      date: new Date().toISOString(),
      data: {}
    };
    this.tokens.push(this.token);
    this.saveData();
  }

  loadByToken(token_name) {
    this.loadData();
    const idx1 = this.indexOf(token_name);
    if (idx1 === -1) {
      throw new Error(`Invalid token ${token_name}.`);
    }
    this.token = this.tokens[idx1];
    const idx2 = this.tokens.length - 1;
    if (idx1 !== idx2) {
      const temp = this.tokens[idx2];
      this.tokens[idx1] = temp;
      this.tokens[idx2] = this.token;
    }
    this.saveData();
    this.notifyClients('load-by-token');
  }

  findByName(token_name) {
    return this.tokens.find(t => t.name === token_name);
  }

  indexOf(token_name) {
    return this.tokens.findIndex(token_obj => token_obj.token === token_name);
  }

  loadData() {
    this.tokens = JSON.parse(localStorage.getItem(this.page_id)) || [];
    if (this.tokens.length === 0) {
      this.createToken();
    } else {
      this.token = this.tokens[this.tokens.length - 1];
    }
    this.notifyClients('load-data');
  }

  saveData() {
    localStorage.setItem(this.page_id, JSON.stringify(this.tokens));
    this.notifyClients('save-data');
  }

  setData(key, data) {
    if (typeof this.token.data !== 'object') {
      this.token.data = {};
    }
    this.token.data[key] = data;
    this.saveData();
  }

  getData(key) {
    if (!key) {
      return this.token.data;
    }
    return this.token.data[key];
  }

  setName(name) {
    this.token.name = name;
    this.saveData();
  }

  getName() {
    return this.token.name;
  }
}

class UserInputSaver {
  constructor(node, persistance) {
    this.node = $(node);
    this.persistance = persistance;
    this.buildUI();
    this.persistance.addListener((event_name) => {
      // console.log(event_name);
      this.update();
    });
  }

  buildUI() {
    const thisObj = this;
    this.blk_control = $('<div>')
      .addClass('d-print-none')
      .appendTo(this.node);
    this.blk_saves_list = $('<div>')
      .addClass('my-2 d-print-none')
      .appendTo(this.node);
    const select = $('<select>')
      .appendTo(this.blk_saves_list)
      .on('change', e => {
        const val = select.val();
        if (val.length !== 8 && val !== 'new') {
          return;
        }
        if (val === 'new') {
          this.persistance.createToken();
        } else {
          this.persistance.loadByToken(val);
        }
      });
    this._refreshTokensList();

    $('<button>')
      .text('Changer nom...')
      .addClass('btn btn-success ml-2')
      .appendTo(this.blk_saves_list)
      .on('click', (e) => {
        const newName = prompt('Donner un nouveau nom à votre travail !', thisObj.persistance.getName());
        if (!/^[A-Za-z0-9_]+$/.test(newName)) {
          alert('Caractères invalides, uniquement des nombres et des chiffres et le caractère de soulignement (_).');
          return;
        }
        if (newName.length < 3 || newName.length > 32) {
          alert('Longueur invalide, la longueur du nom doit être entre 3 et 32 caractères');
          return;
        }
        thisObj.persistance.setName(newName);
      });

    $('.save-content').each(function (index) {
      const input_ctrl = $(this);
      const placeholder = input_ctrl.attr('placeholder') || 'Taper un texte...';
      input_ctrl
        .wrap('<div></div>');
      const div_id = `save-content-${index}`;
      const parent_div = input_ctrl
        .parent('div')
        .attr('id', div_id)
        .addClass('save-content-div');
      input_ctrl
        .on('blur', (e) => {
          const input_ctrl = $(e.target);
          const parent_div = input_ctrl.parent('div');
          const div_id = parent_div.attr('id');
          thisObj.persistance.setData(div_id, input_ctrl.val());
          input_ctrl.hide();
          parent_div.find('pre')
            .show()
            .text(thisObj.persistance.getData(div_id) || placeholder);
        })
        .hide();
      $('<pre>')
        .text(thisObj.persistance.getData(div_id) || placeholder)
        .addClass('save-content-pre')
        .on('click', (e) => {
          const pre = $(e.target);
          const parent_div = pre.parent('div');
          const div_id = parent_div.attr('id');
          pre.hide();
          parent_div.find('.save-content')
            .show()
            .val(thisObj.persistance.getData(div_id) || '')
            .focus();
        })
        .appendTo(parent_div);
    });
  }

  _refreshTokensList() {
    const select = this.blk_saves_list.find('select')
      .html('');
    this.persistance.tokens.forEach((token, index) => {
      const option = $('<option>')
        .attr('value', token.token)
        .text(`${token.name} (${token.date.substr(0, 16)})`)
        .appendTo(select);
      if (token.token === this.persistance.token['token']) {
        option.attr('selected', true);
      }
    });
    $('<option>')
      .attr('value', 'new')
      .text('Nouvelle sauvegarde...')
      .appendTo(select);
  }

  _refreshInputs() {
    const thisObj = this;
    $('.save-content-div')
      .each(function () {
        const div = $(this);
        const div_id = div.attr('id');
        const input_ctrl = div.find('.save-content');
        const pre = div.find('.save-content-pre');
        const placeholder = input_ctrl.attr('placeholder') || 'Taper un texte...';
        input_ctrl.val(thisObj.persistance.getData(div_id) || '');
        pre.text(thisObj.persistance.getData(div_id) || placeholder);
      });
  }

  update() {
    this._refreshTokensList();
    this._refreshInputs();
  }
}

document.querySelectorAll('.order-items-exercise')
  .forEach(item => new ExerciceOrderItems(item));

document.querySelectorAll('.bricks-canvas')
  .forEach(item => new BrickExercise(item));

document.querySelectorAll('.qcm-exercise')
  .forEach(item => new QcmExercise(item));
