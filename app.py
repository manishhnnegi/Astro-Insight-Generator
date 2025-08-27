"""
app.py

Main entry point for launching the Flask-based Astro Insight Generator application.

This script initializes the UI layer (`UIStarter`), which sets up:
- Model configuration and loading (e.g., Gemini LLM or dummy predictor).
- Astrological insight generation pipeline.
- Flask web server for user interaction via REST API.

Usage
-----
Run the application with:

    python app.py

Server configuration (host, port, debug mode) is defined in `config/config.py`.

Notes
-----
`UIStarter.start()` handles:
1. Loading global configuration and models.
2. Setting up the model inference pipeline.
3. Launching the Flask UI backend to handle `/predict` requests.
"""


# import sys
# import os

# sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from src.interface.ui_main import UIStarter


def main():
    """
    Entry point function to start the Flask application.

    Calls `UIStarter.start()`, which initializes models,
    sets up inference, and launches the UI interface.
    """

    UIStarter.start()


if __name__ == "__main__":
    main()
