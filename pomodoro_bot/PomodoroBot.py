import os

from discord.ext import commands
from dotenv import load_dotenv
from timer import PomodoroTimer

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

session = PomodoroTimer(25)

bot = commands.Bot(command_prefix="!")


@bot.command(name="SetTimer", help="Sets Pomodoro timer in minutes")
async def SetTimer(ctx, inputTime):
    session.setWorkTimer(int(inputTime))
    await ctx.send("Pomodoro timer has been set for " + inputTime + " minutes")


@bot.command(name="SetBreak", help="Set break timer in minutes for pomodoro session")
async def SetBreak(ctx, inputTime):
    session.setBreakTimer(int(inputTime))
    await ctx.send("You've set a break time for " + inputTime + " minutes :smiley:")


@bot.command(name="StartTimer", help="Starts the pomodoro timer")
async def StartTimer(ctx):
    message = session.startWorkTimer()
    await ctx.send(message)
    message = session.startBreakTimer()
    await ctx.send(message)


bot.run(TOKEN)
