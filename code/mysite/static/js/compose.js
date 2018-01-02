class CurrentState {
  constructor() {
    this.title = $('#markdown-title')[0].value;
    this.content = $('#markdown-content')[0].value;
    this.timeToAjax = 2000;
  }

  isChanged(newBlob, type) {
    if (type === 'title' && this.title !== newBlob) {
      return true
    } else if (type === 'content' && this.content !== newBlob) {
      return true
    } else {
      return false
    }
  }

  getCookie(name) {
    return document.cookie.split(';')
    .filter((kvPair) => new RegExp(name, 'g').test(kvPair))[0]
    .split('=')[1]
  }

  updateFieldWithAjax(field, fieldType) {
    $.ajax({
      type: 'PUT',
      headers: {
        'X-CSRFToken': this.getCookie('csrftoken'),
        'Content-Type': 'application/json'
      },
      data: JSON.stringify({
        [fieldType]: field
      }),
      success: (response) => {
        console.log(response)
        console.log('successfully saved');
      }
    })
  }

  update(newBlob, type) {
    if (type === 'title') {
      this.title = newBlob;
      if (this.updateTitleTimeout) {
        clearTimeout(this.updateTitleTimeout)
      }
      this.updateTitleTimeout = setTimeout(() => {
        this.updateFieldWithAjax(this.title, 'title')
      }, this.timeToAjax);
    } else if (type === 'content') {
      this.content = newBlob
      if (this.updateContentTimeout) {
        clearTimeout(this.updateContentTimeout)
      }
      this.updateContentTimeout = setTimeout(() => {
        this.updateFieldWithAjax(this.content, 'content')
      }, this.timeToAjax);
    }
  }
}

function autosaveBlob(event, type) {
  var blob = event.value;
  if (composeState.isChanged(blob, type)) {
    composeState.update(blob, type);
  }
}
