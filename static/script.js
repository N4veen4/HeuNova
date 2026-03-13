document.addEventListener('DOMContentLoaded', () => {
    const intro = document.getElementById('intro-screen');
    const appContent = document.getElementById('app-content');
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const resultArea = document.getElementById('result-area');
    const previewOriginal = document.getElementById('preview-original');
    const previewColorized = document.getElementById('preview-colorized');
    const colorizeBtn = document.getElementById('colorize-btn');
    const downloadLink = document.getElementById('download-link');
    const processingOverlay = document.getElementById('processing-overlay');

    let currentFile = null;

    // --- Intro Sequence ---
    setTimeout(() => {
        intro.classList.add('fade-out');
        appContent.classList.remove('hidden');
        appContent.style.opacity = '0';
        setTimeout(() => {
            appContent.style.transition = 'opacity 1.5s ease-out';
            appContent.style.opacity = '1';
        }, 50);
        setTimeout(() => intro.remove(), 1000);
    }, 2000); // Original timing for the letters reveal

    // --- File Handling ---
    dropZone.addEventListener('click', () => fileInput.click());

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.style.borderColor = "#3fb950";
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.style.borderColor = "rgba(255, 255, 255, 0.08)";
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        const files = e.dataTransfer.files;
        if (files.length) handleFile(files[0]);
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) handleFile(e.target.files[0]);
    });

    function handleFile(file) {
        if (!file.type.startsWith('image/')) {
            alert('Please upload an image file');
            return;
        }
        currentFile = file;
        const reader = new FileReader();
        reader.onload = (e) => {
            previewOriginal.src = e.target.result;
            previewColorized.src = e.target.result; // Temporary
            resultArea.classList.remove('hidden');
            downloadLink.classList.add('hidden');
            resultArea.scrollIntoView({ behavior: 'smooth' });
        };
        reader.readAsDataURL(file);
    }

    // --- Colorization Logic ---
    colorizeBtn.addEventListener('click', async () => {
        if (!currentFile) return;

        processingOverlay.classList.remove('hidden');
        colorizeBtn.disabled = true;

        const formData = new FormData();
        formData.append('file', currentFile);

        try {
            const response = await fetch('/api/colorize', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) throw new Error('Colorization failed');

            const data = await response.json();

            previewColorized.src = data.result;
            downloadLink.href = data.result;
            downloadLink.download = 'huenova_colorized.png';
            downloadLink.classList.remove('hidden');

        } catch (error) {
            console.error(error);
            alert('Error colorizing image. Please try again.');
        } finally {
            processingOverlay.classList.add('hidden');
            colorizeBtn.disabled = false;
        }
    });
});
