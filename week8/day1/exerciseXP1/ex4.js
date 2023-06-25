var form = document.getElementById('MyForm');
var volumeInput = document.getElementById('volume');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    var radius = parseFloat(document.getElementById('radius').value);
    var volume = calculateVolume(radius);

    volumeInput.value = volume.toFixed(2);
});

function calculateVolume(radius) {
    var volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
    return volume;
}