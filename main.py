from flask import Flask, request, jsonify
from threading import Thread

app = Flask(__name__)
message_text = "Bot: Online!"

@app.route('/')
def index():
    return message_text

@app.route('/set_message', methods=['POST'])
def set_message():
    global message_text
    new_message = request.json.get('message')
    if new_message:
        message_text = new_message
        return jsonify({'success': True, 'message': 'Message updated successfully'})
    else:
        return jsonify({'success': False, 'message': 'No message provided'})

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
