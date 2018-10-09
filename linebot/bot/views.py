from django.shortcuts import render
from django.http import HttpResponse
import json
import random
import requests
import bot
# Create your views here.
def index(request):
    return HttpResponse("This is bot api.")

def callback(request):
    reply = ""
    request_json = json.loads(request.body.decode('utf-8'))
    for e in request_json['events']:
        reply_token = e['replyToken']
        message_type = e['message']['type']

        if message_type == 'text':
            text = e['message']['text']
            reply += reply_text(reply_token, text)

    return HttpResponse(reply)

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = 'iQNQAmcTmzwsgLFEHfM1x92IxXkfQ9DvgQL47wq8cMk7E6YQG07yeFaYIOZDNN6RfpUga6jQH5Lpx2RzD8JrA4whRO0xlbv4M9Z9mOy8kaHaIaxBrp+we/Kea5wuuYPjL7wUxgA3W1tWKne3UJyU/QdB04t89/1O/w1cDnyilFU='
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

def reply_text(reply_token, text):
    reply = random.choice(bot.load_serif.random_serif)
    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"text",
                    "text": reply
                }
            ]
    }

    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload))
    return reply
