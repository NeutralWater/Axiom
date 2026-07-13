# Axiom v2.0.0

A modular, offline STEM computation toolkit built with Python and Flask.

Axiom provides quick access to mathematical formulas, engineering calculators, scientific constants, unit conversions, digital electronics utilities, and matrix operations through both a terminal interface and a local website.

> [!NOTE]
> Axiom v3.0.0 is currently in development. The upcoming release introduces
> an interactive graphing workspace with multiple expressions, custom axis
> ranges, pan, zoom, and PNG export.

---

## Features

- 15 STEM modules
- 260 formula solvers and utilities
- Local Flask website
- Original terminal interface
- Built-in formula explanations
- Searchable scientific constants library
- Dynamic matrix input generator
- Vector and matrix operations
- Calculus expression support
- Statistical dataset calculations
- Truth table generator
- 2–6 variable Karnaugh map generator
- Boolean expression simplifier
- Modular project structure
- Runs locally without an internet connection
- Interactive 2D graphing workspace *(v3 development preview)*
- Multiple function plotting
- Custom graph ranges
- Pan, scroll zoom, and PNG export
- Graphing access from both the terminal and website

---
## Graphing Preview

Axiom's upcoming v3.0.0 release includes an interactive local graphing
workspace powered by SymPy and Plotly.

Currently supported:

- Explicit functions such as `x^2`, `sin(x)`, and `sqrt(x)`
- Multiple expressions on one graph
- Custom x-axis and y-axis ranges
- Mouse panning and scroll-wheel zooming
- PNG export
- Offline operation
- Website and terminal launching

3D graphing and additional graph types are planned.

---

## Modules

- Aerospace Engineering
- Algebra
- Astronomy
- Calculus
- Chemistry
- Computer Science
- Constants
- Conversions
- Digital Electronics
- Electrical Engineering
- Geometry
- Linear Algebra
- Mechanical Engineering
- Physics
- Statistics

More modules and utilities are planned.

---

## Axiom v2.0.0

Version 2.0.0 introduces a complete Flask-based interface while preserving the original terminal toolkit.

### Website Features

- Automatically generated module and solver pages
- Input fields based on formula parameters
- Support for mathematical functions and expressions
- Comma-separated statistical datasets
- Boolean expression inputs
- Dynamic matrix dimensions and input grids
- Searchable constants reference page
- Formula, variable, unit, topic, and note displays
- Responsive dark interface
- Local operation without external services

---

## Project Structure

```text
Axiom/
│
├── formulas/
│   ├── algebra.py
│   ├── calculus.py
│   ├── constant_values.py
│   ├── digital_electronics.py
│   ├── linear_algebra.py
│   └── ...
│
├── formula_display/
│   ├── core.py
│   ├── display_algebra.py
│   ├── display_calculus.py
│   └── ...
│
├── runners/
│   ├── algebra_runner.py
│   ├── calculus_runner.py
│   └── ...
│
├── topic_lib/
│   ├── menu.py
│   ├── algebra_lib.py
│   └── ...
│
├── website/
│   ├── web_registry.py
│   │
│   ├── templates/
│   │   ├── index.html
│   │   ├── module.html
│   │   ├── solver.html
│   │   ├── constants.html
│   │   └── about.html
│   │
│   └── static/
│       ├── style.css
│       └── script.js
│
├── app.py
├── main.py
├── sysinfo.py
├── README.md
└── LICENSE
```

---

## Website Preview

The website organizes every subject into its own module page. Each solver generates the appropriate inputs and displays its formula, variables, units, topic, and notes.

Special interfaces support:

- Matrices with custom row and column dimensions
- Vectors and collections of vectors
- Comma-separated statistical datasets
- Calculus functions such as `x^2 + sin(x)`
- Boolean expressions such as `(A AND B) OR NOT C`
- Searchable scientific constants

---

## Terminal Preview

```text
╔════════════════════════════════════════════╗
║                   AXIOM                    ║
║               Version 2.0.0                ║
╠════════════════════════════════════════════╣
║ Status         : ONLINE                    ║
║ Formula Modules: 14 Loaded                 ║
║ Total Formulas : 260 Available             ║
║ Constant Library: Loaded                   ║
║ Formula Database: Ready                    ║
╠════════════════════════════════════════════╣
║                                            ║
║ [1] Algebra                                ║
║ [2] Calculus                               ║
║ [3] Constants                              ║
║ [4] Conversions                            ║
║ [5] Geometry                               ║
║ [6] Physics                                ║
║ [7] Statistics                             ║
║ [8] Linear Algebra                         ║
║ [9] Chemistry                              ║
║ [10] Astronomy                             ║
║ [11] Computer Science                      ║
║ [12] Electrical Engineering                ║
║ [13] Digital Electronics                   ║
║ [14] Aerospace Engineering                 ║
║ [15] Mechanical Engineering                ║
║ [16] Graphing                              ║
║                                            ║
║ [0] Exit                                   ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Requirements

- Python 3.14+
- Flask
- SymPy

Install the required packages:

```bash
python -m pip install flask sympy
```

---

## Running the Website

From the main Axiom directory, run:

```bash
python app.py
```

Open the local address displayed in the terminal:

```text
http://127.0.0.1:5000
```

---

## Running the Terminal Interface

```bash
python main.py
```

---

## Current Capabilities

### Mathematics

- Algebraic calculations
- Derivatives and integrals
- Limits and critical points
- Statistical mean and range
- Geometry calculations
- Vector operations
- Matrix operations and decompositions
- Systems of linear equations

### Science

- Physics calculations
- Chemistry calculations
- Astronomy calculations
- Scientific and mathematical constants
- Unit conversions

### Engineering

- Aerospace engineering
- Electrical engineering
- Mechanical engineering
- Digital electronics
- Computer science utilities

### Digital Electronics

- Boolean expression simplification
- Truth table generation
- 2–6 variable Karnaugh maps
- Support for `AND`, `OR`, `NOT`, `XOR`, `&`, `|`, `~`, and `^`

---

## Future Plans

- Graphing support
- Formula favorites
- Calculation history
- Circuit analysis tools
- Enhanced matrix visualizations
- Additional unit conversions
- More STEM modules
- Finance module
- Expanded formula search

---

## License

Axiom is available under the MIT License.

---

*Aut viam inveniam aut faciam.*