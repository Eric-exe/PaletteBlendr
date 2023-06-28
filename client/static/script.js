$(document).ready(function () {
	// draggable color elements
	$("#original-palette-container").sortable();
	$("#original-palette-container").disableSelection();

	const originalPalette = document.getElementById("original-palette-container");
	const observer = new MutationObserver(function (mutations) {
		sendPostRequest();
	});
	const observerConfig = { childList: true };
	observer.observe(originalPalette, observerConfig);

	$("#new-palette-size-range").on("input", function () {
		sendPostRequest();
	});
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
	const colorCardTexts = $(".color-card-text-draggable");

	let colorID;
	switch (colorType) {
		case "hex":
			colorID = 0;
			break;
		case "rgb":
			colorID = 1;
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

function copyColorsID(colorType, id) {
	const colors = [];
	const colorCardTexts = $("#" + id).find(".color-card-text");
	console.log(colorCardTexts);

	let colorID;
	switch (colorType) {
		case "hex":
			colorID = 0;
			break;
		case "rgb":
			colorID = 1;
			break;
	}

	for (let i = 0; i < colorCardTexts.length; i++) {
		const colorCardText = colorCardTexts[i];
		const colorText = colorCardText.innerHTML.split("<br>")[colorID];
		const currentColor = colorText.split("</b> ")[1];
		colors.push(currentColor);
	}

	const colorsString = colors.join(", ");
	navigator.clipboard.writeText(colorsString);

	// show the copied message
	const popup = $("#popup");
	popup.removeClass("hidden");
	setTimeout(function () {
		popup.addClass("hidden");
	}, 1000);

	return colors;
}

// slider
$(document).ready(function () {
	const slider = $("#new-palette-size-range");

	slider.on("input", function () {
		$("#new-palette-size").text(slider.val());
	});
});

// get the new size of the palette
function getNewPaletteSize() {
	const slider = $("#new-palette-size-range");
	return slider.val();
}

function sendPostRequest() {
	const data = {
		colors: getColors("hex", true),
		new_size: getNewPaletteSize()
	};

	fetch("/api/color_lerp", {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify(data)
	})
		.then((response) => response.json())
		.then((data) => {
			updatePalettes("#rgb-palette-container", data.rgb);
			updatePalettes("#hsv-palette-container", data.hsv);
			updatePalettes("#lchab-palette-container", data.lchab);
			updatePalettes("#lchuv-palette-container", data.lchuv);
			updatePalettes("#lab-palette-container", data.lab);
			updatePalettes("#xyz-palette-container", data.xyz);
		})
		.catch((error) => {
			console.log("Error: " + error.message);
		});
}

function updatePalettes(id, colors) {
	const paletteContainer = $(id);
	paletteContainer.empty();
	if (colors.length == 0) {
		paletteContainer.html("No colors :(");
		return;
	}

	for (let i = 0; i < colors.length; i++) {
		const color = colors[i];
		const colorCard = createColorCard(color);
		paletteContainer.append(colorCard);
	}
}

function hexToRgb(hex) {
	// Convert hex color code to RGB
	const r = parseInt(hex.substring(1, 3), 16);
	const g = parseInt(hex.substring(3, 5), 16);
	const b = parseInt(hex.substring(5, 7), 16);
	return [r, g, b];
}

function createColorCard(color) {
	const cardElement = document.createElement("div");
	cardElement.classList.add("col-2", "p-1");

	const colorCard = document.createElement("div");
	colorCard.classList.add("card", "border-2", "color-card");

	const colorCardBody = document.createElement("div");
	colorCardBody.classList.add("card-body", "px-2", "py-1");

	const colorCardColor = document.createElement("div");
	colorCardColor.style.backgroundColor = color;
	colorCardColor.style.height = $(".pcr-button").css("height");
	colorCardColor.style.borderRadius = $(".pcr-button").css("border-radius");

	const colorCardText = document.createElement("div");
	colorCardText.classList.add("card-text", "color-card-text");
	let rgbColor = hexToRgb(color);
	rgbColor =
		"rgb(" + rgbColor[0] + ", " + rgbColor[1] + ", " + rgbColor[2] + ")";
	colorCardText.innerHTML = colorCardText.innerHTML =
		"<b>HEX:</b> " + color.toUpperCase() + "<br><b>RGB:</b> " + rgbColor;

	colorCardBody.appendChild(colorCardText);
	colorCard.appendChild(colorCardColor);
	colorCard.appendChild(colorCardBody);
	cardElement.appendChild(colorCard);

	return cardElement;
}

function showHidePalette(color) {
	if ($("#" + color + "-palette").hasClass("d-none")) {
		$("#" + color + "-palette").removeClass("d-none");
		$("#show-" + color + "-palette-button-content").html(`
		<div class="d-flex align-items-center" id="show-rgb-palette-button-content">
			<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-slash" viewBox="0 0 16 16">
				<path d="M13.359 11.238C15.06 9.72 16 8 16 8s-3-5.5-8-5.5a7.028 7.028 0 0 0-2.79.588l.77.771A5.944 5.944 0 0 1 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.134 13.134 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755-.165.165-.337.328-.517.486l.708.709z"/>
				<path d="M11.297 9.176a3.5 3.5 0 0 0-4.474-4.474l.823.823a2.5 2.5 0 0 1 2.829 2.829l.822.822zm-2.943 1.299.822.822a3.5 3.5 0 0 1-4.474-4.474l.823.823a2.5 2.5 0 0 0 2.829 2.829z"/>
				<path d="M3.35 5.47c-.18.16-.353.322-.518.487A13.134 13.134 0 0 0 1.172 8l.195.288c.335.48.83 1.12 1.465 1.755C4.121 11.332 5.881 12.5 8 12.5c.716 0 1.39-.133 2.02-.36l.77.772A7.029 7.029 0 0 1 8 13.5C3 13.5 0 8 0 8s.939-1.721 2.641-3.238l.708.709zm10.296 8.884-12-12 .708-.708 12 12-.708.708z"/>
	  		</svg>
			&nbsp;Hide
		</div>
		`);
		$("#" + color + "-palette-buttons").removeClass("d-none");
	} else {
		$("#" + color + "-palette").addClass("d-none");
		$("#show-" + color + "-palette-button-content").html(`
		<div class="d-flex align-items-center" id="show-rgb-palette-button-content">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye" viewBox="0 0 16 16">
				<path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z" />
				<path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z" />
			</svg>
			&nbsp;Show
		</div>
		`);
		$("#" + color + "-palette-buttons").addClass("d-none");
	}
}
