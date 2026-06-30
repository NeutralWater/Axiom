def make_formula(formula, variables, units=None, topic=None, notes=None):
    return {
        "formula": formula,
        "variables": variables,
        "units": units,
        "topic": topic,
        "notes": notes
    }

def display_formula(data):
    print("\nFormula Used:")
    print(data["formula"])

    print("\nVariables:")
    for var, desc in data["variables"].items():
        print(f"{var} = {desc}")

    if data.get("units"):
        print("\nUnits:")
        print(data["units"])

    if data.get("topic"):
        print("\nTopic:")
        print(data["topic"])

    if data.get("notes"):
        print("\nNotes:")
        print(data["notes"])