import discord
import openai


token = 'token'
openai.api_key = 'openai-token'


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

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
            responce = openai.Completion.create(
                  model = "text-davinci-003",
                  prompt = prompt[3:],
                  max_tokens = 1000,
                  temperature = 0.7
            )
            await message.channel.send(responce["choices"][0]["text"])
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
