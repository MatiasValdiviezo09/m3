import discord
from discord.ext import commands
from bot_logic import gen_pass  # Importamos la función
# import * - es una forma rápida de importar todos los archivos de la biblioteca
from bot_logic import *
import math
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('¡Hola! Soy un bot')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$raiz'):
        try:
            # Obtener el número después del comando
            _, num_str = message.content.split()
            numero = float(num_str)
            resultado = math.sqrt(numero)
            await message.channel.send(f"La raíz cuadrada de {numero} es {int(resultado)}" if resultado.is_integer() else f"La raíz cuadrada de {numero} es {resultado:.2f}")
        except (ValueError, IndexError):
            await message.channel.send("Por favor, proporciona un número válido. Uso: `$raiz <número>`")
    elif message.content.startswith('$factorial'):
        try:
            # Obtener el número después del comando
            _, num_str = message.content.split()
            numero = int(num_str)
            if numero < 0:
                await message.channel.send("El factorial no está definido para números negativos.")
            else:
                resultado = math.factorial(numero)
                await message.channel.send(f"El factorial de {numero} es {resultado}")
        except (ValueError, IndexError):
            await message.channel.send("Por favor, proporciona un número válido. Uso: `$factorial <número>`")
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")

client.run("TOKEN")


