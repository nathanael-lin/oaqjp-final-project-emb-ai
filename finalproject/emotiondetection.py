"""
Emotion detection module for Watson NLP EmotionPredict service.

Task 2 requirement:
- Expose a function named `emotiondetector`
- Accept a text string as input
- Call the Watson EmotionPredict endpoint
- Return the `text` attribute of the HTTP response object (raw JSON string)
"""

import json
from urllib import request


def emotiondetector(text_to_analyze: str) -> str:
    """
    Call the Watson NLP EmotionPredict endpoint with the given text
    and return the raw response text.

    Parameters
    ----------
    text_to_analyze : str
        The input text that needs to be analyzed for emotions.

    Returns
    -------
    str
        The response body decoded as text (equivalent to response.text).
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
        # Read bytes and decode to string, same idea as response.text
        response_text = response.read().decode("utf-8")

    return response_text
