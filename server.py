'''
Flask server for the Emotion Detection application.
Read input from UI and return response using EmotionDetection package
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def getemotions():
    '''
    Initiate index.html by default
    '''
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST", "GET"])
def detect_emotion():
    '''
    Read the text to analyze from request and
    return response along with dominant emotion
    '''
    if request.method == 'POST':
        req = request.get_json()
        text_to_analyze = req.get('textToAnalyze')

    if request.method == 'GET':
        text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
