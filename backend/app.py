from flask import Flask, jsonify, request
from tasks import prioritize_tasks
from notes import convert_speech_to_text
from utils import get_weather, get_news, get_quote

app = Flask(__name__)

@app.route('/api/prioritize', methods=['POST'])
def prioritize():
    tasks = request.json.get('tasks', [])
    prioritized = prioritize_tasks(tasks)
    return jsonify({'prioritized_tasks': prioritized})

@app.route('/api/quote')
def quote():
    return jsonify({'quote': get_quote()})

@app.route('/api/weather')
def weather():
    return jsonify(get_weather())

@app.route('/api/news')
def news():
    return jsonify(get_news())

@app.route('/api/speech-to-text', methods=['POST'])
def speech_to_text():
    audio_file = request.files['audio']
    text = convert_speech_to_text(audio_file)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
