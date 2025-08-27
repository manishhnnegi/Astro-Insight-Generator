Here’s a polished **README.md** for your **Astro-Insight-Generator** project based on your directory and assignment content:

```markdown
# Astro-Insight-Generator

A personalized **Astrological Insight Generator** that provides daily astrological predictions based on the user's birth details. This service combines zodiac logic and LLM-based language generation, with optional multilingual support and caching.

---

## 📝 Problem Statement

This project takes a user's birth details (name, date, time, and location) and returns a personalized daily astrological insight. The system:

- Infers zodiac signs from birth date/time.
- Uses simplified or dummy astrology rules per zodiac.
- Generates natural language insights using a dummy or LLM-based pipeline.
- Supports multilingual outputs (e.g., Hindi) via translation modules.
- Implements caching to store and retrieve previous predictions.

---

## 🎯 Features

- **Zodiac Inference:** Calculates the user's zodiac sign from birth date.
- **LLM/Dummy Prediction:** Generates personalized insights.
- **Translation:** Supports multiple languages via Google Translate or dummy translations.
- **Caching:** Stores previous predictions for quick retrieval.
- **REST API:** Exposes a `/predict` endpoint for easy integration.

---

## 🧱 Project Structure

```

Astro-Insight-Generator/
│
├── app.py                     # Entry point to launch the app
├── config/
│   ├── config.py              # Configuration (models, server, API keys)
│   └── .env                   # Store GEMINI\_API\_KEY
│
├── src/
│   ├── interface/
│   │   ├── ui\_main.py         # UIStarter (orchestrates app launch)
│   │   └── ui\_backend.py      # Flask routes & backend logic
│   │
│   ├── model/
│   │   ├── model\_setup.py     # Loads Gemini LLM
│   │   └── model\_infer.py     # Prediction pipeline
│   │
│   ├── llms/
│   │   └── gemini\_client.py   # Gemini LLM wrapper
│   │
│   ├── prompts/
│   │   └── prompt.py          # Prompt templates
│   │
│   ├── translator/
│   │   └── translate.py       # Translation logic
│   │
│   └── cache/
│       └── cache.py           # Caching system
│
└── cache\_db/
└── cache.json             # Stores cached predictions

````

---

## 📌 Sample Input/Output

**Input:**

```json
{
  "name": "Ritika",
  "birth_date": "1995-08-20",
  "birth_time": "14:30",
  "birth_place": "Jaipur, India",
  "language": "en"
}
````

**Output:**

```json
{
  "zodiac": "Leo",
  "insight": "Your innate leadership and warmth will shine today. Embrace spontaneity and avoid overthinking.",
  "language": "en",
  "cached": false
}
```

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/Astro-Insight-Generator.git
cd Astro-Insight-Generator
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
# In config/.env
GEMINI_API_KEY=<YOUR_GOOGLE_GEMINI_API_KEY>
```

---

## 🚀 Running the Application

Run the app via **Flask**:

```bash
python app.py
```

By default, the API will be available at:

```
http://127.0.0.1:8000/predict
```

---

## 🛠 API Usage

Send a POST request with JSON payload:

```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{
    "name": "Ritika",
    "birth_date": "1995-08-20",
    "birth_time": "14:30",
    "birth_place": "Jaipur, India",
    "language": "en"
}'
```

---

## ⚙ Configuration

All runtime configuration is in `config/config.py`:

* `SERVER` → Flask host, port, debug
* `GEMINI_API_KEY` → API key for Google Gemini LLM
* `USE_DUMMY_LLM` → Toggle between dummy predictor and LLM
* `USE_DUMMY_TRANSLATION` → Toggle dummy translation

---

## 🧩 Notes on Design Choices

* **Modular Architecture:** Separate modules for zodiac calculation, translation, caching, LLM integration.
* **Dummy LLM:** Supports offline testing or early development.
* **Translation:** Supports multiple Indian languages using Google Translate or dummy translator.
* **Caching:** Stores previous predictions to improve performance and simulate personalization.

---

## 📚 Future Enhancements

* Replace dummy LLM with a real Google Gemini or OpenAI model.
* Integrate real Panchang data for precise astrological insights.
* Add user authentication and history tracking.
* Expand multilingual support to include more Indian languages.
* Add scoring/personalization for predictions.

---

## 👨‍💻 Author

Manish Negi

---

## 📄 License

MIT License

```

---

I can also create a **short version of README** specifically for GitHub repository **homepage** if you want, which is concise and looks professional with badges, quick start, and sample output.  

Do you want me to create that version as well?
```
