from discord.ext import commands
from discord.ext import menus
import discord
import random
import asyncio
import aiohttp
import json

hid = 666317117154525185

async def req(a=0):
	async with aiohttp.ClientSession() as session:
		if a != 0 and a != 1 and a != 2 and a != 3:
			a = 0
		if a == 0:
			url = "URL1"
		if a == 1:
			url = "URL2"
		if a == 2:
			url = "URL3"
		if a == 3:
			url = "URL4"
		async with session.get(url, headers={'auth': 'PASSWORD'}) as resp:
			txt = await resp.text()
			return json.loads(txt)

def cen(ip):
	ip = ip.split(".")
	for n in [1,2]:
		for i in range(0,10):
			ip[n] = ip[n].replace(str(i),'x')
	ip = '.'.join(ip)
	return ip

class MySource(menus.ListPageSource):
	def __init__(self, data, json):
		super().__init__(data, per_page=1)
		max = 9
		if json['sys']['sys']['node'] == 'justh':
			self._max_pages = max
		if json['sys']['sys']['node'] != 'justh':
			self._max_pages = max-1
		self.json = json

	async def format_page(self, menu, entries):
		dat = self.json
		if menu.current_page == 0:
			zer = dat['sys']['sys']
			msg = discord.Embed(title="System Info",description=f"**{zer['node']}**\n*page {menu.current_page+1}/{self.get_max_pages()}*",color=eval(f"0x{client.info['color']}"))
			msg.set_thumbnail(url=f"{client.info['avatar']}")
			msg.set_footer(text=f'created by @{client.get_user(hid)} <{hid}>', icon_url=client.get_user(hid).avatar_url)
			msg.add_field(name='OS',value=f"{zer['os']}",inline=False)
			msg.add_field(name='Node',value=f"{zer['node']}",inline=False)
			msg.add_field(name='Release',value=f"{zer['release']}",inline=False)
			msg.add_field(name='Version',value=f"{zer['ver']}",inline=False)
			msg.add_field(name='Architecture',value=f"{zer['arch']}",inline=False)
			msg.add_field(name='Boot Time',value=f"{zer['start']}",inline=False)
			return msg
		if menu.current_page == 1:
			zer = dat['sys']['cpu']
			msg = discord.Embed(title="Cpu Info",description=f"**{dat['sys']['sys']['node']}**\n*page {menu.current_page+1}/{self.get_max_pages()}*",color=eval(f"0x{client.info['color']}"))
			msg.set_thumbnail(url=f"{client.info['avatar']}")
			msg.set_footer(text=f'created by @{client.get_user(hid)} <{hid}>', icon_url=client.get_user(hid).avatar_url)
			msg.add_field(name='Current Frequency',value=f"{zer['curfreq']}",inline=False)
			msg.add_field(name='Number of Physical Cores',value=f"{zer['phys']}",inline=False)
			msg.add_field(name='Number of Toal Cores',value=f"{zer['total']}",inline=False)
			msg.add_field(name='Percent Used',value=f"{zer['use']}",inline=False)
			return msg
		if menu.current_page == 2:
			zer = dat['sys']['mem']
			msg = discord.Embed(title="Memory Info",description=f"**{dat['sys']['sys']['node']}**\n*page {menu.current_page+1}/{self.get_max_pages()}*",color=eval(f"0x{client.info['color']}"))
			msg.set_thumbnail(url=f"{client.info['avatar']}")
			msg.set_footer(text=f'created by @{client.get_user(hid)} <{hid}>', icon_url=client.get_user(hid).avatar_url)
			msg.add_field(name='Total Storage',value=f"{zer['total']}",inline=False)
			msg.add_field(name='Avaliable Storage',value=f"{zer['avaliable']}",inline=False)
			msg.add_field(name='Used Storage',value=f"{zer['used']}",inline=False)
			msg.add_field(name='Percent Free',value=f"{zer['percnt']}",inline=False)
			return msg
		if menu.current_page == 3:
			zer = dat['sys']['mem']['swap']
			msg = discord.Embed(title="Swap Info",description=f"**{dat['sys']['sys']['node']}**\n*page {menu.current_page+1}/{self.get_max_pages()}*",color=eval(f"0x{client.info['color']}"))
			msg.set_thumbnail(url=f"{client.info['avatar']}")
			msg.set_footer(text=f'created by @{client.get_user(hid)} <{hid}>', icon_url=client.get_user(hid).avatar_url)
			msg.add_field(name='Total Space',value=f"{zer['total']}",inline=False)
			msg.add_field(name='Free Space',value=f"{zer['free']}",inline=False)
			msg.add_field(name='Used Space',value=f"{zer['used']}",inline=False)
			msg.add_field(name='Percent Used',value=f"{zer['percnt']}",inline=False)
			return msg
		if menu.current_page == 4:
			zer = dat['sys']['net']
			msg = discord.Embed(title="Network Info",description=f"**{dat['sys']['sys']['node']}**\n*page {menu.current_page+1}/{self.get_max_pages()}*",color=eval(f"0x{client.info['color']}"))
			msg.set_thumbnail(url=f"{client.info['avatar']}")
			msg.set_footer(text=f'created by @{client.get_user(hid)} <{hid}>', icon_url=client.get_user(hid).avatar_url)
			msg.add_field(name='Interface Name',value=f"{zer['name']}",inline=False)
			msg.add_field(name='IP',value=f"{cen(zer['ip'])}",inline=False)
			msg.add_field(name='NetMask',value=f"{zer['mask']}",inline=False)
			msg.add_field(name='Broadcast IP',value=f"{cen(zer['bip'])}",inline=False)
			return msg
		if menu.current_page == 5:
			zer = dat['sys']['io']
			msg = discord.Embed(title="I/O Info",description=f"**{dat['sys']['sys']['node']}**\n*page {menu.current_page+1}/{self.get_max_pages()}*",color=eval(f"0x{client.info['color']}"))
			msg.set_thumbnail(url=f"{client.info['avatar']}")
			msg.set_footer(text=f'created by @{client.get_user(hid)} <{hid}>', icon_url=client.get_user(hid).avatar_url)
			msg.add_field(name='Sent',value=f"{zer['sent']}",inline=False)
			msg.add_field(name='Recived',value=f"{zer['rcved']}",inline=False)
			return msg
		if menu.current_page == 6:
			zer = dat['py']
			msg = discord.Embed(title="Python Info",description=f"**{dat['sys']['sys']['node']}**\n*page {menu.current_page+1}/{self.get_max_pages()}*",color=eval(f"0x{client.info['color']}"))
			msg.set_thumbnail(url=f"{client.info['avatar']}")
			msg.set_footer(text=f'created by @{client.get_user(hid)} <{hid}>', icon_url=client.get_user(hid).avatar_url)
			msg.add_field(name='Version',value=f"{zer['ver']}",inline=False)
			msg.add_field(name='Version info',value=f"```py\n{zer['verinf']}```",inline=False)
			return msg
		if menu.current_page == 7:
			zer = dat['other-versions']
			if dat['sys']['sys']['node'] == 'justh':
				msg = discord.Embed(title="Other Version Info",description=f"**{dat['sys']['sys']['node']}**\n*page {menu.current_page+1}/{self.get_max_pages()}*",color=eval(f"0x{client.info['color']}"))
				msg.set_thumbnail(url=f"{client.info['avatar']}")
				msg.set_footer(text=f'created by @{client.get_user(hid)} <{hid}>', icon_url=client.get_user(hid).avatar_url)
				msg.add_field(name='Ruby',value=f"{zer['ruby']}",inline=True)
				msg.add_field(name='Julia',value=f"{zer['julia']}",inline=True)
				msg.add_field(name='PHP',value=f"{zer['php']}",inline=True)
				msg.add_field(name='GoLang',value=f"{zer['go']}",inline=True)
				msg.add_field(name='JavaScript',value=f"{zer['js']}",inline=True)
				msg.add_field(name='Lua',value=f"{zer['lua']}",inline=True)
				msg.add_field(name='Rust',value=f"{zer['rust']}",inline=True)
				msg.add_field(name='Crystal',value=f"{zer['crystal']}",inline=True)
				msg.add_field(name='Dart',value=f"{zer['dart']}",inline=True)
				msg.add_field(name='Elixir',value=f"{zer['elixir']}",inline=True)
				msg.add_field(name='Nginx',value=f"{zer['nginx']}",inline=True)
				msg.add_field(name='Docker',value=f"{zer['docker']}",inline=True)
				msg.add_field(name='Docker Compose',value=f"{zer['docker-compose']}",inline=True)
				msg.add_field(name='Apt',value=f"{zer['apt']}",inline=True)
				msg.add_field(name='Nano',value=f"{zer['nano']}",inline=True)
			if dat['sys']['sys']['node'] != 'justh':
				msg = discord.Embed(title="Other Version Info",description=f"**{dat['sys']['sys']['node']}**\n*page {menu.current_page+1}/{self.get_max_pages()}*",color=eval(f"0x{client.info['color']}"))
				msg.set_thumbnail(url=f"{client.info['avatar']}")
				msg.set_footer(text=f'created by @{client.get_user(hid)} <{hid}>', icon_url=client.get_user(hid).avatar_url)
				try: zer['apt']
				except KeyError: zer['apt'] = None
				if zer['apt'] is not None:
					msg.add_field(name='Apt',value=f"{zer['apt']}",inline=False)
				try: zer['dnf']
				except KeyError: zer['dnf'] = None
				if zer['dnf'] is not None:
					msg.add_field(name='Dnf',value=f"{zer['dnf']}",inline=False)
				msg.add_field(name='Nginx',value=f"{zer['nginx']}",inline=False)
				msg.add_field(name='Nano',value=f"{zer['nano']}",inline=False)
			return msg
		if menu.current_page == 8:
			zer = dat['other-versions']['dotnet']
			msg = discord.Embed(title=".NET Info",description=f"**{dat['sys']['sys']['node']}**\n*page {menu.current_page+1}/{self.get_max_pages()}*",color=eval(f"0x{client.info['color']}"))
			msg.set_thumbnail(url=f"{client.info['avatar']}")
			msg.set_footer(text=f'created by @{client.get_user(hid)} <{hid}>', icon_url=client.get_user(hid).avatar_url)
			msg.add_field(name='Version',value=f"{zer['ver']}",inline=False)
			msg.add_field(name='Runtimes',value=f"{zer['runtimes']}",inline=False)
			msg.add_field(name='SDKs',value=f"{zer['sdks']}",inline=False)
			return msg
def menuobj(inp):
	a = ['.']
	for i in range(9):
		a.append('.')
	return menus.MenuPages(source=MySource(a, inp), clear_reactions_after=True)

class hreqs(commands.Cog):
	@commands.command()
	async def req(self, ctx):
		if ctx.message.author.id == hid:
			loading = await ctx.message.channel.send(content="loading...")
			arg = ctx.message.content[6:len(ctx.message.content)]
			arg = arg.replace(" ","")
			if arg == "" or arg == "bot" or arg == "bots" or arg == "0":
				resp = await req(0)
			if arg == "chem" or arg == "chemistry" or arg == "computertime" or arg == "1":
				resp = await req(1)
			if arg == "misc" or arg == "cent" or arg == "hmisc" or arg == "2":
				resp = await req(2)
			if arg == "site" or arg == "sites" or arg == "hsites" or arg == "3":
				resp = await req(3)
			pages = menuobj(resp)
			await pages.start(ctx)
			await loading.delete()
		if ctx.message.author.id != hid:
			await ctx.message.channel.send(content=f"only <@!{hid}> can do that!")
def setup(bot):
	bot.add_cog(hreqs())
	global client
	client = bot