window.onload = () => {
	$("#navToggle").sideNav();
	$("#settings_dropdown_button").dropdown({
		belowOrigin: true,
		constrainWidth: false,
	});
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
