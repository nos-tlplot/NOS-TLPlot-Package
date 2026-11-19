import os
import sys

from streamlit.web import cli as stcli

THEME_ARGS = [
    "--theme.base", "dark",
    "--theme.primaryColor", "#dbedffff",
    "--theme.backgroundColor", "#0E1117",
    "--theme.secondaryBackgroundColor", "#262730",
    "--theme.textColor", "#FAFAFAff",
    "--server.maxUploadSize", "50",
]

def run_app():
    app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py")
    sys.argv = ["streamlit", "run", app_path] + THEME_ARGS
    sys.exit(stcli.main())

if __name__ == "__main__":
    run_app()
