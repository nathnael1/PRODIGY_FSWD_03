function displayFileName() {
    var input = document.getElementById('file-upload');
    var fileNameDisplay = document.getElementById('file-upload-filename');

    if (input.files && input.files.length > 0) {
        fileNameDisplay.textContent = input.files[0].name;
    } else {
        fileNameDisplay.textContent = '';
    }
}
