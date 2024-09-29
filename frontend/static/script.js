// script.js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const fileInput = document.querySelector("input[type='file']");
    const fileName = document.querySelector(".file-name");
    const errorMessage = document.querySelector(".error-message");

    fileInput.addEventListener("change", function (event) {
        if (event.target.files.length > 0) {
            if (event.target.files.length === 1) {
                fileName.textContent = event.target.files[0].name;
            } else {
                fileName.textContent = `${event.target.files.length} files selected`;
            }
            errorMessage.textContent = "";
        } else {
            fileName.textContent = "";
        }
    });

    form.addEventListener("submit", function (event) {
        if (fileInput.files.length === 0) {
            event.preventDefault();
            errorMessage.textContent = "Please select at least one image to upload!";
        } else {
            errorMessage.textContent = "";
        }
    });
});