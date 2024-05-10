import discord
from discord.ext import commands
from flask import Flask, jsonify
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

# Discord Bot setup
bot = commands.Bot(command_prefix='/')  # You can change the prefix if needed

@bot.command()
async def changesite(ctx, *, new_message):
    global message_text
    message_text = new_message
    await ctx.send('Message updated successfully.')

keep_alive()
bot.run(os.environ.get("token"))
