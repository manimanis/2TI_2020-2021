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
    this.refreshButtons();
  }

  buildUI() {
    const exercice = document.createDocumentFragment();
    const exDiv = document.createElement('div');
    exDiv.className = 'ordered-items-exercise';
    exDiv.id = this.id;
    // énoncé
    const enonce_p = document.createElement('p');
    enonce_p.textContent = this.exNode.dataset.enonce;
    exDiv.appendChild(enonce_p);
    // choix
    const choix_div = document.createElement('div');
    choix_div.className = 'drop-target proposed-items border p-2';
    exDiv.appendChild(choix_div);
    this.choix_div = choix_div;
    // élément à ordonner
    const items = this.exNode.querySelectorAll('[data-ordre]');
    choix_div.dataset.slots = items.length;
    items
      .forEach((item, index) => {
        this.itemsOrder.push({
          id: `item_${this.num_id}_${index}`,
          ordre: +item.dataset.ordre
        });
        const span = document.createElement('span');
        span.id = `item_${this.num_id}_${index}`;
        span.className = 'badge badge-secondary p-2 m-1 draggable-item';
        span.textContent = item.textContent;
        span.draggable = true;
        choix_div.appendChild(span);

        exDiv.addEventListener('dragstart', e => {
          if (e.target.classList.contains('draggable-item')) {
            e.dataTransfer.setData("Text", e.target.id);
          }
        });
        exDiv.addEventListener('dragover', e => { e.preventDefault(); });
        exDiv.addEventListener('drop', e => {
          e.preventDefault();
          if (e.target.classList.contains('drop-target')) {
            const target = e.target;
            console.log(target.classList.contains('list-group-item'));
            if (target.classList.contains('list-group-item')) {
              if (target.childNodes.length > 0) {
                target.childNodes.forEach(node => {
                  choix_div.appendChild(node);
                  this.refreshButtons();
                });
              }
            }
            if (target.childNodes.length >= +target.dataset.slots) {
              return;
            }
            const data = e.dataTransfer.getData("Text");
            if (data.substr(0, data.lastIndexOf('_')) === `item_${this.num_id}`) {
              target.appendChild(document.getElementById(data));
              this.refreshButtons();
            }
          }
        });
      });
    // éléments ordonnées
    const ordred_div = document.createElement('div');
    ordred_div.className = 'ordered-items';
    exDiv.appendChild(ordred_div);
    const ol = document.createElement('ul');
    ol.className = 'list-group';
    ordred_div.appendChild(ol);
    items
      .forEach(item => {
        const li = document.createElement('li');
        li.className = 'list-group-item drop-target';
        if (this.is_numbered) {
          li.classList.add('numbered');
        }
        li.dataset.slots = 1;
        ol.appendChild(li);
      });
    // Boutons
    const btn_div = document.createElement('div');
    btn_div.className = 'my-2 d-print-none';
    exDiv.appendChild(btn_div);
    const btnVerify = document.createElement('button');
    btnVerify.className = 'btn btn-primary';
    btnVerify.textContent = 'Vérifier';
    btnVerify.addEventListener('click', (e) => {
      e.preventDefault();
      this.verify();
    });
    this.btn_verify = btnVerify;
    btn_div.appendChild(btnVerify);
    const btnReset = document.createElement('button');
    btnReset.className = 'btn btn-dark ml-2';
    btnReset.textContent = 'Reset';
    btnReset.addEventListener('click', (e) => {
      e.preventDefault();
      this.reset();
    });
    this.btn_reset = btnReset;
    btn_div.appendChild(btnReset);
    this.exNode.parentNode.insertBefore(exDiv, this.exNode.nextSibling);
    this.node = exDiv;
  }

  hasAllItemsPlaced() {
    return this.node.querySelectorAll('.ordered-items ul li span').length === this.itemsOrder.length;
  }

  refreshButtons() {
    if (!this.is_verified && this.hasAllItemsPlaced()) {
      this.btn_verify.removeAttribute('disabled');
    } else {
      this.btn_verify.setAttribute('disabled', '');
    }
    if (this.is_verified) {
      this.btn_reset.removeAttribute('disabled');
    } else {
      this.btn_reset.setAttribute('disabled', '');
    }
  }

  verify() {
    if (!this.hasAllItemsPlaced()) {
      alert(`Veuillez ordonner tous les éléments avant de vérifier!`);
      return;
    }

    const spanItems = this.node.querySelectorAll('.ordered-items ul li span');
    spanItems.forEach((span, index) => {
      const ordreObj = this.itemsOrder.find(obj => obj.id === span.id);
      span.draggable = false;
      if ((index + 1) === ordreObj.ordre) {
        span.classList.remove('badge-secondary', 'badge-danger');
        span.classList.add('badge-success');
      } else {
        span.classList.remove('badge-secondary', 'badge-success');
        span.classList.add('badge-danger');
      }
    });
    this.choix_div.style.display = 'none';
    this.is_verified = true;
    this.refreshButtons();
  }

  reset() {
    const spanItems = this.node.querySelectorAll('.ordered-items ul li span');
    spanItems.forEach(span => {
      span.draggable = true;
      span.classList.remove('badge-danger', 'badge-success');
      span.classList.add('badge-secondary');
      this.choix_div.appendChild(span);
    });
    this.choix_div.style.display = 'block';
    this.is_verified = false;
    this.refreshButtons();
  }
}

document.querySelectorAll('.order-items-exercise')
  .forEach(item => new ExerciceOrderItems(item));