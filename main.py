from quart import Quart, request, render_template
from telethon import TelegramClient
import os
import asyncio

app = Quart(__name__)

api_id = "" # insert your app_id via telegram
api_hash = "" # insert your app_id via telegram

session_file = 'YOUR_SESSION.session'
if os.path.exists(session_file):
    os.remove(session_file)

loop = asyncio.get_event_loop()

client = TelegramClient('YOUR_SESSION', api_id, api_hash)

@app.before_serving
async def startup():
    await client.start()

@app.route('/')
async def index():
    return await render_template('index.html')

@app.route('/send_message', methods=['POST'])
async def send_message():
    data = await request.form
    message = data['message']

    async with client:
        await client.send_message('@USERNAME', message) # fill in desired username id

    return await render_template('message_sent.html')

if __name__ == '__main__':
    app.run()