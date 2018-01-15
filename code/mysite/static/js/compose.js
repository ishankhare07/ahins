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
    .filter((kvPair) => new RegExp(name, 'g').test(kvPair))[0]  // we can write a blogpost about it
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
        $('#saving-loader').removeClass('active');
        $('#saved-icon').removeClass('hide');
        Materialize.toast('Saved successfully', 3000);
      }
    })
  }

  update(newBlob, type) {
    // show loading sign
    $('#saving-loader').addClass('active');
    $('#saved-icon').addClass('hide');

    if (type === 'title') {
      this.title = newBlob;
      if (this.updateTitleTimeout) {
        clearTimeout(this.updateTitleTimeout)
      }
      this.updateTitleTimeout = setTimeout(() => {
        this.updateFieldWithAjax(this.title, 'title');
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

function resizeIFrame(element) {
  console.log('resizing iframe');
  element.style.height = element.contentWindow.document.body.scrollHeight + 'px';
}

function reloadNewPreview(element) {
  element.contentWindow.location.reload();
}

function toggleFilesTab(event) {
  var compose_card_element = $('#compose-card');
  var files_card_element = $('#files-card');
  if (event.checked) {
    compose_card_element.removeClass('offset-m2');
    compose_card_element.removeClass('m8');
    files_card_element.removeClass('hide');
    compose_card_element.addClass('offset-m1');
    compose_card_element.addClass('m7');
  } else {
    compose_card_element.addClass('offset-m2');
    compose_card_element.addClass('m8');
    files_card_element.addClass('hide');
    compose_card_element.removeClass('offset-m1');
    compose_card_element.removeClass('m7');
  }
}
