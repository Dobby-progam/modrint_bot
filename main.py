import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests

load_dotenv()

search_url = 'https://api.modrinth.com/v2/search?limit=1&query='
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(debug_guilds=[955135608228024394], command_prefix="-", status=discord.Status.dnd,
                   activity=discord.Activity(type=discord.ActivityType.listening, name="mod time!"),
                   owner='820255805257023498', intents=intents, )
bot = discord.Bot()


@bot.listen()
async def on_ready():
    embed = discord.Embed(title=":green_circle: Online!\nNice modding!", timestamp=discord.utils.utcnow(),
                          colour=0x00f00, )
    await bot.get_guild(955135608228024394).get_channel(1011649871511572500).send(embed=embed)
    print("Now ready!")


@bot.command()
async def test(ctx):
    await ctx.respond("works")
    print("send command 'test!'")


@bot.command()
async def search(ctx, text:str):
    url = (f'{search_url}{text}')
    result = requests.get(url)
    hit = result.json()
    print(result,  url, hit)
    embed = discord.Embed(title="Search", timestamp=discord.utils.utcnow(),
                          colour=0x206694,)
    embed.add_field(name='resuld', value=hit)
    await ctx.send(embed=embed)

bot.run(os.getenv('TOLKEN'))
