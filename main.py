import discord
import random
import os
from colorama import Fore
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
greets = [
  'Hi', 'hello', 'Howdy', 'Wsg', 'Whats up!', 'Hey', "How's it going!?",
  'HueHueHue', 'Merhaba', 'Selam', 'Yo!'
]

goodByes = [
  'Bye', 'See you later', 'Come back soon', 'We will miss you', 'Aloha',
  'Adios', 'Salam', 'GGs Bro'
]

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(Fore.GREEN + '*******Logged in a as {0.user}********'.format(client) +
        Fore.RESET)


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('hello') or message.content.startswith(
      'Hello') or message.content.startswith(
        'Hi') or message.content.startswith('hi'):
    await message.channel.send(message.author.mention + ' ' +
                               random.choice(greets))
  if message.content.endswith('bye') or message.content.endswith('Bye'):
    await message.channel.send(message.author.mention + " " +
                               random.choice(goodByes))



keep_alive()
client.run(os.environ.get("TOKEN")) # ENTER YOUR TOKEN HERE OR USE REPLIT IT HAS IN BUILT SYSTEM TO HANDLE TOKENS 
