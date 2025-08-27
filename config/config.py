"""
config.py

Centralized configuration module for the Astro Insight Generator application.

This module defines global runtime settings, including:
- Device selection (CPU or GPU) for model execution.
- Model identifiers (e.g., Gemini LLM).
- Flask server settings (host, port, debug mode).
- API keys loaded from `.env`.
- Cache file path and dummy mode toggles.

Attributes
----------
Config.DEVICE : str
    Device to use for model execution ("cuda" if GPU is available, otherwise "cpu").

Config.MODELS : dict[str, str]
    Identifiers for models used in the project:
        - "GEMINI": str, name or version of the Gemini LLM.

Config.SERVER : dict[str, object]
    Flask server configuration:
        - "HOST": str, host address for the server (default "0.0.0.0").
        - "PORT": int, port number (default 8000).
        - "DEBUG": bool, debug mode toggle (default True).

Config.GEMINI_API_KEY : str | None
    API key for the Google Gemini LLM, loaded from `.env`.

Config.CACHE_FILE : str
    Path to the JSON cache file storing user insights.

Config.USE_DUMMY_LLM : bool
    Toggle to use dummy insight generation instead of calling Gemini LLM.

Config.USE_DUMMY_TRANSLATION : bool
    Toggle to use dummy translation instead of calling a real translation API.

Config.GENERATION_LANG : str
    Default language for text generation (e.g., "English"). First letter of language should be in uppercase.

Usage
-----
from config.config import Config

print(Config.DEVICE)
print(Config.MODELS["GEMINI"])
print(Config.SERVER["PORT"])
"""

import torch
import os
from dotenv import load_dotenv

# Load .env file (from config folder)
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)


class Config:
    """
    Global configuration for the application.

    Attributes
    ----------
    DEVICE : str
        The device to use for model execution ("cuda" if GPU available, otherwise "cpu").
    MODELS : dict[str, str]
        Dictionary of model identifiers:
            - "GEMINI": str, Gemini LLM identifier.
    SERVER : dict[str, object]
        Flask server configuration:
            - "HOST": str, host address for the server (default "0.0.0.0").
            - "PORT": int, port number (default 5000).
            - "DEBUG": bool, debug mode toggle (default True).
    GEMINI_API_KEY : str or None
        API key for Google Gemini LLM, loaded from `.env`.
    """

    DEVICE: str = "cuda" if torch.cuda.is_available() else "cpu"

    MODELS: dict[str, str] = {
        "GEMINI": "gemini-2.0-flash",
    }

    SERVER: dict[str, object] = {
        "HOST": "0.0.0.0",
        "PORT": 8000,
        "DEBUG": True,
    }

    GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")

    CACHE_FILE: str = "D:\Assignment_2\Astro-Insight-Generator\cache_db\cache.json"

    USE_DUMMY_LLM: bool = False
    USE_DUMMY_TRANSLATION: bool = False
    GENERATION_LANG: str = "English"  # should start from UpperCase


if __name__ == "__main__":
    m = Config.GEMINI_API_KEY
    m = Config.CACHE_FILE
    print(m)
