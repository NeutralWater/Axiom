const searchBar = document.getElementById("searchBar");
const cards = document.querySelectorAll(".module-card");

if (searchBar) searchBar.addEventListener("input", () => {
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

document.querySelectorAll(".matrix-builder").forEach(builder => {
    const rowsInput = builder.querySelector(".matrix-rows");
    const colsInput = builder.querySelector(".matrix-cols");
    const grid = builder.querySelector(".matrix-grid");
    const hiddenInput = builder.querySelector(".matrix-value");

    function generateMatrix(values = null) {
        const rows = Math.max(1, Math.min(10, Number(rowsInput.value) || 1));
        const cols = Math.max(1, Math.min(10, Number(colsInput.value) || 1));
        grid.innerHTML = "";
        grid.style.gridTemplateColumns = `repeat(${cols}, minmax(64px, 1fr))`;

        for (let row = 0; row < rows; row++) {
            for (let col = 0; col < cols; col++) {
                const cell = document.createElement("input");
                cell.type = "number";
                cell.step = "any";
                cell.required = true;
                cell.className = "matrix-cell";
                cell.setAttribute("aria-label", `Row ${row + 1}, column ${col + 1}`);
                cell.value = values?.[row]?.[col] ?? "";
                grid.appendChild(cell);
            }
        }
    }

    builder.querySelector(".generate-matrix").addEventListener("click", () => generateMatrix());

    let previousValues = null;
    try {
        previousValues = JSON.parse(hiddenInput.value);
        if (Array.isArray(previousValues) && previousValues.length) {
            rowsInput.value = previousValues.length;
            colsInput.value = previousValues[0].length;
        }
    } catch (_) {}
    generateMatrix(previousValues);

    builder.closest("form").addEventListener("submit", () => {
        const rows = Number(rowsInput.value);
        const cols = Number(colsInput.value);
        const cells = [...grid.querySelectorAll(".matrix-cell")];
        const matrix = [];
        for (let row = 0; row < rows; row++) {
            matrix.push(cells.slice(row * cols, (row + 1) * cols).map(cell => cell.value));
        }
        hiddenInput.value = JSON.stringify(matrix);
    });
});
