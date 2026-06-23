"""
Flask web application for the EmotionDetection package.

Uses templates/ and static/ located at the repository root.
"""

import os

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotiondetector


# Resolve paths to templates and static one level above this file
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)  # repo root
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route("/", methods=["GET"])
def index():
    """
    Render the main page with the text input form.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def emotionDetector():
    """
    Endpoint called from the web page to analyze text emotions.

    Expects JSON body with key 'textToAnalyze'.
    Returns JSON with a formatted message describing emotions.
    """
    data = request.get_json()
    text_to_analyze = data.get("textToAnalyze", "")

    # Call the emotion detection function
    result = emotiondetector(text_to_analyze)

    # Build the formatted message:
    # For the given statement, the system response is anger A, disgust D,
    # fear F, joy J and sadness S. The dominant emotion is <name>.
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
    # Application needs to be deployed on localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
