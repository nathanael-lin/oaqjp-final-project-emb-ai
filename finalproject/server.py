"""
Flask web application for the EmotionDetection package.

Exposes a web interface that calls the emotiondetector function and
displays emotion scores and the dominant emotion.
"""

import os

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotiondetector


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route("/", methods=["GET"])
def index():
    """
    Render the main page with the text input form.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotionDetector():  # pylint: disable=invalid-name
    """
    Analyze emotions in the provided text and return a formatted message.

    For blank or invalid input, returns an error message instead.
    """
    if request.method == "GET":
        text_to_analyze = request.args.get("textToAnalyze", "")
    else:
        data = request.get_json(silent=True) or {}
        text_to_analyze = data.get("textToAnalyze", "")

    result = emotiondetector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify({"response": "Invalid text! Please try again!"})

    message = (
        "For the given statement, the system response is "
        f"anger {result['anger']}, "
        f"disgust {result['disgust']}, "
        f"fear {result['fear']}, "
        f"joy {result['joy']} and "
        f"sadness {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": message})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
