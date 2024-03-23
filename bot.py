import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

def joke():
  response = requests.get('https://official-joke-api.appspot.com/random_joke')
  json_data = json.loads(response.text)
  delivery = json_data['setup'] +' '+ json_data['punchline']
  return delivery

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())

    if message.content.startswith('$joke'):
      await message.channel.send(joke())


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')
