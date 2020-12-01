import os

from timer import PomodoroTimer, BotTime

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

session = PomodoroTimer()
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user} is connected to the Discord!")


@bot.command(name="SetTimer", help="Sets Pomodoro timer in minutes")
@commands.has_role('Admin')
async def SetTimer(ctx, inputTime):
	if int(inputTime) >= 0 and int(inputTime) <= 40:
	    session.setWorkTimer(int(inputTime))
	    await ctx.send("Pomodoro timer has been set for " + inputTime + " minutes")
	    timeout_session.resetTimer()
	else:
		await ctx.send("Invalid time value! :sob:")


@bot.command(name="SetBreak", help="Set break timer in minutes for pomodoro session")
@commands.has_role('Admin')
async def SetBreak(ctx, inputTime):
    session.setBreakTimer(int(inputTime))
    if int(inputTime) >= 0 and int(inputTime) <= 10:
	    await ctx.send("You've set a break time for " + inputTime + " minutes :smiley:")
	    timeout_session.resetTimer()
	else:
		await ctx.send("Invalid time value! :sob:")

@bot.command(name="Check", help="Check the times set for pomodoro sessions")
async def Check(ctx):
    working_time = str(int(session.time / 60))
    break_time = str(int(session.breakTime / 60))
    await ctx.send("Productivity Time: " + working_time + "minutes \n" + "Break Time: " + break_time + " minutes")

@bot.command(name="StartTimer", help="Starts the pomodoro timer")
@commands.has_role('Admin')
async def StartTimer(ctx):
    message = session.startWorkTimer()
    await ctx.send(message)
    message = session.startBreakTimer()
    await ctx.send(message)
    timeout_session.resetTimer()


@bot.command(name="exit", help="Logs pomodoro bot out of discord")
@commands.has_role('Admin')
async def botExit(ctx):
    await ctx.send("Farewell, everyone! :hugging: :hugging_face:")
    await bot.close()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

#if timeout_session.timeout == -1:
#    bot.close()
#else:
#    bot.run(TOKEN)

bot.run(TOKEN)
