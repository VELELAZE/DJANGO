function toggleFullscreen() {
    const iconElement = document.getElementById('fullscreenIconElement');
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
        iconElement.classList.remove('fa-expand');
        iconElement.classList.add('fa-compress');
        localStorage.setItem('fullscreen', 'true'); // Save fullscreen state
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
            iconElement.classList.remove('fa-compress');
            iconElement.classList.add('fa-expand');
            localStorage.setItem('fullscreen', 'false'); // Save exit state
        }
    }
}

// Check fullscreen state on page load
document.addEventListener('DOMContentLoaded', () => {
    const fullscreenState = localStorage.getItem('fullscreen');
    const iconElement = document.getElementById('fullscreenIconElement');
    if (fullscreenState === 'true') {
        document.documentElement.requestFullscreen();
        iconElement.classList.remove('fa-expand');
        iconElement.classList.add('fa-compress');
    }
});

// Change icon on fullscreen change
document.addEventListener('fullscreenchange', () => {
    const iconElement = document.getElementById('fullscreenIconElement');
    if (document.fullscreenElement) {
        iconElement.classList.remove('fa-expand');
        iconElement.classList.add('fa-compress');
        localStorage.setItem('fullscreen', 'true'); // Update state
    } else {
        iconElement.classList.remove('fa-compress');
        iconElement.classList.add('fa-expand');
        localStorage.setItem('fullscreen', 'false'); // Update state
    }
});