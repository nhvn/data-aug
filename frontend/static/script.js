// script.js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const fileInput = document.querySelector("input[type='file']");
    const fileName = document.querySelector(".file-name");
    const errorMessage = document.querySelector(".error-message");
    const dropArea = document.getElementById('drop-area');

    // Handle file selection via input
    fileInput.addEventListener("change", function (event) {
        if (event.target.files.length > 0) {
            displayFileNames(event.target.files);
        } else {
            fileName.textContent = "";
        }
    });

    // Prevent default behaviors for drag-and-drop events
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    // Highlight drop area when file is dragged over it
    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, () => {
            dropArea.classList.add('dragging');
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, () => {
            dropArea.classList.remove('dragging');
        });
    });

    // Handle dropped files
    dropArea.addEventListener('drop', (e) => {
        const files = e.dataTransfer.files;
        handleFiles(files);
    });

    function handleFiles(files) {
        fileInput.files = files;  // Update the file input element with dropped files
        displayFileNames(files);  // Display file names
    }

    function displayFileNames(files) {
        if (files.length === 1) {
            fileName.textContent = files[0].name;
        } else {
            fileName.textContent = `${files.length} files selected`;
        }
        errorMessage.textContent = "";
    }

    // Form submission validation
    form.addEventListener("submit", function (event) {
        if (fileInput.files.length === 0) {
            event.preventDefault();
            errorMessage.textContent = "Please select or drop at least one image to upload!";
        } else {
            errorMessage.textContent = "";
        }
    });
});
