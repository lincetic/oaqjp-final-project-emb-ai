"""
File server.py
Web application using Flask
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion():
    """
    sent emotion by interface
    get a text to analyze and return formatted text
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    response_dict = dict(response)

    if response_dict['dominant_emotion'] is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

    last_item_pop = response_dict.pop('dominant_emotion')
    response_dict = str(response_dict).strip("{}")
    response_item_and = response_dict.rsplit(",",1)
    response_dict = " y".join(response_item_and)

    return f"""Para la declaración dada, la respuesta del sistema es {response_dict}.
            La emoción dominante es {last_item_pop}."""

@app.route("/")
def render_index_page():
    """
    index page interface
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
