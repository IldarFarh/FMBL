import random
import os
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAHFNk7ZBIn0BAAhyeVnyqVPjeV5BB3pCgU2Oi4lAw4CkiLGZBZBUPT6uZC16OiWcnOZBya5ZBMu33GdcFvcWUxK7QsCBVoYqzZAK0e0mjaKlOu0Senwn8WN0BON2WiVDto0q5aj3fgHKvrSOB1hPMYJmzZA3YrU9DszyWTZCXOZCYWwZDZD'
VERIFY_TOKEN = 'SECRET'
bot = Bot(ACCESS_TOKEN)

@app.route('/', methods=['GET', 'POST'])
def recieve_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        if token_sent == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return 'Invalid verification token'
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = form_message()
                        send_message(recipient_id, response_sent_text)
                    if message['message'].get('attachments'):
                        response_sent_nontext = form_message()
                        send_message(recipient_id, response_sent_nontext)

def form_message():
    sample_responses = ["You are stunning!",
                        "We-re proud of you!",
                        "Keep on being you!",
                        "We're greatfull to know you!"]
    return random.choice(sample_responses)

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == '__main__':
    app.run()
