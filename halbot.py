import discord
from openai import OpenAI
import time

token = 'your_discord_bot_token'
api_key = 'your_openai_api_key'


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)
openai = OpenAI(api_key=api_key)

@client.event
async def on_ready():
        print("bot is online")

@client.event
async def on_message(message):
       if message.author.bot: 
             return
       
       prompt = message.content.lower()
       if prompt == "!hello":
            await message.reply("hello", mention_author=True)
       if prompt[0:3] =="!ai":
            response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "user", "content": prompt}
                ]
            )
            await message.channel.send(response.choices[0].message.content)
       elif prompt == "!help":
             await message.channel.send("1) asking a question to ai use ' !ai ' followed by the question you want to ask\n2) for setting up a reminder use ' !rem ' followed by the amount and unit of time(d-days,h-hours,m-minute,s-seconds) and what you want to be reminded of")
       elif prompt[0:4] == "!rem":
          y = prompt[4:].split()
          
          temp = int(y[0])
          if y[1].lower() == 'd':
             y[0] = temp*86400
          elif y[1].lower() == "h":
             y[0] = temp*3600
          elif y[1].lower() == 'm':
             y[0] = temp*60
          p = " ".join(y[2:])
          time.sleep(int(y[0]))
          await message.reply(p,mention_author=True)
         

client.run(token)
