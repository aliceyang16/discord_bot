import os
import discord
import random

from timer import PomodoroTimer 

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

session = PomodoroTimer(25)

bot = commands.Bot(command_prefix='!')

@bot.command(name='SetTimer', help='Sets Pomodoro timer in minutes')
async def SetTimer(ctx, inputTime):
	session.setTimer(int(inputTime))
	await ctx.send('Pomodoro timer has been set for ' + inputTime + ' minutes')

@bot.command(name='StartTimer', help='Starts the pomodoro timer')
async def StartTimer(ctx):
	message = session.startTimer()
	await ctx.send(message)

bot.run(TOKEN)