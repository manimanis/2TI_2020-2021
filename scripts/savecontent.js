class PagePersistance {
  constructor() {
    this.page_id = location.pathname;
    this.listeners = [];
    this.tokens = [];
    this.token = {};
    this.loadData();
  }

  validateToken(token_string) {
    try {
      const token = JSON.parse(token_string);
      const keys = ['data', 'date', 'name', 'token'];
      let valid = typeof token === 'object';
      const tokenKeys = Object.keys(token);
      valid = valid && tokenKeys
        .reduce((pv, cv) => pv && keys.includes(cv), valid);
      valid = valid && keys
        .reduce((pv, cv) => pv && tokenKeys.includes(cv), valid);
      valid = valid && typeof token.data === 'object' && Object
        .entries(token.data)
        .findIndex(arr => arr.findIndex(el => typeof el !== 'string') !== -1) === -1;
      return valid;
    } catch (err) {
      return false;
    }
  }

  setToken(token_string) {
    const token = JSON.parse(token_string);
    this.token.data = { ...token.data };
    this.token.date = token.date;
    this.notifyClients('load-token');
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

  resetData() {
    this.token.data = {};
    this.notifyClients('reset-data');
  }

  setName(name) {
    this.token.name = name;
    this.saveData();
  }

  getName() {
    return this.token.name;
  }
}

class ServerSaves {
  constructor() {
    this.url = 'saves.php';
    this.listeners = [];
    this.data = {};
  }

  addListener(listener) {
    this.listeners.push(listener);
  }

  _notify(event_name, data) {
    for (let listener of this.listeners) {
      listener(event_name, data, this);
    }
  }

  save(key, value) {
    this._notify('saving', null);
    $.post(this.url, { key: key, value: value }, (data) => {
      if (data.resultat === 'ok') {
        this.data = data.data;
        this._notify('saved', data.data);
      } else {
        this._notify('error', data.message);
      }
    }, 'json');
  }

  load(key) {
    this._notify('loading', null);
    $.getJSON(this.url, { key: key }, (data) => {
      if (data.resultat === 'ok') {
        this.data = data.data;
        this._notify('loaded', data.data);
      } else {
        this._notify('error', data.message);
      }
    });
  }

  getData(field) {
    return this.data[field];
  }
}

class UserInputSaver {
  constructor(node, localStore, serverStore) {
    this.node = $(node);
    this.localStore = localStore;
    this.serverStore = serverStore;
    this.buildUI();
    this.localStore.addListener((event_name) => {
      // console.log(event_name);
      this.update();
    });
    this.serverStore.addListener((event_name, data) => {
      // console.log(event_name, data);
      if (event_name === 'loading') {
        this._enableButtons(false);
        this.msg_span.text('Chargement en cours...');
      } else if (event_name === 'saving') {
        this._enableButtons(false);
        this.msg_span.text('Enregistrement en cours...');
      } else if (event_name === 'loaded') {
        this._enableButtons(true);
        this.localStore.setToken(data['valeur']);
        this.msg_span.text(`Loaded. Clé : ${data['cle']} - Création : ${data['creation_date']} - MAJ : ${data['update_date']}`);
      } else if (event_name === 'saved') {
        this._enableButtons(true);
        this.localStore.setToken(data['valeur']);
        this.msg_span.text(`Saved. Clé : ${data['cle']} - Création : ${data['creation_date']} - MAJ : ${data['update_date']}`);
      } else if (event_name === 'error') {
        this.msg_span.text('Erreur : ' + data);
      }
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
    this.btn_load = $('<button>')
      .addClass('btn btn-success ml-2')
      .text('Charger...')
      .appendTo(this.blk_saves_list)
      .on('click', (e) => {
        const key = prompt('Clé de sauvegarde');
        if (!key) {
          return;
        }
        this._loadFromServer(key);
      });
    this.btn_save = $('<button>')
      .addClass('btn btn-success ml-2')
      .text('Enregistrer')
      .appendTo(this.blk_saves_list)
      .on('click', (e) => {
        this._saveToServer();
      });
    this.msg_span = $('<span>')
      .addClass('small ml-2')
      .appendTo(this.blk_saves_list);

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
          thisObj.localStore.setData(div_id, input_ctrl.val());
          input_ctrl.hide();
          parent_div.find('pre')
            .show()
            .text(thisObj.localStore.getData(div_id) || placeholder);
        })
        .hide();
      $('<pre>')
        .text(thisObj.localStore.getData(div_id) || placeholder)
        .addClass('save-content-pre')
        .on('click', (e) => {
          const pre = $(e.target);
          const parent_div = pre.parent('div');
          const div_id = parent_div.attr('id');
          pre.hide();
          parent_div.find('.save-content')
            .show()
            .val(thisObj.localStore.getData(div_id) || '')
            .focus();
        })
        .appendTo(parent_div);
    });
  }

  update() {
    this._refreshInputs();
  }

  _saveToServer() {
    this.serverStore.save(
      this.serverStore.getData('cle'),
      JSON.stringify(this.localStore.token)
    );
  }

  _loadFromServer(key) {
    this.serverStore.load(key);
  }

  _enableButtons(enabled) {
    this.btn_load
      .attr('disabled', !enabled);
    this.btn_save
      .attr('disabled', !enabled);
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
        input_ctrl.val(thisObj.localStore.getData(div_id) || '');
        pre.text(thisObj.localStore.getData(div_id) || placeholder);

      });
  }
}
