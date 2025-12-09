import requests
import json

def emotion_detector(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    object_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=object_json, headers=header)
    formatted_response = json.loads(response.text)

    emotions=dict()

    if response.status_code == 400:
        
        emotions['anger']= None
        emotions['disgust']= None
        emotions['fear']= None
        emotions['joy']= None
        emotions['sadness']= None
        emotions['dominant_emotion']= None
        return emotions

    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    emotions['dominant_emotion']= max(emotions,key=emotions.get)

    return emotions