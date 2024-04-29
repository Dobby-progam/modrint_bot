import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

search_url = 'https://api.modrinth.com/v2/search?limit=2&query='
version_url = 'https://api.modrinth.com/v2/project//version'
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
    await bot.get_guild(955135608228024394).get_channel(1104138752529551480).send(embed=embed)
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
async def search_project(ctx, text:str):
    print('new request')
    print("--"*50)
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

        if client_side =='none'or 'unsupported':
            client= ':negative_squared_cross_mark:'
        else:
            client= ':white_check_mark:'

        if server_side =='none'or 'unsupported':
            server= ':negative_squared_cross_mark:'
        else:
            server= ':white_check_mark:'

        print(result, url, )
        print(project_id, project_type,slug,author,title,description, downloads,
              follows, icon_url, date_created, date_modified, latest_version, license, client_side,server_side,featured_gallery,color)

        print('next thing \n')
        print("*-*" * 50)

        embed = discord.Embed(title="result", timestamp=discord.utils.utcnow(),)
        embed.set_thumbnail(url=icon_url)

        embed.add_field(name='project ID:', value=project_id)
        embed.add_field(name='project type', value=project_type)
        embed.add_field(name='latest version', value=latest_version)
        embed.add_field(name='slug', value=slug)
        embed.add_field(name='author', value=author)
        embed.add_field(name='title', value=title)
        embed.add_field(name='description', value=description)
        embed.add_field(name='downloads', value=downloads)
        embed.add_field(name='follows', value=follows)
        embed.add_field(name='icon imgae', value=icon_url)
        embed.add_field(name='date created', value=date_created)
        embed.add_field(name='date modifiy', value=date_modified)
        embed.add_field(name='latest version', value=latest_version)
        embed.add_field(name='license', value=license)
        embed.add_field(name='client side?', value=client)
        embed.add_field(name='server side?', value=server)
        if featured_gallery is not None:
            embed.set_image(url=featured_gallery)
        else:
            print(' no featured gallery')

        await ctx.respond(embed=embed)
        print("sending next embed")
    print('end message')


@bot.command() 
async def versionlookup(ctx, versionid: str):
    print('new request')
    print("--"*50)

    response = requests.get(f'https://api.modrinth.com/v2/version/{versionid}')
    data = response.json()

    game_versions = ', '.join(data["game_versions"])
    loaders = ', '.join(data["loaders"])
    dependencies = ', '.join([f'{dep["project_id"]}: {dep["dependency_type"]}' for dep in data["dependencies"]])
    changelog = data["changelog"].replace('\r\n', ' ')
    print(dependencies)
    embed = discord.Embed(title="result", timestamp=discord.utils.utcnow(),)
    embed.add_field(name='Game ID:', value=data["name"])
    embed.add_field(name='name', value=data["name"])
    embed.add_field(name='date published', value=data["date_published"])
    embed.add_field(name='version type', value=data["version_type"])
    embed.add_field(name='game versions', value=game_versions)
    embed.add_field(name='loaders', value=loaders)
    embed.add_field(name='dependencies', value=dependencies)
    embed.add_field(name='changelog', value=changelog) 

    await ctx.respond(embed=embed)

bot.run(os.getenv('TOLKEN'))
