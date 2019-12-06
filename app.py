from flask import Flask, request
from classes.game import Person, bcolors

app = Flask(__name__)

magic = [{"name": "Fire", "cost": 10, "dmg":120},
         {"name": "Water", "cost": 5, "dmg":80},
         {"name": "Air", "cost": 7, "dmg":113}]


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

@app.route('/', methods=['GET', 'POST'])
def recieve_message():
    if request.method == 'GET':
        response = form_response({'text': 'start', 'payload': 'bubu'})
        return response
    else:
        payload = request.get_json()
        response = form_response(payload)
        return response


def form_response(payload):
    if payload["text"] == 'start':
        return player.choose_action()


if __name__ == '__main__':
    app.run()
