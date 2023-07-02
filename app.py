from flask import Flask, request, send_from_directory
from flask_socketio import SocketIO, send, emit
from lib.Storage import Storage
from os import path

app = Flask(__name__)
app.config['secret_key'] = 'change_me'
socket = SocketIO(app)

ROOT_DIR = path.dirname(path.abspath(__file__))
projectRoot = path.join(ROOT_DIR)
storagePath = f'{projectRoot}/data'


messages = Storage(dir=storagePath, entity='messages')
users = Storage(dir=storagePath, entity='users')

@app.route('/')
def root():
    return send_from_directory('static', 'index.html')

# serve static generated files
@app.route('/assets/<file_name>', methods=['GET'])
def static_handler(file_name):
    return send_from_directory('static/assets', file_name)

@socket.on('message')
def message_handler(message):
    return emit('message', f'recieved {message}')



@socket.on('connection')
def connection_handler(connection):
    return emit('message', 'Hello There')

@socket.on_error_default
def default_error_handler(e):
    print(request.event["message"]) # "my error event"
    print(request.event["args"])    # (data,)

if(__name__ == "__main__"):
    socket.run(app, port=3000, debug=True)