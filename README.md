# SmartDesk

SmartDesk is a personal productivity dashboard built with Flask and vanilla HTML/JS. It provides the following features:

- AI-powered Task Prioritization using OpenAI's GPT
- Weather Updates
- Top News Headlines
- Daily Inspirational Quote
- Speech-to-Text Notes (Optional)

---

## Project Structure

```
smartdesk/
├── backend/
│   ├── app.py                # Flask app
│   ├── tasks.py              # Task prioritization logic
│   ├── utils.py              # Weather, news, quote
│   ├── notes.py              # Speech-to-text (if used)
│   ├── config.py             # API keys
│   └── requirements.txt      # Python dependencies
├── frontend/
│   ├── index.html            # Main interface
│   ├── styles.css            # Optional styling
```

---

## How to Run

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/smartdesk.git
cd smartdesk/backend
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Add Your API Keys
Create a file called `config.py` inside the `backend/` folder:
```python
# config.py
OPENAI_API_KEY = "your-openai-api-key"
WEATHER_API_KEY = "your-weather-api-key"
NEWS_API_KEY = "your-news-api-key"
```

### Step 4: Run the App
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## Task Prioritization (How it works)
- The user enters tasks in a textarea.
- The backend sends those tasks to OpenAI's GPT model.
- The model replies with a prioritized list based on urgency and importance.

---

## Optional Features
You can also extend this project to include:
- Speech-to-text note-taking
- Google Calendar integration
- AI daily planner

---

## Acknowledgements
- OpenAI for GPT API
- News & Weather APIs

---

## Preview
![SmartDesk Screenshot](screenshot.png) <!-- Optional if you want to show off the UI -->
