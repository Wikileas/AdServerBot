#DO NOT CREATE THE JSON BEFOREHAND, JUST RUN THIS FILE ALONE AND IT SHOULD WORK.

import discord
import os
import json
from discord.ext import commands
import asyncio
client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)



@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online)
  os.system('clear')
  print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.command()
async def start(ctx):
    global running
    running = True
    while running:
        with open('messages.json') as f:
            data = json.load(f)
            message = data['message']
            servers = data['servers']
            for server in servers:
                channel_id = server['channel_id']
                slowmode = server['slowmode']
                channel = client.get_channel(int(channel_id))
                await asyncio.sleep(slowmode + 5)
                await channel.send(message)
@client.command()
async def build(ctx, channel_id: int, cooldown: int, message: str):
    try:
        with open('messages.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError: #IF YOU GET JSON DECODER ERROR JUST DELETE YOUR JSON
        data = {}

    data["message"] = message
    if "servers" not in data:
        data["servers"] = []

    data['servers'].append({
        "channel_id": channel_id,
        "slowmode": cooldown
    })

    with open('messages.json', 'w') as f:
        json.dump(data, f, indent=2)

@client.command()
async def stop(ctx):
    global running
    running = False
    await ctx.send("Stopping!")
client.run('MTA3MzM1NDg0MjI3MTEzNzg3Mw.GfsJT3.qguxHyt_oP-ajMnWPjAHDQ-_vENOH37pdKIqiM')
