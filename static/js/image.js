 function openModal(imageUrl) {
    document.getElementById("modalImage").src = imageUrl;
    document.getElementById("imageModal").classList.remove("hidden");
}

function closeModal() {
    document.getElementById("imageModal").classList.add("hidden");
}