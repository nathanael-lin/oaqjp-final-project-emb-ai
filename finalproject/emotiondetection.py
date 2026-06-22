"""
Emotion detection module for Watson NLP EmotionPredict service.

Task 3 requirement:
- Use the EmotionPredict endpoint (as in Task 2)
- Parse the JSON response
- Extract anger, disgust, fear, joy, sadness scores
- Compute the dominant emotion (highest score)
- Return a dictionary with those scores plus 'dominant_emotion'
"""

import json
from urllib import request


def emotiondetector(text_to_analyze: str) -> dict:
    """
    Call the Watson NLP EmotionPredict endpoint with the given text,
    then return the formatted result with individual emotion scores
    and the dominant emotion.

    Parameters
    ----------
    text_to_analyze : str
        The input text that needs to be analyzed for emotions.

    Returns
    -------
    dict
        Dictionary with keys:
        - 'anger'
        - 'disgust'
        - 'fear'
        - 'joy'
        - 'sadness'
        - 'dominant_emotion'
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": (
            "emotion_aggregated-workflow_lang_en_stock"
        ),
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze,
        }
    }

    data_bytes = json.dumps(payload).encode("utf-8")

    http_request = request.Request(url, data=data_bytes, headers=headers, method="POST")

    with request.urlopen(http_request, timeout=10) as response:
        response_text = response.read().decode("utf-8")

    # ---- Task 3 formatting logic ----

    # Convert JSON string to Python dictionary
    response_dict = json.loads(response_text)

    # Navigate to the emotion scores
    # structure: emotionPredictions[0]["emotion"]
    prediction = response_dict["emotionPredictions"][0]
    emotions = prediction["emotion"]

    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    # Find dominant emotion (highest score)
    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return dictionary in required format
    result = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }

    return result
