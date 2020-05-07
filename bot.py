import discord
from discord.ext import commands
import random
import json

bot = commands.Bot(command_prefix='&&')
bot.remove_command('help')
hid = 666317117154525185
info=json.load(open('data.json','r+'))
botinf =info['bot']

@bot.event
async def on_ready():
    global startlat
    await bot.change_presence(activity=discord.Game(name='...'), status=discord.Status('dnd'))
    tmplat = str(round(bot.latency*1000,0))
    startlat = f'{tmplat[0:len(tmplat)-2]}ms'
    print(f"ready with lat of {startlat}")
@bot.event
async def on_message(message):
    if message.content.startswith('ping--'):
        msg = discord.Embed(title="Pong",description='*python5*', color=eval(f"0x{botinf['color']}"))
        msg.set_thumbnail(url=f"{botinf['avatar']}")
        msg.set_footer(text=f'created by @{bot.get_user(hid)} <{hid}>', icon_url=bot.get_user(hid).avatar_url)
        tmplat = str(round(bot.latency*1000,0))
        msg.add_field(name='Latency Now',value=f'{tmplat[0:len(tmplat)-2]}ms',inline=False)
        msg.add_field(name='Latency At Startup',value=startlat,inline=False)
        await message.channel.send(embed=msg)
    if message.author.id == hid:
        if message.content.startswith('kyst--') or message.content.startswith('stoppy5--'):
            message.content = '&&jsk shutdown'
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    msg = discord.Embed(title="\U0001f3d3Pong",color=eval(f"0x{botinf['color']}"))
    msg.set_thumbnail(url=f"{botinf['avatar']}")
    msg.set_footer(text=f'created by @{bot.get_user(hid)} <{hid}>', icon_url=bot.get_user(hid).avatar_url)
    tmplat = str(round(bot.latency*1000,0))
    msg.add_field(name='Latency Now',value=f'\U0001f3d3{tmplat[0:len(tmplat)-2]}ms',inline=False)
    msg.add_field(name='Latency At Startup',value='\U0001f3d3'+startlat,inline=False)
    await ctx.message.channel.send(embed=msg)

bot.load_extension('getdat')
bot.load_extension('jishaku')
bot.load_extension('main')
bot.load_extension('reqs')
bot.run('TOKEN')
