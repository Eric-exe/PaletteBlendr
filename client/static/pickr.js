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
        save: true,
      },
    },

    i18n: {
      "btn:save": "Add",
    },
  });
});
