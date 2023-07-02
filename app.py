from flask import Flask, request, send_from_directory
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['secret_key'] = 'change_me'
socket = SocketIO(app)


@app.route('/')
def root():
    return send_from_directory('static', 'index.html')

# serve static generated files
@app.route('/assets/<file_name>', methods=['GET'])
def static_handler(file_name):
    return send_from_directory('static/assets', file_name)

@socket.on('message')
def message_handler(message):
    return f'recieved message {message}'

@socket.on('json')
def json_handler(json):
    return f'recieved json {json}'

@socket.on('connection')
def connection_handler(connection):
    return emit('message', 'Hello There')

@socket.on_error_default
def default_error_handler(e):
    print(request.event["message"]) # "my error event"
    print(request.event["args"])    # (data,)

if(__name__ == "__main__"):
    socket.run(app, port=3000, debug=True)