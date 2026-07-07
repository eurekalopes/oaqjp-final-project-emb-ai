# Import libraries
from flask import Flask, redirect, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate Flask functionality
app = Flask(__name__)



@app.route("/")
def getemotions():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST", "GET"])
def detect_emotion():
    if request.method == 'POST':
        req = request.get_json()
        text_to_analyze = req.get('textToAnalyze')
    
    if request.method == 'GET':
        text_to_analyze = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] == None:
        return "Invalid text! Please try again!"
    else:
        return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
