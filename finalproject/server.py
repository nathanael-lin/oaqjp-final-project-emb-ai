"""
Flask web application for the EmotionDetection package.

Exposes a web form that sends text to the emotiondetector function
and displays the emotion scores and dominant emotion.
"""

from flask import Flask, render_template, request, jsonify

from EmotionDetection import emotiondetector

app = Flask(__name__)


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
    Returns a JSON response with a formatted message.
    """
    data = request.get_json()
    text_to_analyze = data.get("textToAnalyze", "")

    # Call the emotion detection function
    result = emotiondetector(text_to_analyze)

    # Build the formatted message:
    # "For the given statement, the system response is anger X, disgust Y,
    # fear Z, joy A and sadness B. The dominant emotion is <name>."
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
