"""
Emotion detection module for Watson NLP EmotionPredict service.

Task 2 requirement:
- Expose a function named `emotiondetector`
- Accept a text string as input
- Call the Watson EmotionPredict endpoint
- Return the `text` attribute of the HTTP response object (raw JSON string)
"""

import requests


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
        The response.text value returned by the EmotionPredict service.
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

    response = requests.post(url, headers=headers, json=payload, timeout=10)

    # Task 2: return the text attribute of the response object (no parsing yet)
    return response.text