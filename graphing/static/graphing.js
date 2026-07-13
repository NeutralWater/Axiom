const expressionRows = document.getElementById("expressionRows");
const graphButton = document.getElementById("graphButton");
const addExpressionButton = document.getElementById("addExpression");
const downloadGraphButton = document.getElementById("downloadGraph");
const xMinInput = document.getElementById("xMin");
const xMaxInput = document.getElementById("xMax");
const graphStatus = document.getElementById("graphStatus");
const plot = document.getElementById("plot");
const yMinInput = document.getElementById("yMin");
const yMaxInput = document.getElementById("yMax");

const COLORS = [
    "#60a5fa",
    "#f472b6",
    "#34d399",
    "#fbbf24",
    "#a78bfa",
    "#fb7185",
];

let colorIndex = 0;
let debounceTimer;



function addExpression(value = "") {
    const row = document.createElement("div");

    row.className = "expression-row";

    row.innerHTML = `
        <input
            class="expression-color"
            type="color"
            value="${COLORS[colorIndex % COLORS.length]}"
            aria-label="Function color"
        >

        <span class="expression-prefix">y =</span>

        <input
            class="expression-input"
            type="text"
            value="${value}"
            placeholder="x^2 + 2*x - 3"
            autocomplete="off"
        >

        <button
            class="remove-expression"
            type="button"
            aria-label="Remove expression"
        >
            ×
        </button>
    `;

    colorIndex += 1;

    row
        .querySelector(".remove-expression")
        .addEventListener("click", () => {
            row.remove();

            if (!expressionRows.children.length) {
                addExpression();
            }

            scheduleGraph();
        });

    row
        .querySelector(".expression-input")
        .addEventListener("input", scheduleGraph);

    row
        .querySelector(".expression-color")
        .addEventListener("input", scheduleGraph);

    expressionRows.appendChild(row);
}


function getPayload() {
    return {
        x_min: xMinInput.value,
        x_max: xMaxInput.value,
        samples: 801,

        expressions: [
            ...expressionRows.querySelectorAll(".expression-row"),
        ].map(row => ({
            expression: row.querySelector(".expression-input").value,
            color: row.querySelector(".expression-color").value,
        })),
    };
}


function setStatus(message = "", type = "") {
    graphStatus.textContent = message;
    graphStatus.className = `graph-status ${type}`;
}


async function graphFunctions() {
    setStatus("Graphing…");

    graphButton.disabled = true;
    const yMin = Number(yMinInput.value);
    const yMax = Number(yMaxInput.value);

    if (
        !Number.isFinite(yMin)
        || !Number.isFinite(yMax)
        || yMin >= yMax
    ) {
        setStatus(
            "The minimum y value must be smaller than the maximum.",
            "error"
        );

        return;
    }

    try {
        const response = await fetch("/graphing/api", {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify(getPayload()),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.error
                || "Axiom could not graph those functions."
            );
        }

        const traces = data.traces.map(trace => ({
            x: trace.x,
            y: trace.y,
            name: trace.name,

            type: "scatter",
            mode: "lines",
            connectgaps: false,

            line: {
                color: trace.color,
                width: 2.5,
            },

            hovertemplate:
                "x = %{x:.4g}<br>y = %{y:.4g}<extra>"
                + trace.name
                + "</extra>",
        }));

        await Plotly.react(
            plot,
            traces,
            {
                paper_bgcolor: "#111827",
                plot_bgcolor: "#111827",

                font: {
                    color: "#e2e8f0",
                },

                margin: {
                    l: 58,
                    r: 24,
                    t: 24,
                    b: 52,
                },

                xaxis: {
                    title: "x",
                    gridcolor: "#263244",
                    zerolinecolor: "#64748b",
                    linecolor: "#64748b",
                },

                yaxis: {
                    title: "y",
                    range: [yMin, yMax],
                    gridcolor: "#263244",
                    zerolinecolor: "#64748b",
                    linecolor: "#64748b",
                },

                legend: {
                    orientation: "h",
                    y: 1.12,
                },

                hovermode: "closest",
                dragmode: "pan",

                // Preserves zoom and pan while expressions update.
                uirevision: "axiom-graph",
            },
            {
                responsive: true,
                scrollZoom: true,
                displaylogo: false,

                modeBarButtonsToRemove: [
                    "zoom2d",
                    "select2d",
                    "lasso2d",
                ]
            }
        );

        setStatus(data.errors?.join(" ") || "");

    } catch (error) {
        setStatus(error.message, "error");

    } finally {
        graphButton.disabled = false;
    }
}


function scheduleGraph() {
    clearTimeout(debounceTimer);

    debounceTimer = setTimeout(
        graphFunctions,
        350
    );
}


addExpression("x^2");
addExpression("sin(x)");

addExpressionButton.addEventListener("click", () => {
    addExpression();

    expressionRows
        .lastElementChild
        .querySelector(".expression-input")
        .focus();
});

graphButton.addEventListener("click", graphFunctions);

xMinInput.addEventListener("change", graphFunctions);
xMaxInput.addEventListener("change", graphFunctions);
yMinInput.addEventListener("change", graphFunctions);
yMaxInput.addEventListener("change", graphFunctions);

downloadGraphButton.addEventListener("click", () => {
    Plotly.downloadImage(plot, {
        format: "png",
        filename: "axiom-graph",
        width: 1400,
        height: 900,
        scale: 2,
    });
});

graphFunctions();