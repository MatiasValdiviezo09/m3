import discord
from discord.ext import commands
from bot_logic import gen_pass  # Asegúrate de que gen_pass esté definido en bot_logic
import random

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
    await ctx.send("🫡")

# Comando password
@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))  # Asegúrate de que gen_pass funcione correctamente


@bot.command()
async def add(ctx, left: int, right: int):
    """Suma dos números."""
    try:
        await ctx.send(left + right)
    except ValueError:
        await ctx.send("Por favor, asegúrate de que ambos valores sean números enteros.")


@bot.command()
async def show_commands(ctx):
    help_message = (
        "Aquí tienes los comandos que puedes usar:\n"
        "$hello - Saluda al bot.\n"
        "$bye - Despídete del bot.\n"
        "$password - Genera una contraseña.\n"
        "$add <número1> <número2> - Suma dos números."
        "$guess <número> - Adivina el número del 1 al 10."
    )
    await ctx.send(help_message)


@bot.command()
async def guess(ctx, number: int):
    """Adivina el número del 1 al 10."""
    secret_number = random.randint(1, 10)  # El bot elige un número entre 1 y 10
    if number == secret_number:
        await ctx.send(f"¡Correcto! El número era {secret_number} 🎉")
    else:
        await ctx.send(f"Incorrecto. El número era {secret_number}. Intenta de nuevo.")    


bot.run("TU_TOKEN_AQUÍ")  # Reemplaza 'TU_TOKEN_AQUÍ' con tu token real


