# I will make an actual file for the api just haven't gotten there yet
# So for now its just a big mess

import requests
import discord
users = len(set(bot.get_all_members()))
servers = len(bot.guilds)
guilds = bot.guilds
channels = len([c for c in bot.get_all_channels()])
r = requests.post('http://localhost:5000/api/v1',data={'key':1234,'servers':servers,'users':users,'channels':channels})
print(r.text)
