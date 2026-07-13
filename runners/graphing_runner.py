import os
import subprocess
import sys
import time
import urllib.request
import webbrowser
from pathlib import Path


GRAPHING_URL = "http://127.0.0.1:5000/graphing"


def server_is_running():
    try:
        with urllib.request.urlopen(
            GRAPHING_URL,
            timeout=1,
        ) as response:
            return response.status == 200

    except Exception:
        return False


def start_website():
    project_root = Path(__file__).resolve().parents[1]

    options = {
        "cwd": project_root,
    }

    if os.name == "nt":
        options["creationflags"] = subprocess.CREATE_NEW_CONSOLE

    subprocess.Popen(
        [
            sys.executable,
            str(project_root / "app.py"),
        ],
        **options,
    )


def run_graphing():
    print("Launching Axiom Graphing Workspace...")

    if not server_is_running():
        print("Starting the local Axiom website...")
        start_website()

        for _ in range(20):
            time.sleep(0.5)

            if server_is_running():
                break

    if server_is_running():
        print("Opening Graphing Workspace in your browser.")
        webbrowser.open(GRAPHING_URL)

    else:
        print("Axiom could not start the Graphing Workspace.")
        print("Try running: python app.py")