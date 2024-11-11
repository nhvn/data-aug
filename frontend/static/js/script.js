document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const fileInput = document.querySelector("#fileElem");
    const fileName = document.querySelector(".file-name");
    const errorMessage = document.querySelector(".error-message");
    const submitButton = document.querySelector("button[type='submit']");
    const dropArea = document.getElementById('drop-area');
    const loadingOverlay = document.getElementById('loading-overlay');
    const sampleButton = document.getElementById('load-samples');
    const clearButton = document.getElementById('clear-files');

    if (sampleButton) {
        sampleButton.addEventListener('click', async function() {
            try {
                // Sample images paths
                const sampleImages = [
                    '/projects/data-aug/applications/AugmentAI/static/samples/sample1.jpg',
                    '/projects/data-aug/applications/AugmentAI/static/samples/sample2.jpg',
                    '/projects/data-aug/applications/AugmentAI/static/samples/sample3.jpg'
                ];
                
                const fileList = new DataTransfer();
                
                for (const imagePath of sampleImages) {
                    const response = await fetch(imagePath);
                    if (!response.ok) {
                        throw new Error(`Failed to load ${imagePath}`);
                    }
                    const blob = await response.blob();
                    
                    // Create a new file with explicit image MIME type
                    const file = new File(
                        [blob], 
                        imagePath.split('/').pop(), 
                        { 
                            type: 'image/jpeg',  // Explicitly set MIME type
                            lastModified: new Date().getTime()
                        }
                    );
                    fileList.items.add(file);
                }
                
                fileInput.files = fileList.files;
                displayFileNames(fileInput.files);
                updateSubmitButton();
                
            } catch (error) {
                console.error('Error loading sample images:', error);
                errorMessage.textContent = "Error loading sample images. Please try uploading your own.";
            }
        });
    }

    function clearFiles() {
        if (fileInput) {
            // Clear the file input
            fileInput.value = '';
            // Create empty FileList
            const emptyFileList = new DataTransfer();
            fileInput.files = emptyFileList.files;
            // Update display
            fileName.textContent = '';
            // Hide the clear button
            clearButton.classList.add('hidden');
            // Update submit button state
            updateSubmitButton();
        }
    }

    if (clearButton) {
        clearButton.addEventListener('click', clearFiles);
    }
    
    function updateSubmitButton() {
        const hasFiles = fileInput.files.length > 0;
        submitButton.style.display = hasFiles ? 'inline-block' : 'none';
        submitButton.disabled = !hasFiles;
    }

    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const files = e.target.files;
            displayFileNames(files);
            updateSubmitButton();
        });
    }

    // Drop area functionality
    if (dropArea) {
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            document.addEventListener(eventName, preventDefaults, false);
            dropArea.addEventListener(eventName, preventDefaults, false);
        });

        ['dragenter', 'dragover'].forEach(eventName => {
            dropArea.addEventListener(eventName, highlight, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            dropArea.addEventListener(eventName, unhighlight, false);
        });

        dropArea.addEventListener('drop', handleDrop, false);
    }

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    function highlight(e) {
        dropArea.classList.add('dragging');
    }

    function unhighlight(e) {
        dropArea.classList.remove('dragging');
    }

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const items = dt.items;
        
        if (items) {
            // If it's a folder being dropped
            if (items[0].webkitGetAsEntry().isDirectory) {
                const entry = items[0].webkitGetAsEntry();
                traverseDirectory(entry).then(files => {
                    if (files.length > 0) {
                        const fileList = new DataTransfer();
                        files.forEach(file => {
                            if (file.type.startsWith('image/')) {
                                fileList.items.add(file);
                            }
                        });
                        fileInput.files = fileList.files;
                        displayFileNames(fileList.files);
                        updateSubmitButton();
                    }
                });
            } else {
                // If individual files are being dropped
                const files = dt.files;
                const fileList = new DataTransfer();
                for (let file of files) {
                    if (file.type.startsWith('image/')) {
                        fileList.items.add(file);
                    }
                }
                fileInput.files = fileList.files;
                displayFileNames(fileList.files);
                updateSubmitButton();
            }
        }
    }

    async function traverseDirectory(entry) {
        const files = [];
        
        async function readEntry(entry) {
            if (entry.isFile) {
                const file = await new Promise((resolve) => entry.file(resolve));
                if (file.type.startsWith('image/')) {
                    files.push(file);
                }
            } else if (entry.isDirectory) {
                const reader = entry.createReader();
                const entries = await new Promise((resolve) => {
                    reader.readEntries((entries) => resolve(entries));
                });
                for (const entry of entries) {
                    await readEntry(entry);
                }
            }
        }
        
        await readEntry(entry);
        return files;
    }

    function displayFileNames(files) {
        if (fileName && files) {
            if (files.length === 0) {
                fileName.textContent = "";
                clearButton.classList.add('hidden'); // Hide clear button
            } else if (files.length === 1) {
                fileName.textContent = files[0].name;
                clearButton.classList.remove('hidden'); // Show clear button
            } else {
                fileName.textContent = `${files.length} files selected`;
                clearButton.classList.remove('hidden'); // Show clear button
            }
            errorMessage.textContent = "";
        }
    }

    if (form) {
        form.addEventListener("submit", function (event) {
            if (fileInput.files.length === 0) {
                event.preventDefault();
                errorMessage.textContent = "Please select or drop at least one file to upload!";
                return;
            }
            
            if (fileInput.files.length > 10) {
                event.preventDefault();
                errorMessage.textContent = "Maximum 10 files allowed!";
                return;
            }

            errorMessage.textContent = "";
            
            // Show loading overlay before form submission
            loadingOverlay.classList.remove('hidden');

            // Hide loading overlay after 30 seconds
            setTimeout(() => {
                loadingOverlay.classList.add('hidden');
            }, 30000);
        });
    }

    // Initialize button state
    updateSubmitButton();
});