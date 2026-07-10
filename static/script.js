const searchBar = document.getElementById("searchBar");
const cards = document.querySelectorAll(".module-card");

searchBar.addEventListener("input", () => {
    const query = searchBar.value.toLowerCase();

    cards.forEach(card => {
        const text = card.innerText.toLowerCase();

        if (text.includes(query)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
});