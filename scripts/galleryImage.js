<script>
    const galleryImages = document.querySelectorAll('#image-gallery .gallery img');

    galleryImages.forEach((image) => {
        image.addEventListener('click', () => {
            const overlay = document.createElement('div');
            overlay.classList.add('overlay');

            const largeImage = document.createElement('img');
            largeImage.src = image.src;
            largeImage.alt = image.alt;

            overlay.appendChild(largeImage);

            overlay.addEventListener('click', () => {
                overlay.remove();
            });

            document.body.appendChild(overlay);
        });
    });
	</script>