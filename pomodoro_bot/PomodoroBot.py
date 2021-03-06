import os

from dotenv import load_dotenv
from discord.ext import commands

import vardata
from threading_time import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

pomodoro_thread = FuncThread("Pomodoro Thread")
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
	channel = bot.get_channel(778923727517515788)
	await channel.send("Hi everyone! I'm Pomodoro Bot!")
	print(f"{bot.user} is connected to the Discord!")
	


@bot.command(name="setTimer", help="Sets Pomodoro timer in minutes")
@commands.has_role('Admin')
async def SetTimer(ctx, inputTime):
	if int(inputTime) >= 0 and int(inputTime) <= 40:
		pomodoro_thread.setProductivityTime(int(inputTime))
		await ctx.send("Pomodoro timer has been set for " + inputTime + " minutes")
	else:
		await ctx.send("Invalid time value! :sob:")


@bot.command(name="setBreak", help="Set break timer in minutes for pomodoro session")
@commands.has_role('Admin')
async def SetBreak(ctx, inputTime):
	if int(inputTime) >= 0 and int(inputTime) <= 10:
		pomodoro_thread.setBreakTime(int(inputTime))
		await ctx.send("You've set a break time for " + inputTime + " minutes :smiley:")
	else:
		await ctx.send("Invalid time value! :sob:")

@bot.command(name="setPomo", help="Enter productivity and break session times with a space between")
@commands.has_role('Admin')
async def setPomo(ctx, inputWork, inputBreak):
	if int(inputWork) >= 0 and int(inputBreak) >= 0 and int(inputWork) <= 40 and int(inputBreak) <= 10:
		pomodoro_thread.setProductivityTime(int(inputWork))
		pomodoro_thread.setBreakTime(int(inputBreak))
	else:
		await ctx.send("Invalid inputs given.")

@bot.command(name="check", help="Check the times set for pomodoro sessions")
async def Check(ctx):
	working_time = str(int(pomodoro_thread.productivity / 60))
	break_time = str(int(pomodoro_thread.breakSession / 60))
	await ctx.send("Productivity Time: " + working_time + " minutes \n" + "Break Time: " + break_time + " minutes")

@bot.command(name="start", help="Starts the pomodoro timer")
@commands.has_role('Admin')
async def runTimer(ctx):
	pomodoro_thread.start()
	await ctx.send("Starting Productivity Session :smiley:")
	#message = pomodoro_thread.runProductivity()
	#await ctx.send(message)
	#await ctx.send("Starting well-deserved break session!")
	#message = pomodoro_thread.runBreak()
	#await ctx.send(message)

@bot.command(name="stop", help="Stops the current timer.")
async def stopTimer(ctx):
	vardata.exit_flag = True
	await ctx.send("Timer has been stopped")


@bot.command(name="exit", help="Logs pomodoro bot out of discord")
@commands.has_role('Admin')
async def botExit(ctx):
	await ctx.send("Farewell, everyone! :hugging: :hugging_face:")
	await bot.close()

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CheckFailure):
		await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)