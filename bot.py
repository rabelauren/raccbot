from discord.ext import commands
import random
import requests
client = commands.Bot(command_prefix="racc ", case_insensitive=True)

with open("bot_key.txt", "r") as file:
     botKey = file.read()
     
with open("nasa_key.txt", "r") as file:
     nasaKey = file.read()

@client.command()
async def test(ctx): 
    await ctx.send("racc test")

@client.command()
async def meme(ctx): 
    # open txt file
    with open("raccbotlinks.txt", "r") as file:
        raccLinks = file.read()
    
    # splits string into list
    memeList = raccLinks.splitlines()
    
    await ctx.send(random.choice(memeList))

@client.command()
async def bored(ctx):
    async with ctx.typing():
        response = requests.get("https://www.boredapi.com/api/activity").json()
        await ctx.send((response["activity"]).lower() + "!")
        
@client.command()
async def apod(ctx):
    async with ctx.typing():
        response = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + nasaKey).json()
        await ctx.send("**" + response["title"] + "**: " + response["date"])
        await ctx.send(response["hdurl"])
        await ctx.send("||" + response["explanation"] + "||")


     
client.run(botKey)