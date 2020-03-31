import os
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SEC']
socketio = SocketIO(app)

@socketio.on('json', namespace='')
def broadcastPoint(message):
    emit('json', message, broadcast=True)

@app.route('/')
def hello():
    agent = request.headers.get('User-Agent')
    if 'iphone' in agent.lower():
            return render_template('ios.html')
    return render_template('index.html')

@app.route('/favicon.ico')
def nof():
    return ''
