import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

search_url = 'https://api.modrinth.com/v2/search?limit=2&query='
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

#store some code

    #import json
    #data = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
    #print(data['two'])  # or `print data['two']` in Python 2
    #embed.add_field(name='resuld', value=hit)
    #

@bot.command()
async def search(ctx, text:str):
    url = f'{search_url}{text}'
    result = requests.get(url)
    hit = result.json()

    for hit in hit["hits"]:
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
        color = hex(hit["color"])
        print(project_id, project_type,slug,author,title,description, downloads,
              follows, icon_url, date_created, date_modified, latest_version, license, client_side,server_side,featured_gallery,color)
        print(result,  url,)
        print('next thing \n')
        embed = discord.Embed(title="result", timestamp=discord.utils.utcnow(),
                             colour=hex(hit["color"]),)
        embed.add_field(name='project ID:', value=project_id)
        embed.add_field(name='project type', value=project_type)
        embed.add_field(name='latest version', value=latest_version)
        embed.add_field(name='resuld', value=hit)
        embed.add_field(name='resuld', value=hit)
        embed.add_field(name='resuld', value=hit)
        embed.add_field(name='resuld', value=hit)



    await ctx.send(embed=embed)



bot.run(os.getenv('TOLKEN'))
