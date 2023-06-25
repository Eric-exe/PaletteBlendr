let colorPickrs = []; // array of pickr objects that the user created

$(document).ready(function () {
  const pickr = Pickr.create({
    el: ".color_picker",
    theme: "monolith", // or 'monolith', or 'nano'

    swatches: [
      "rgb(244, 67, 54)",
      "rgb(233, 30, 99)",
      "rgb(156, 39, 176)",
      "rgb(103, 58, 183)",
      "rgb(63, 81, 181)",
      "rgb(33, 150, 243)",
      "rgb(3, 169, 244)",
      "rgb(0, 188, 212)",
      "rgb(0, 150, 136)",
      "rgb(76, 175, 80)",
      "rgb(139, 195, 74)",
      "rgb(205, 220, 57)",
      "rgb(255, 235, 59)",
      "rgb(255, 193, 7)",
    ],

    lockOpacity: true,
    useAsButton: true,

    components: {
      // Main components
      preview: false,
      opacity: false,
      hue: true,

      // Input / output Options
      interaction: {
        input: true,
        save: true
      },
    },

    i18n: {
      "btn:save": "Add",
    },
  });

  pickr.on("save", (color, instance) => {
    // check if the outer palette container is hidden
    if ($("#original-palette-container-outer").hasClass("d-none")) {
      $("#original-palette-container-outer").removeClass("d-none");
    }

    const hexColor = color.toHEXA().toString();
    let rgbColor = color.toRGBA().toString(0);
    let hsvColor = color.toHSVA().toString(0);

    // remove alpha from rgb and hsv
    rgbColor = rgbColor.replace(", 1)", ")").replace("rgba", "rgb");
    hsvColor = hsvColor.replace(", 1)", ")").replace("hsva", "hsv");

    const cardElement = document.createElement("div");
    cardElement.classList.add("col-2");
    cardElement.classList.add("p-1");

    const colorCard = document.createElement("div");
    colorCard.classList.add("card");
    colorCard.classList.add("border-2");
    colorCard.classList.add("color-card");

    // x button
    const colorCardClose = document.createElement("button");
    colorCardClose.setAttribute("type", "button");
    colorCardClose.classList.add("btn-close");
    colorCardClose.classList.add("btn-close-white-filter");
    colorCardClose.setAttribute("aria-label", "Close");

    let colorCardColorPickr = document.createElement("div");
    const colorCardColor = document.createElement("div");
    colorCardColor.append(colorCardColorPickr);

    const colorCardBody = document.createElement("div");
    colorCardBody.classList.add("card-body");
    colorCardBody.classList.add("px-2");
    colorCardBody.classList.add("py-1");

    const colorCardText = document.createElement("div");
    colorCardText.classList.add("card-text");
    colorCardText.classList.add("color-card-text");
    colorCardText.innerHTML = "<b>HEX:</b> " + hexColor + "<br><b>RGB:</b> " + rgbColor + "<br><b>HSV:</b> " + hsvColor;

    colorCardBody.appendChild(colorCardText);
    colorCard.appendChild(colorCardColor);
    colorCard.appendChild(colorCardBody);
    colorCard.appendChild(colorCardClose);
    cardElement.appendChild(colorCard);

    $("#original-palette-container").append(cardElement);

    colorCardColorPickr = Pickr.create({
      el: colorCardColorPickr,
      theme: "monolith",
      default: hexColor,
      
      swatches: [
        "rgb(244, 67, 54)",
        "rgb(233, 30, 99)",
        "rgb(156, 39, 176)",
        "rgb(103, 58, 183)",
        "rgb(63, 81, 181)",
        "rgb(33, 150, 243)",
        "rgb(3, 169, 244)",
        "rgb(0, 188, 212)",
        "rgb(0, 150, 136)",
        "rgb(76, 175, 80)",
        "rgb(139, 195, 74)",
        "rgb(205, 220, 57)",
        "rgb(255, 235, 59)",
        "rgb(255, 193, 7)",
      ],

      lockOpacity: true,

      components: {
        // Main components
        preview: false,
        opacity: false,
        hue: true,

        // Input / output Options
        interaction: {
          input: true,
        }
      },
    });

    // everytime the pickr color is changed, update the color card
    colorCardColorPickr.on("change", (color, source, instance) => {

      colorCardColorPickr.applyColor();

      const hexColor = color.toHEXA().toString();
      let rgbColor = color.toRGBA().toString(0);
      let hsvColor = color.toHSVA().toString(0);

      // remove alpha from rgb and hsv
      rgbColor = rgbColor.replace(", 1)", ")").replace("rgba", "rgb");
      hsvColor = hsvColor.replace(", 1)", ")").replace("hsva", "hsv");

      colorCardText.innerHTML = "<b>HEX:</b> " + hexColor + "<br><b>RGB:</b> " + rgbColor + "<br><b>HSV:</b> " + hsvColor;
    });

    // add listener to the x button
    colorCardClose.addEventListener("click", (event) => {
      colorCardColorPickr.destroyAndRemove();
      cardElement.remove();

      // remove it from the array
      const index = colorPickrs.indexOf(colorCardColorPickr);
      if (index > -1) {
        colorPickrs.splice(index, 1);
      }
    });

    colorPickrs.push(colorCardColorPickr);

    colorCardColor.style.height =
      Math.floor(colorCard.offsetWidth / 2) + "px";
    
  });
});
