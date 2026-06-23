import json
from urllib import request, error


def emotiondetector(text_to_analyze: str) -> dict:
    """
    Call the Watson NLP EmotionPredict endpoint with the given text.

    On success:
        Return dict with anger, disgust, fear, joy, sadness, dominant_emotion.
    On HTTP 400 (blank/invalid text):
        Return same dict structure with all values set to None.
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

    http_request = request.Request(
        url,
        data=data_bytes,
        headers=headers,
        method="POST",
    )

    try:
        with request.urlopen(http_request, timeout=10) as response:
            response_text = response.read().decode("utf-8")
    except error.HTTPError as http_err:
        # Task 7: handle 400 Bad Request (e.g., blank input)
        if http_err.code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }
        # For any other HTTP error, re-raise (or you could choose to return None)
        raise

    # Normal Task-3 behaviour for successful responses
    response_dict = json.loads(response_text)

    prediction = response_dict["emotionPredictions"][0]
    emotions = prediction["emotion"]

    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }
