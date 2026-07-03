from sysinfo import formula_count, module_count


def menu():
    width = 44

    def border(left, middle, right):
        print(left + middle * width + right)

    def line(text=""):
        print("║" + text[:width].ljust(width) + "║")

    def centered(text):
        print("║" + text[:width].center(width) + "║")

    def row(label, value):
        text = f"{label:<16}: {value}"
        line(text)

    border("╔", "═", "╗")
    centered("AXIOM")
    centered("Version 1.2.0")
    border("╠", "═", "╣")

    row(" Status", "ONLINE")
    row(" Formula Modules", f"{module_count()} Loaded")
    row(" Total Formulas", f"{formula_count()} Available")
    row(" Constant Library", "Loaded")
    row(" Formula Database", "Ready")

    border("╠", "═", "╣")
    line()

    modules = [
        "Algebra",
        "Calculus",
        "Constants",
        "Conversions",
        "Geometry",
        "Physics",
        "Statistics",
        "Linear Algebra",
        "Chemistry",
        "Astronomy",
        "Computer Science",
        "Electrical Engineering",
        "Digital Electronics",
        "Aerospace Engineering",
        "Mechanical Engineering",
    ]

    for i, module in enumerate(modules, start=1):
        line(f" [{i}] {module}")

    line()
    line(" [0] Exit")
    line()
    border("╚", "═", "╝")
    print()