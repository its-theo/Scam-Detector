import nextcord as discord
from nextcord.ext import commands
from pyjavaproperties import Properties
p = Properties()
p.load(open('bot.properties'))
TOKEN = p['token']
PREFIX = p['prefix']
scam_detector = commands.Bot(command_prefix=PREFIX, help_command=None)

@scam_detector.event
async def on_message(msg):
  f = open("list.txt", "r")
  if msg.content in f.read():
    member = msg.author
    await member.kick(reason="Sent a scam link")
  else:
    return
  
scam_detector.run(TOKEN)  
