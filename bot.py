import discord
from discord.ext import commands
from bot_logic import gen_pass  # Asegúrate de que gen_pass esté definido en bot_logic

# Configuración de los intents
intents = discord.Intents.default()
intents.message_content = True  # Habilita el intent para leer el contenido de los mensajes

# Inicialización del bot usando commands.Bot
bot = commands.Bot(command_prefix='$', intents=intents)

# Evento de inicio
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

# Comando hello
@bot.command()
async def hello(ctx):
    await ctx.send("¡Hola! Soy un bot")

# Comando bye
@bot.command()
async def bye(ctx):
    await ctx.send("😎")

# Comando password
@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))  # Asegúrate de que gen_pass funcione correctamente


@bot.command()
async def add(ctx, left: int, right: int):
    """Suma dos números."""
    await ctx.send(left + right)    

bot.run("TOKEN")  # Reemplaza 'TU_TOKEN_AQUÍ' con tu token real


