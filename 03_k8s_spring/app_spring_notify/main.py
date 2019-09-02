import base64
import json
import logging

from flask import Flask, request


logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route('/')
def hello():
    return 'works!'


@app.route('/cloudbuild_notify', methods=['POST'])
def receive_messages_handler():
    envelope = json.loads(request.data.decode('utf-8'))
    payload = base64.b64decode(envelope['message']['data'])
    payload_json = payload.decode('utf8').replace("'", '"')
    msn_data = json.loads(payload_json)
    logging.info(msn_data)

    status = msn_data['status']

    if status == 'SUCCESS':
        # TODO; send message
        logging.info('deployment is SUCCESS')

    elif status == 'FAILURE':
        # TODO; send message
        logging.info('deployment is FAILURE')

    elif status == 'WORKING':
        logging.info('deployment is WORKING')

    elif status == 'QUEUED':
        logging.info('deployment is QUEUED')

    return 'OK', 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
