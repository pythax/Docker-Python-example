import discord
import requests


client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="getting tested on", url="Please get me out of this container! | Hosted @ pythaxprivate.net"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    r = requests.get("https://pythaxprivate.net").status_code
    if message.content.startswith('Wyd') or message.content.startswith('wyd') or message.content.startswith('WYD')  :
        await message.channel.send(' Yes yes im here {}, Im containered, come free me.'.format(r))

client.run('')