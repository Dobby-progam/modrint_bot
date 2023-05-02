import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests
import json

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
    embed = discord.Embed(title="Search", timestamp=discord.utils.utcnow(),
                          colour=0x206694,)
    url = (f'{search_url}{text}')
    result = requests.get(url)
    hit = result.json()
    data = json.loads(hit)
    for hit in data["hits"]:
        project_id = hit["project_id"]
        project_type = hit["project_type"]
        slug = hit["slug"]
        author = hit["author"]
        title = hit["title"]
        description = hit["description"]
        categories = hit["categories"]
        display_categories = hit["display_categories"]
        versions = hit["versions"]
        downloads = hit["downloads"]
        follows = hit["follows"]
        icon_url = hit["icon_url"]
        date_created = hit["date_created"]
        date_modified = hit["date_modified"]
        latest_version = hit["latest_version"]
        license = hit["license"]
        client_side = hit["client_side"]
        server_side = hit["server_side"]
        gallery = hit["gallery"]
        featured_gallery = hit["featured_gallery"]
        color = hit["color"]







    print(result,  url, hit)

    embed.add_field(name='resuld', value=hit)
    await ctx.send(embed=embed)

bot.run(os.getenv('TOLKEN'))
