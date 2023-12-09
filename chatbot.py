import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def helpme(ctx):
    await ctx.send(f'Ecco la lista dei comandi:(metti sempre davanti il prefisso $)')
    await ctx.send(f'ciao, che ti permette di essere salutato')
    await ctx.send(f'flip_coin, che ti permette di lanciare una moneta')
    await ctx.send(f'heh, che va scritto assieme a quante volte lo si vuole ripetere')
    await ctx.send(f'add, che va scritto assieme ai numeri che si vuole sommare')
    await ctx.send(f'roll, che va scritto prima quanti dadi vogliamo lanciare poi d e poi di quanto deve essere il dado. Es: 1d6')
    await ctx.send(f'choose, che va scritto insieme ad altre parole ed il bot ne sceglierà una a caso')
    await ctx.send(f'repeat, che va scritto prima il numero di quante volte si vuole ripetere una parola e poi la parola')
    await ctx.send(f'gen_meme, invia un meme causale')
    await ctx.send(f'meme_basic, invia un meme causale tra alcuni predefiniti')
    await ctx.send(f'meme_byme, invia un meme causale tra alcuni creati da me')
    await ctx.send(f'meme_web, invia un meme casuale tra alcuni presi dal web')

@bot.command()
async def flip_coin(ctx):
    flip = random.randint(0, 2)
    if flip == 0:
        await ctx.send (f"HEADS")
    else:
        await ctx.send(f"TAILS")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def gen_meme(ctx, name=None):
    folder = "images"
    memes = os.listdir(folder)
    
    if name is None or name not in memes:
        name = random.choice(memes)

    with open(f'{folder}/{name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def meme_basic(ctx, name_b=None):
    folder_b= "images_basic"
    memes_b = os.listdir(folder_b)
    if name_b is None or name_b not in memes_b:
        name_b = random.choice(memes_b)
    with open(f'{folder_b}/{name_b}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def meme_byme(ctx, name_m=None):
    folder_m= "images_me"
    memes_m = os.listdir(folder_m)
    if name_m is None or name_m not in memes_m:
        name_m = random.choice(memes_m)
    with open(f'{folder_m}/{name_m}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def meme_web(ctx, name_w=None):
    folder_w= "images_web"
    memes_w = os.listdir(folder_w)
    if name_w is None or name_w not in memes_w:
        name_w = random.choice(memes_w)
    with open(f'{folder_w}/{name_w}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


bot.run("MTE3NTM4MTY3ODM4MjkxNTYwNA.GOsbxr.-YOThCJW9FBbh9_DUHPckljkOpiJjwwGD74C6o")
