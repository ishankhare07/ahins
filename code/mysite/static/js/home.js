window.onload = () => {
	$("#navToggle").sideNav();
	$("#settings_dropdown_button").dropdown({
		belowOrigin: true,
		constrainWidth: false,
	});

	$('#tabs.tabs').tabs();
	window.composeState = new CurrentState();
	console.log('composeState created');
}

// window.onload = function()
// {
//     if (window.jQuery)
//     {
//         alert('jQuery is loaded');
//     }
//     else
//     {
//         alert('jQuery is not loaded');
//     }
// }
