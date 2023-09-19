import discord
import os
import random as rand


#For bots to interactable with channel
intents = discord.Intents.default()
intents.message_content = True
#Setting Up
client = discord.Client(intents= intents)
token = os.environ['DISCORD_TOKEN']

#My main function
def CoinToss():
  result = rand.randint(0,1)
  if result == 0:
    return 'Head'
  else:
    return 'Tail'


def d(val):
  
  result = rand.randint(1,int(val))
  return(int(result))
  


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
      
#My Bots Functionality  
  if msg.startswith('/Toss'):
    outcome = CoinToss()
    await message.channel.send(outcome)
    
  if msg.startswith('/MultiToss'):
    number = int(msg.split('/MultiToss',1)[1])
    for x in range(number):
      result = CoinToss()
      outcome = "Number of coin: "+str(x+1) + " "+ result
      await message.channel.send(outcome)

  if msg.startswith('/D'):
    try:
      val = msg.split('/D',1)[1]
      if len(val) ==1:
        number = 1
        face = int(val)
      else:
        face, number = val.split()
        number = int(number)
    except:
      face = 6
      number = 1
    if number <= 0:
      number = 1
    await message.channel.send(f"You choose to roll {number} {face}-faces dice! The result will appear shortly")
    for x in range(int(number)):
      result = d(int(face))
      outcome ="Dice #"+str(x+1)+": "+ str(result)
      await message.channel.send(outcome)
      
client.run(token)

