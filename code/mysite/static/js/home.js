$(document).ready(() => {
	$(".sidenav").sidenav();
	$("#settings_dropdown_button").dropdown({
		belowOrigin: true,
		constrainWidth: false,
	});

	$('#tabs.tabs').tabs({
		onShow: (t) => {
			if (t[0].id === 'preview') {
				$('#md-preview')[0].contentWindow.location.reload();
			}
		}
	});

	if (typeof CurrentState !== 'undefined') {
		// instantiate current state if the class is available
		window.composeState = new CurrentState();
	}

	// set textarea height
	if ($('#markdown-content') === true) {
		var ta = $('#markdown-content')[0];
		ta.style.height = ta.scrollHeight + 'px';
	}

	$('#file-bottom-sheet').modal({
		ready: function(modal, trigger) {
			var post_id = window.location.pathname.match(/\/(\d+)\/$/)[1];
			$.ajax({
				type: 'GET',
				url: `/posts/images/${post_id}`,
				headers: {
	        'X-CSRFToken': getCookie('csrftoken'),
	        'Content-Type': 'application/json'
	      },
				success: (response) => {
					var file_list = $('#file-list');
					if (response.results) {
						for(var i of response.results) {
							file_list.append(renderUploadedFileListItem(i));
						}
					}
				}
			})
		},
		complete: () => {
			$('#file-list').empty();
		}
	});

	$('.chips-autocomplete').chips({
		autocompleteOptions: {
			data: {
				'golang': null,
				'docker': null,
				'kubernetes': null
			}
		},
		onChipAdd: function(event) {
			console.log('tag added');
		}
	});
});
