import json
import requests

def is_invalid_input(text):
    if not isinstance(text, str):
        return True
    stripped = text.strip()
    if stripped == '':
        return True
    if stripped.isdigit():
        return True
    return False

def emotion_detector(text_to_analyze) -> None:
    '''
    read the text and return emotion score
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    custom_header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    if is_invalid_input(text_to_analyze):
        response.status_code = 400

    response = requests.post(url, json = input_json, headers = custom_header)
    
    if response.status_code == 200:
        formatted_result = json.loads(response.text)
        formatted_dict_result = dominant_emotion(formatted_result)
    elif response.status_code == 400:
        formated_dict_result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    return formatted_dict_result
    
def dominant_emotion(detected_text):
    emotions = detected_text['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    max_emotion = max(emotions, key=emotions.get)
    formated_dict_emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': max_emotion
    }
    return formated_dict_emotions
 

# print(emotion_detector("I hate working long hours."))