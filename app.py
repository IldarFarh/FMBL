from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def recieve_message():
    if request.method == 'GET':
        return 'This is python answering'
    else:
        output = request.get_json()
        return 'This is python answering'

if __name__ == '__main__':
    app.run()
