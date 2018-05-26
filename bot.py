import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from pprint import pprint as p
from explore import begin_exploration, has_begun_exploring, has_chosen_starter
from secrets import key
from pymongo import MongoClient

mongoClient = MongoClient('localhost', 27017)
bot = Bot(command_prefix='`')

@bot.event
async def on_ready():
    print("on ready has been called")
    print(bot.user.id)
    db = mongoClient.get_database("poke-adventures")
    pdb = db["users"]
    pdb.insert_one({"userId": bot.user.id, "currentPokemon": []})
    begin_exploration("")

@bot.command(pass_context=True)
async def ping(context):
    await bot.say("I'm here")

@bot.command(pass_context=True)
async def hello(context, user: discord.Member):
    p(dir(user))
    p(user.server)
    if user is not None:
        await bot.say("hello there " + user.display_name)
    else:
        await bot.say("Hi, you need to say `hello @username")

@bot.command(pass_context=True, pass_server=True)
async def bans(context):
    p(dir(context))
    p(dir(context.message))
    p(context.message.content)

@bot.command(pass_context=True)
async def explore(context):

    user_mention_text = f"<@{context.message.author.id}>"

    if has_begun_exploring(context.message.author.id):
        await bot.say(f"{user_mention_text}, you've already begun exploring")
    
    else:
        await bot.say(f"Here begins your journey {user_mention_text}.")

        if not has_chosen_starter(context.message.author.id):
            await bot.say(f"You've not chosen your start pokemon yet. Please, choose one below.")
        
        
bot.run(key)