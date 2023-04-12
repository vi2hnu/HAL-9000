import discord
import openai


token = 'MTA5NTM0MjIxMjYwNDI0ODA5NA.GSmVKZ.aSscPXclQoPKSi1hN_4EXVxW__7oKmzHsOTTjI'
openai.api_key = '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'


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
       elif prompt[0:4] == "!rem":
            pass

client.run(token)