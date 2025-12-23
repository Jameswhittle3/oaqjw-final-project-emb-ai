"""
Emotion Detection Server

This script defines the Flask application for the emotion detection system.
It exposes endpoints for analyzing text and rendering the main page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the sentiment of the provided text.

    Retrieves text from the request arguments, passes it to the emotion_detector
    function, and returns a formatted string with the emotion scores.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant = response['dominant_emotion']

    if dominant is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application page.

    Serves the index.html template when the root URL is accessed.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
    