import asyncio
from googletrans import Translator


async def translate_text(text: str, dest: str = "hi") -> str:
    """
    Translate input text asynchronously using googletrans.

    Parameters:
    - text: str → Text to translate
    - dest: str → Target language (default: Hindi 'hi')

    Returns:
    - Translated text as string
    """
    async with Translator() as translator:
        result = await translator.translate(text, dest=dest)
        return result.text  # Return translated string


# Example usage
async def main():
    translated = await translate_text("my name is Manish Negi", dest="hi")
    print("Translated:", translated)


# Run async function
asyncio.run(main())

# if __name__ == "__main__":
# Indian language to Google Translate code
lang_to_code = {
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

# Reverse mapping: code → language
code_to_lang = {code: lang for lang, code in lang_to_code.items()}

# Example usage
print(lang_to_code["Hindi"])  # Output: hi
print(code_to_lang["ta"])  # Output: Tamil
