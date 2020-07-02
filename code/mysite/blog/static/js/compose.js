class CurrentState {
  constructor() {
    this.title = $('#markdown-title')[0].value;
    this.content = $('#markdown-content')[0].value;
    this.background_image = $('#markdown-bg')[0].value;
    this.timeToAjax = 2000;
  }

  isChanged(newBlob, type) {
    if (type === 'title' && this.title !== newBlob) {
      return true
    } else if (type === 'content' && this.content !== newBlob) {
      return true
    } else if (type === 'background_image' && this.background_image !== newBlob) {
      return true
    } else {
      return false
    }
  }

  updateFieldWithAjax(field, fieldType) {
    $.ajax({
      type: 'PUT',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'Content-Type': 'application/json'
      },
      data: JSON.stringify({
        [fieldType]: field
      }),
      success: (response) => {
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
    } else if (type === 'background_image') {
      this.background_image = newBlob
      if (this.updateBgTimeout) {
        clearTimeout(this.updateBgTimeout)
      }
      this.updateBgTimeout = setTimeout(() => {
        this.updateFieldWithAjax(this.background_image, 'background_image')
      }, this.timeToAjax);
    }
  }
}

function getCookie(name) {
  return document.cookie.split(';')
  .filter((kvPair) => new RegExp(name, 'g').test(kvPair))[0]  // we can write a blogpost about it
  .split('=')[1]
}


function autosaveBlob(event, type) {
  var blob = event.value;
  if (composeState.isChanged(blob, type)) {
    composeState.update(blob, type);
  }
}

function resizeIFrame(element) {
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

function copyToClipboard(elementId) {
  var range = document.createRange();
  range.selectNodeContents($(`#${elementId}`)[0]);
  window.getSelection().addRange(range);
  document.execCommand('Copy');
  window.getSelection().empty();
}

function renderUploadedFileListItem(result) {
  return `
      <li class="collection-item avatar">
        <img src="${result.image}" class="circle">
        <span id="image-id-${result.id}" class="title">${result.image}</span>
        <button class="secondary-content btn waves" onclick="copyToClipboard('image-id-${result.id}')">
          <i class="material-icons">content_copy</i>
        </button>
      </li>
      `
}

function uploadFile() {
  var formData = new FormData();
  var file = document.getElementById('file-field').files[0];
  var post_id = window.location.pathname.match(/\/(\d+)\/$/)[1];
  formData.append('image', file);
  formData.append('post_id', post_id);
  formData.append('name', file.name);


  var xhr = new XMLHttpRequest();
  xhr.open("POST", `/posts/images/${post_id}/`);
  xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));

  xhr.onreadystatechange = () => {
    if (xhr.readyState === 4 && (xhr.status >= 200 && xhr.status < 300 )) {
      $('#file-field')[0].value = null;
      $('.file-path')[0].value = null;
      $('#file-list').append(renderUploadedFileListItem(JSON.parse(xhr.responseText)));
    }
  }

  xhr.send(formData);
}

function initializeChips() {
  $('.chips-autocomplete').chips({
    data: [
      {
        tag: 'golang',
        id: 1
      },
      {
        tag: 'kubernetes',
        id: 2
      }
    ],
    autocompleteOptions: {
      data: {
        'golang': null,
        'docker': null,
        'kubernetes': null
      },
      minLength: 2
    },
    onChipAdd: (event, chips) => {
      console.log(event[0].M_Chips.chipsData);
    }
  });
}
