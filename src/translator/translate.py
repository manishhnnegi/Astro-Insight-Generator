"""
translate.py

Translation module for the Astro Insight Generator application.

Provides classes and methods to:
- Translate text to multiple Indian languages and English.
- Offer both real Google Translate integration and dummy translation for testing.
- Support synchronous translation calls suitable for Flask endpoints.

Classes
-------
TranslateWithGoogle
    Uses Google Translator API asynchronously and provides a synchronous wrapper.
DummyTranslator
    Simulates translation by prefixing text with language markers (useful for testing).
"""

import asyncio
from googletrans import Translator as GoogleTranslator


class TranslateWithGoogle:
    """
    Translator class using Google Translator API asynchronously.

    Attributes
    ----------
    lang_to_code : dict[str, str]
        Maps human-readable language names to Google Translator language codes.
    code_to_lang : dict[str, str]
        Reverse mapping of language codes to language names.
    """

    def __init__(self):
        self.lang_to_code = {
            "English": "en",
            "Hindi": "hi",
            "Bengali": "bn",
            "Telugu": "te",
            "Marathi": "mr",
            "Tamil": "ta",
            "Urdu": "ur",
            "Gujarati": "gu",
            "Kannada": "kn",
            "Malayalam": "ml",
            "Odia": "or",
            "Punjabi": "pa",
            "Assamese": "as",
            "Maithili": "mai",
            "Sanskrit": "sa",
            "Konkani": "kok",
            "Kashmiri": "ks",
            "Nepali": "ne",
            "Sindhi": "sd",
            "Dogri": "doi",
            "Bodo": "brx",
        }
        self.code_to_lang = {code: lang for lang, code in self.lang_to_code.items()}

    async def _translate_async(self, text: str, dest: str = "hi") -> str:
        """
        Asynchronously translate a given text to a target language.

        Parameters
        ----------
        text : str
            Text to be translated.
        dest : str, optional
            Destination language code (default is 'hi' for Hindi).

        Returns
        -------
        str
            Translated text.
        """

        async with GoogleTranslator() as translator:
            result = await translator.translate(text, dest=dest)
            return result.text

    def translate(self, text: str, dest: str = "hi") -> str:
        """
        Synchronous wrapper for Flask usage.
        """
        return asyncio.run(self._translate_async(text, dest))


class DummyTranslator:
    """
    Dummy translation class for testing or development purposes.

    Simulates translation by adding language-specific prefixes.
    """

    def __init__(self):
        self.lang_to_code = {
            "English": "en",
            "Hindi": "hi",
            "Bengali": "bn",
            "Telugu": "te",
            "Marathi": "mr",
            "Tamil": "ta",
            "Urdu": "ur",
            "Gujarati": "gu",
            "Kannada": "kn",
            "Malayalam": "ml",
            "Odia": "or",
            "Punjabi": "pa",
            "Assamese": "as",
            "Maithili": "mai",
            "Sanskrit": "sa",
            "Konkani": "kok",
            "Kashmiri": "ks",
            "Nepali": "ne",
            "Sindhi": "sd",
            "Dogri": "doi",
            "Bodo": "brx",
        }

        self.code_to_lang = {code: lang for lang, code in self.lang_to_code.items()}

    def translate(self, text: str, language: str) -> str:
        return "[Translation] " + text


if __name__ == "__main__":
    tt = TranslateWithGoogle()
    insight = "my name is Manish Negi"
    language = "Tamil"

    translated = tt.translate(insight, tt.lang_to_code[language])

    print(translated)
