import discord, os
from keep_alive import keep_alive

client= discord.Client()

numeros_rimas={'1': 'Tu culo desayuno',
'2': 'Esta es para vos',
'3': 'En el culo te la ves',
'4': 'Como tu vieja',
'5': 'En el culo te la hinco',
'6': 'En el culo os la veis'}

def numero_en_mensaje(mensaj,  modo):
  pass



@client.event
async def on_ready():
  print('{0.user} se inicio correctamente.'.format(client))

@client.event
async def on_message(mensaje):
  if mensaje.author == client.user:
    return

  msg = mensaje.content

  if msg.startswith('$saludo'):
    await mensaje.channel.send("hoal")


  if msg.endswith(for numero in numeros_rimas.keys()):
    rima=numeros_rimas[mensaje.content]
    await mensaje.channel.send(rima)

keep_alive()
client.run(os.getenv('TOKEN'))