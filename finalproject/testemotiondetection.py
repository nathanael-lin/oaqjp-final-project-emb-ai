"""
Unit tests for the EmotionDetection package.

Validates that the dominant emotion matches expectations
for a set of predefined input sentences.
"""

import unittest

from EmotionDetection import emotiondetector


class TestEmotionDetection(unittest.TestCase):
    """
    Test cases for emotiondetector function.
    """

    def test_joy(self):
        """
        Statement: 'I am glad this happened' -> dominant_emotion should be 'joy'.
        """
        result = emotiondetector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """
        Statement: 'I am really mad about this' -> dominant_emotion should be 'anger'.
        """
        result = emotiondetector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """
        Statement: 'I feel disgusted just hearing about this' -> dominant_emotion should be 'disgust'.
        """
        result = emotiondetector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """
        Statement: 'I am so sad about this' -> dominant_emotion should be 'sadness'.
        """
        result = emotiondetector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """
        Statement: 'I am really afraid that this will happen' -> dominant_emotion should be 'fear'.
        """
        result = emotiondetector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
