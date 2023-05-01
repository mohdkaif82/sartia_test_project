$(document).ready(function () {
	//custom input
	bsCustomFileInput.init();
	//lightbox gallery
	$(document).on("click", '[data-toggle="lightbox"]', function (event) {
		event.preventDefault();
		$(this).ekkoLightbox({
			alwaysShowClose: true,
		});
	});
});
