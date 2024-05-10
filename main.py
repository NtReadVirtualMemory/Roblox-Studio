import discord
from discord.ext import commands
from flask import Flask, request, jsonify
from threading import Thread
import os
import time

app = Flask(__name__)
message_text = "return"

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

intents = discord.Intents.default()
intents.messages = True 
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def execute(ctx, *, new_message):
    global message_text
    message_text = new_message
    await ctx.send('Executing...')
    time.sleep(1)
    message_text = "return"

keep_alive()


try:
    bot.run(os.environ.get("token"))
except Exception as e:
    print(f"Error starting bot: {e}")
