// draggable color elements
$(document).ready(function () {
	$("#original-palette-container").sortable();
	$("#original-palette-container").disableSelection();
});

// clear original palette
function clearOriginalPalette() {
	for (let i = 0; i < colorPickrs.length; i++) {
		colorPickrs[i].destroyAndRemove();
	}
	colorPickrs = [];

	$("#original-palette-container").empty();
	$("#original-palette-container-outer").addClass("d-none");
	$("#original-palette-buttons").addClass("d-none");
	$("#original-palette-size").text(0);
}

// Copy functions
// get the colors from the color-card-text elements
// This is because the pickrs can be dragged around but
// the order of the pickrs in the array is not updated
function getColors(colorType) {
	const colors = [];
	const colorCardTexts = $(".color-card-text");

	let colorID;
	switch (colorType) {
		case "hex":
			colorID = 0;
			break;
		case "rgb":
			colorID = 1;
			break;
		case "hsv":
			colorID = 2;
			break;
	}

	for (let i = 0; i < colorCardTexts.length; i++) {
		const colorCardText = colorCardTexts[i];
		const colorText = colorCardText.innerHTML.split("<br>")[colorID];
		const currentColor = colorText.split("</b> ")[1];
		colors.push(currentColor);
	}

	return colors;
}

function copyColors(colorType) {
	const colors = getColors(colorType);
	const colorsString = colors.join(", ");
	navigator.clipboard.writeText(colorsString);

	// show the copied message
	const popup = $("#popup");
	popup.removeClass("hidden");
	setTimeout(function () {
		popup.addClass("hidden");
	}, 1000);
}

// slider
$(document).ready(function () {
	const slider = $("#new-palette-size-range");

	slider.on("input", function () {
		$("#new-palette-size").text(slider.val());
	});
});
