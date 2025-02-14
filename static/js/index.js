document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".like-button").forEach(button => {
        let postId = button.getAttribute("data-post-id");
        let likesCountElem = document.getElementById(`likes-count-${postId}`);
        let icon = button.querySelector("i");

        // Boshlang‘ich rangni belgilash (bosilgan bo‘lsa qizil, bo‘lmasa oppoq)
        let isLiked = button.getAttribute("data-liked") === "true";
        icon.style.color = isLiked ? "red" : "white";

        button.addEventListener("click", function () {
            let url = `/posts/likes/${postId}/like/`;

            fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                credentials: "same-origin"
            })
            .then(response => response.json())
            .then(data => {
                if (data.liked) {
                    icon.style.color = "red";
                    button.setAttribute("data-liked", "true");
                } else {
                    icon.style.color = "white";
                    button.setAttribute("data-liked", "false");
                }
                likesCountElem.textContent = `${data.likes_count} likes`;
            })
            .catch(error => console.error("Error:", error));
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            document.cookie.split(";").forEach(cookie => {
                let trimmedCookie = cookie.trim();
                if (trimmedCookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(trimmedCookie.substring(name.length + 1));
                }
            });
        }
        return cookieValue;
    }
});
