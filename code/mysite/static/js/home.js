window.onload = () => {
	$("#navToggle").sideNav();
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
	if ($('#markdown-content')) {
		var ta = $('#markdown-content')[0];
		ta.style.height = ta.scrollHeight + 'px';
	}
}
