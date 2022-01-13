import os
import discord
import requests
import json

discordToken = os.environ['TOKEN']
yoMammaEndpoint =  "http://jokes.guyliangilsing.me/retrieveJokes.php?type=yomama"
chuckNorrisEndpoint = "http://jokes.guyliangilsing.me/retrieveJokes.php?type=chucknorris"
dadJokeEndpoint = "http://jokes.guyliangilsing.me/retrieveJokes.php?type=dadjoke"
randomJokeEndpoint = "http://jokes.guyliangilsing.me/retrieveJokes.php?type=random"

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.content)
    if message.content.lower().startswith('!yomomma'):
        try:
          response = requests.get(yoMammaEndpoint)
          textJSON = json.loads(response.text)
          if (response.status_code == 200):
            await message.channel.send(textJSON["joke"])
          else:
            await message.channel.send("Bad Status from API " + str(response.status_code))
        except Exception:
            await message.channel.send("That sign wasn't found, please try again.")
    elif message.content.lower().startswith('!chucknorris'):
        try:
          response = requests.get(chuckNorrisEndpoint)
          textJSON = json.loads(response.text)
          if (response.status_code == 200):
            await message.channel.send(textJSON["joke"])
          else:
            await message.channel.send("Bad Status from API " + str(response.status_code))
        except Exception:
            await message.channel.send("That sign wasn't found, please try again.")
    elif message.content.lower().startswith('!dadjoke'):
        try:
          response = requests.get(dadJokeEndpoint)
          textJSON = json.loads(response.text)
          if (response.status_code == 200):
            await message.channel.send(textJSON["joke"])
          else:
            await message.channel.send("Bad Status from API " + str(response.status_code))
        except Exception:
            await message.channel.send("That sign wasn't found, please try again.")
    elif message.content.lower().startswith('!joke'):
        try:
          response = requests.get(randomJokeEndpoint)
          textJSON = json.loads(response.text)
          if (response.status_code == 200):
            await message.channel.send(textJSON["joke"])
          else:
            await message.channel.send("Bad Status from API " + str(response.status_code))
        except Exception:
            await message.channel.send("That sign wasn't found, please try again.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

try:
  client.run(discordToken)
# HTTPException  
except Exception:
  print("Rate limited")