import discord
from discord.ext import commands
import compliments
import random

prefix = ('!', '?', '~', '$')
TOKEN = ""
BOT = commands.Bot(command_prefix=prefix)


@BOT.command()
async def info(ctx):
    embed = discord.Embed(title="My-First-Bot", description="A bot to learn python with", color=0xeee657)

    await ctx.send(embed=embed)


#compliment another person
@BOT.command(aliases=["Compliment", "comp"],
             pass_context = True)
async def compliment(ctx, *args):
    message = compliments.comp(*args)
    await ctx.send(message)

@BOT.command(pass_context = False)
async def choose(ctx, *args):
    choice = random.choice(args)
    await ctx.send("Between those, I choose " + choice + ", " + ctx.message.author.mention)

#look up something on amazon

#link to video on youtube

#hangman with individual user. each user plays own game of hangman




@BOT.event
async def on_ready():
    print("Everything's all ready to go~")
    print('Logged in as')
    print(BOT.user.name)
    print(BOT.user.id)
    print('------')

BOT.run(TOKEN)