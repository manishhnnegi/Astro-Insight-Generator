import random


class DummyPredictor:
    """
    A dummy LLM client that generates zodiac-based insights
    without calling an external API.

    Useful for:
    - Local development (no API keys required).
    - Unit testing (predictable, reproducible responses).
    """

    RESPONSES = {
        "Aries": [
            "Your fiery spirit will open new doors today.",
            "Stay bold, Aries, but listen before you act.",
            "A spark of inspiration guides you forward.",
        ],
        "Taurus": [
            "Stability brings you peace today.",
            "Focus on small joys; they bring great comfort.",
            "Patience will reward your persistence.",
        ],
        "Gemini": [
            "Conversations bring clarity today.",
            "Your curiosity leads to a surprising discovery.",
            "Stay flexible, new opportunities may come suddenly.",
        ],
        "Cancer": [
            "Nurturing connections will warm your heart today.",
            "Trust your intuition—it’s stronger than logic.",
            "Emotional balance helps you thrive today.",
        ],
        "Leo": [
            "Your charisma draws people closer today.",
            "Take the spotlight—your voice matters.",
            "Confidence attracts the right kind of attention.",
        ],
        "Virgo": [
            "Organizing your thoughts clears your path.",
            "Attention to detail brings success today.",
            "Your practicality grounds those around you.",
        ],
        "Libra": [
            "Seek harmony in partnerships today.",
            "Balance leads to unexpected opportunities.",
            "Fairness will bring inner peace.",
        ],
        "Scorpio": [
            "Transformation begins within today.",
            "Your passion fuels breakthroughs.",
            "Embrace change—it’s on your side.",
        ],
        "Sagittarius": [
            "Adventure calls—step into the unknown.",
            "Optimism attracts opportunities today.",
            "Keep learning; wisdom guides your journey.",
        ],
        "Capricorn": [
            "Hard work brings steady progress.",
            "Discipline is your strength today.",
            "Focus on long-term goals, not quick wins.",
        ],
        "Aquarius": [
            "Innovation sparks fresh ideas today.",
            "Your unique perspective inspires others.",
            "Collaboration brings surprising results.",
        ],
        "Pisces": [
            "Creativity flows effortlessly today.",
            "Dreams reveal hidden guidance.",
            "Compassion strengthens your connections.",
        ],
    }

    def __init__(self, model: str = "dummy-zodiac-model"):
        """
        Initialize the DummyLLM.

        Parameters
        ----------
        model : str, optional
            Mock model identifier (default: "dummy-zodiac-model").
        """
        self.model = model

    def generate_text(self, zodiac: str, name: str) -> str:
        """
        Generate a personalized zodiac insight.

        Parameters
        ----------
        zodiac : str
            The zodiac sign (e.g., "Aries", "Taurus").
        name : str
            The user's name for personalization.

        Returns
        -------
        str
            A short personalized astrological message.
        """
        if zodiac not in self.RESPONSES:
            return f"{name}, today is a day of mystery and self-discovery."

        return f"{name}, {random.choice(self.RESPONSES[zodiac])}"


if __name__ == "__main__":
    # Demo run
    client = DummyPredictor()
    print(client.generate_text("Leo", "Ritika"))
    print(client.generate_text("Virgo", "Aman"))
    print(client.generate_text("Unknown", "Sam"))
