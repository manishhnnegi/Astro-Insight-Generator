"""
ui_backend.py

Flask-based UI backend module for the Astro Insight Generator.

This module defines the `UIInterface` class, which provides a REST API
to handle user requests for astrological insights. It integrates:
- Model inference via `ModelInference`.
- Translation (dummy or Google Translate) via `translator` classes.
- Local caching to store previously generated insights.
- Input validation and error handling.

Endpoints
---------
POST /predict
    Accepts a JSON payload with user birth details and returns a personalized
    astrological insight in the requested language.

Example Request:
----------------
{
    "name": "Ritika",
    "birth_date": "1995-08-20",
    "birth_time": "14:30",
    "birth_place": "Jaipur, India",
    "language": "Hindi"
}

Example Response:
-----------------
{
    "zodiac": "Leo",
    "insight": "[Hindi Translation] Ritika, Take the spotlight—your voice matters.",
    "language": "Hindi",
    "cached": False
}
"""

from flask import Flask, request, jsonify
from src.utils.utils import Utils
from src.translator.translate import DummyTranslator, TranslateWithGoogle
from src.cache.cache import Cache
from config.config import Config


class UIInterface:
    """
    UI backend class that manages Flask routes, model inference, translation,
    and caching for the Astro Insight Generator application.

    Attributes
    ----------
    app : Flask
        The Flask application instance.
    model_infer : ModelInference
        Object that provides zodiac computation and insight generation.
    cache : Cache
        Caching object to store previously generated predictions.
    translator : DummyTranslator or TranslateWithGoogle
        Translation handler depending on configuration.

    Methods
    -------
    _register_routes():
        Registers Flask routes, currently only /predict.

    predict():
        Handles POST requests to /predict, performs input validation, checks cache,
        generates zodiac sign and insight, translates the text if required, caches
        the result, and returns a JSON response.

    run(host='0.0.0.0', port=8000, debug=True):
        Starts the Flask server with the specified host, port, and debug mode.
    """

    def __init__(self, model_infer):
        self.app = Flask(__name__)
        self.model_infer = model_infer
        self.cache = Cache()
        self._register_routes()
        if Config.USE_DUMMY_TRANSLATION:
            self.translator = DummyTranslator()
        else:
            self.translator = TranslateWithGoogle()

    def _register_routes(self):
        """
        Register all Flask routes for the UI backend.

        Currently registers:
        - POST /predict : Handles prediction requests for astrological insights.
        """
        self.app.add_url_rule("/predict", "predict", self.predict, methods=["POST"])

    def predict(self):
        """
        Handle POST requests to /predict endpoint.

        Workflow:
        1. Parse JSON input for name, birth_date, birth_time, birth_place, and language.
        2. Validate required fields and date format.
        3. Check if insight is cached; return cached result if available.
        4. Compute zodiac sign from birth_date.
        5. Generate insight using either dummy predictor or LLM.
        6. Translate insight if requested language is not English.
        7. Cache the generated result.
        8. Return a JSON response with zodiac, insight, language, and cached status.

        Returns
        -------
        Flask Response (JSON)
            {
                "zodiac": str,
                "insight": str,
                "language": str,
                "cached": bool
            }
        Or, in case of error:
            {
                "error": str
            }
        """

        try:
            data = request.get_json(force=True)
            name = data.get("name")
            birth_date = data.get("birth_date")
            birth_time = data.get("birth_time")
            birth_place = data.get("birth_place")
            language = data.get("language", "English")

            if language not in self.translator.lang_to_code:
                language = "English"
                print(
                    "Choice of language not Supported or LAnguage name not started with Upper Case!!"
                )

            if not all([name, birth_date, birth_time, birth_place]):
                return jsonify({"error": "Missing required fields"}), 400
            if not Utils.validate_date(birth_date):
                return jsonify({"error": "Invalid date format"}), 400

            key = Utils.user_key(name, birth_date)

            cached = self.cache.get(key)
            if cached:
                return jsonify({**cached, "cached": True})

            zodiac = self.model_infer.get_zodiac_sign(birth_date)

            if Config.USE_DUMMY_LLM:
                insight = self.model_infer.generate_insight_from_dummy_predictor(
                    zodiac, name
                )
                if language != "English":
                    language_code = self.translator.lang_to_code[language]
                    translated = self.translator.translate(insight, language_code)

                else:
                    translated = insight
            else:
                insight = self.model_infer.generate_insight_from_llm(
                    zodiac, name, language
                )

                translated = insight

            self.cache.set(key, zodiac, translated, language)

            return jsonify(
                {
                    "zodiac": zodiac,
                    "insight": translated,
                    "language": language,
                    "cached": False,
                }
            )

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def run(self, host="0.0.0.0", port=8000, debug=True):
        """
        Start the Flask web server.

        Parameters
        ----------
        host : str, optional
            Host address for the server (default is "0.0.0.0").
        port : int, optional
            Port number to run the server on (default is 8000).
        debug : bool, optional
            Enable or disable Flask debug mode (default is True).

        This method blocks and runs the Flask server to handle incoming API requests.
        """

        self.app.run(host=host, port=port, debug=debug)
