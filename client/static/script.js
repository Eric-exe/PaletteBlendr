// initialize popover
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl)
})
// Background color change

const body = document.querySelector('body');
let rotation = 0;

function rotateBackground() {
    rotation++;
    rotation %= 360;

    body.style.background = `linear-gradient(${rotation}deg, #AC32E4 0%, #7918F2 48%, #4801FF 100%)`;
    body.style.backgroundAttachment = 'fixed';
    body.style.overscrollBehavior = 'none';

    requestAnimationFrame(rotateBackground);
}

rotateBackground();