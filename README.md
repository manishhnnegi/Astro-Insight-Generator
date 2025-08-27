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

## 🛠 Tech Stack Justification

| Component / Tool                     | Purpose / Justification                                                                 |
|-------------------------------------|----------------------------------------------------------------------------------------|
| **Python 3.10+**                     | Simple, readable language with rich ecosystem for ML, NLP, and web development.        |
| **Flask**                            | Lightweight web framework for building REST APIs; easy to prototype and modularize.    |
| **Google Gemini / Dummy LLM**        | Generates personalized astrological insights; dummy LLM allows offline testing.       |
| **Google Translator / Dummy Translator** | Provides multilingual support (Hindi, Indian languages) for insights.               |
| **Cache (`cache.json`)**             | Stores previous predictions to improve performance and reduce redundant LLM calls.     |
| **Modular Design (`src/`)**          | Separates zodiac logic, prediction, translation, and caching for maintainability.      |
| **Environment Variables (`.env`)**   | Secure storage for API keys and secrets, follows best practices for config management. |
| **JSON-based REST API**              | Enables easy integration with web, mobile, or CLI clients to fetch astrological insights. |

---


## 📂 Project Structure

```
Astro-Insight-Generator/
│
├── app.py                     # Entry point to launch the app
├── config/
│   ├── config.py              # Configuration (models, server, API keys)
│   └── .env                   # Store GEMINI_API_KEY
│
├── src/
│   ├── interface/
│   │   ├── ui_main.py         # UIStarter (orchestrates app launch)
│   │   └── ui_backend.py      # Flask routes & backend logic
│   │
│   ├── model/
│   │   ├── model_setup.py     # Loads Gemini
│   │   └── model_infer.py     # prediction pipeline 
│   │
│   ├── llms/
│   │   └── gemini_client.py   # Gemini LLM wrapper
│   │
│   └── prompts/
│   │    └── prompt.py         # Prompt templates
│   │
│   └── translator/
│   │      └── translate.py         # translation logic
│   └── cache/
│       └── cache.py         # caching templates│ 
│
└── cache_db
│       └── cache.json     # for casining the requests.
│
└── requirements.txt           # Python dependencies

```

---

## 📂 Supported Languages for astro insights generation.

```

| Language     | Code |
| ------------ | ---- |
| Hindi        | hi   |
| Bengali      | bn   |
| Telugu       | te   |
| Marathi      | mr   |
| Tamil        | ta   |
| Urdu         | ur   |
| Gujarati     | gu   |
| Kannada      | kn   |
| Malayalam    | ml   |
| Punjabi      | pa   |
| Assamese     | as   |


```
---

## ⚡ Installation

1. Clone the repository:

```bash
git https://github.com/manishhnnegi/Astro-Insight-Generator.git
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
-d "{\"name\":\"Ganesh\",\"birth_date\":\"1999-08-20\",\"birth_time\":\"11:30\",\"birth_place\":\"Delhi, India\",\"language\":\"Hindi\"}"

```


---

## 🧪 Testing the API

Once the server is running (`python app.py`), you can test the `/predict` endpoint.

### Using `curl`

```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"name\":\"ramu\",\"birth_date\":\"1995-08-20\",\"birth_time\":\"14:30\",\"birth_place\":\"Jaipur, India\",\"language\":\"Hindi\"}"

```

Or you can run python test.py once your server is up.
```
python test.py

```

Some sample resopnses are inside cache_db.

```
{
  "RitikaK_1995-08-20": {
    "zodiac": "Leo",
    "insight": "తప్పకుండా! RitikaK అనే సింహరాశి జాతకురాలికి జ్యోతిష్య అంతర్దృష్టి ఇక్కడ ఉంది:\n\nRitikaK గారు, మీ సింహరాశి మిమ్మల్ని సహజంగానే నాయకురాలిని చేస్తుంది. మీలో ఆత్మవిశ్వాసం మెండుగా ఉంటుంది, దానిని సద్వినియోగం చేసుకోండి. సృజనాత్మకత మీ బలం, కళలు మరియు వినోదం పట్ల మీకున్న ఆసక్తిని పెంచుకోండి, అది మీకు ఆనందాన్ని ఇస్తుంది. ఈ సంవత్సరం మీ సంబంధాలలో వెచ్చదనం మరియు ప్రేమను నింపుతుంది.\n",
    "language": "Telugu"
  },
  "Geeta_1995-08-20": {
    "zodiac": "Leo",
    "insight": "नमस्ते गीता!\n\nयहाँ आपके लिए कुछ ज्योतिषीय अंतर्दृष्टि है:\n\n*   सिंह राशि होने के नाते, आप स्वाभाविक रूप से रचनात्मक और उत्साही हैं। अपनी इस ऊर्जा का उपयोग दूसरों को प्रेरित करने में करें।\n*   सितारे संकेत दे रहे हैं कि आपके नेतृत्व गुण इस समय चमक रहे हैं। अपनी क्षमताओं पर विश्वास रखें और आगे बढ़ें।\n*   यह समय आपके व्यक्तिगत विकास पर ध्यान केंद्रित करने का है। नई चीजें सीखें और अपने आत्मविश्वास को बढ़ाएं।\n",
    "language": "Hindi"
  }
}```

---

## 👨‍💻 Author

Manish Negi

---
