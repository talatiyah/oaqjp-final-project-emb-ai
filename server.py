"""Flask application for final project emotion detection."""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Display the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze text and display the detected emotions."""
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        "The dominant emotion is "
        f"<b>{result['dominant_emotion']}.</b>"
    )

if __name__ == "__main__":
    app.run()
