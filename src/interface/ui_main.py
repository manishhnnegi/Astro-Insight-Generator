"""
ui_main.py

Module to initialize and launch the Astro Insight Generator UI backend.

This module defines the `UIStarter` class, which orchestrates:
- Loading global configuration from `Config`.
- Setting up the model pipeline via `ModelSetUp` and `ModelInference`.
- Launching the Flask-based UI interface (`UIInterface`) for handling API requests.

Classes
-------
UIStarter
    Orchestrates the configuration, model initialization, and UI server launch.
"""

from config.config import Config
from src.models.model_setup import ModelSetUp
from src.models.model_infer import ModelInference
from src.interface.ui_backend import UIInterface


class UIStarter:
    """
    Orchestrator class for initializing and launching the Astro Insight Generator backend.

    Responsibilities
    ----------------
    1. Load global configuration (server settings, API keys, toggles).
    2. Initialize the model setup (`ModelSetUp`) and inference pipeline (`ModelInference`).
    3. Start the Flask UI interface (`UIInterface`) for handling `/predict` requests.

    Methods
    -------
    launch():
        Starts the Flask server with configured host, port, and debug mode.

    start() -> classmethod:
        Convenience method to create a `UIStarter` instance and immediately launch the server.
    """

    def __init__(self):
        self.config = Config()
        self.model_setup = ModelSetUp()
        self.model_infer = ModelInference(self.model_setup)
        self.ui_interface = UIInterface(self.model_infer)

    def launch(self):
        self.ui_interface.run(
            host=self.config.SERVER["HOST"],
            port=self.config.SERVER["PORT"],
            debug=self.config.SERVER["DEBUG"],
        )

    @classmethod
    def start(cls):
        run = cls()
        run.launch()
