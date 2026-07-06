import json
import requests

def emotion_detector(text_to_analyze) -> None:
    '''
    read the text and return emotion score
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    custom_header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers = custom_header)
    formatted_result = json.loads(response.text)
    print(formatted_result)
    print(response.status_code)

emotion_detector("I love this new tehnology")