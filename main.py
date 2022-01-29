import discord
import os
#import random
#from replit import db
#from collections import OrderedDict
from keep_alive import keep_alive

client=discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  #Global varible for the message.channel
  global msgchan
  msgchan = message.channel 

  if message.author == client.user:
    return
  msg = message.content



keep_alive()
client.run(os.environ['token'])


