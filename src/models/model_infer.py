"""
model_infer.py

Module for running model inference in the Astro Insight Generator.

Provides methods to:
- Compute zodiac sign from a birth date.
- Generate astrological insights using either a real LLM or a dummy predictor.
"""

from src.prompts.prompt import SUMMARY_PROMPT_TEMPLATE
from src.zodiac.zodiac import Zodiac
from src.llms.dummy_insight_generator import DummyPredictor


class ModelInference:
    """
    Handles astrological inference by integrating model setup, LLM, and dummy predictors.

    Responsibilities
    ----------------
    1. Generate personalized daily insights for a given zodiac and user name.
    2. Retrieve zodiac sign from birth date.
    3. Support both LLM-based and dummy prediction pipelines.

    Attributes
    ----------
    llm : object
        LLM object initialized by ModelSetUp to generate text-based insights.
    dummy_predictor : DummyPredictor
        Simple rule-based predictor for generating insights without an LLM.
    """

    def __init__(self, model_setup):
        """
        Initialize the ModelInference instance.

        Parameters
        ----------
        model_setup : ModelSetUp
            Object that holds the loaded LLM or other model configurations.
        """

        self.llm = model_setup.llm
        self.dummy_predictor = DummyPredictor()

    def generate_insight_from_llm(self, zodiac: str, name: str, language: str) -> str:
        """
        Generate a personalized astrological insight using the LLM.

        Parameters
        ----------
        zodiac : str
            Zodiac sign of the user.
        name : str
            Name of the user.
        language : str
            Language in which to generate the insight.

        Returns
        -------
        str
            Generated insight text. If the LLM fails, returns a fallback message.
        """

        try:
            prompt = SUMMARY_PROMPT_TEMPLATE.format(
                zodiac=zodiac, name=name, language=language
            )

            return self.llm.generate_text(prompt)
        except Exception:
            return f"{name}, as a {zodiac}, your grounded nature will guide you today."

    def get_zodiac_sign(self, birth_date):
        """
        Compute the zodiac sign from the user's birth date.

        Parameters
        ----------
        birth_date : str
            Date of birth in YYYY-MM-DD format.

        Returns
        -------
        str
            Zodiac sign corresponding to the birth date.
        """

        return Zodiac.get_zodiac(birth_date)

    def generate_insight_from_dummy_predictor(self, zodiac: str, name: str) -> str:
        """
        Generate a personalized insight using the dummy predictor (rule-based).

        Parameters
        ----------
        zodiac : str
            Zodiac sign of the user.
        name : str
            Name of the user.

        Returns
        -------
        str
            Generated insight text. Returns a fallback message if generation fails.
        """

        try:
            return self.dummy_predictor.generate_text(zodiac=zodiac, name=name)
        except Exception:
            return f"{name}, as a {zodiac}, your grounded nature will guide you today."
