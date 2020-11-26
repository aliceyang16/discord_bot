import os

from timer import PomodoroTimer, BotTime

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

session = PomodoroTimer()
timeout_session = BotTime()

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user} is connected to the Discord!")


@bot.command(name="SetTimer", help="Sets Pomodoro timer in minutes")
async def SetTimer(ctx, inputTime):
    session.setWorkTimer(int(inputTime))
    await ctx.send("Pomodoro timer has been set for " + inputTime + " minutes")
    timeout_session.resetTimer()


@bot.command(name="SetBreak", help="Set break timer in minutes for pomodoro session")
async def SetBreak(ctx, inputTime):
    session.setBreakTimer(int(inputTime))
    await ctx.send("You've set a break time for " + inputTime + " minutes :smiley:")
    timeout_session.resetTimer()


@bot.command(name="StartTimer", help="Starts the pomodoro timer")
async def StartTimer(ctx):
    message = session.startWorkTimer()
    await ctx.send(message)
    message = session.startBreakTimer()
    await ctx.send(message)
    timeout_session.resetTimer()


@bot.command(name="exit", help="Logs pomodoro bot out of discord")
async def botExit(ctx):
    await ctx.send("Farewell, everyone! :hugging: :hugging_face:")
    await bot.close()


timeout_session.countDown()

if timeout_session.timeout == -1:
    bot.close()
else:
    bot.run(TOKEN)
