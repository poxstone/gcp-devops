import base64
import json
import logging

from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello():
    return 'works!'


@app.route('/cloudbuild_notify', methods=['POST'])
def receive_messages_handler():
    MESSAGES = []
    envelope = json.loads(request.data.decode('utf-8'))
    payload = base64.b64decode(envelope['message']['data'])
    MESSAGES.append(payload)
    logging.info('message_decoded: ', payload)

    return 'OK', 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
