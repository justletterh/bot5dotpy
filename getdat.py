import json
def setup(bot):
  with open('data.json', 'r+') as f:
    bot.dat = json.load(f)
    bot.info = bot.dat['bot']
