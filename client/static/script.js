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
}
