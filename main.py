import discord, os
from keep_alive import keep_alive

client= discord.Client()

numeros_rimas={
'20': 'Mi pene en tu mente',
'15': 'No me la hagas un esguince',
'14': 'Cuidado no la forces (malisima lol)',
'13': 'En tu culo se me cuece',
'12': 'Te la meto sin que roce',
'11': 'la tengo de bronce',
'10': 'En el culo te la ves',
'9': 'En el culo se te mueve',
'8': 'El culo te abrocho',
'7': 'En el culo se te mete',
'6': 'En el culo os la veis',
'5': 'En el culo te la hinco',
'4': 'En tu culo mi aparato',
'3': 'En el culo te la ves',
'2': 'Esta es para vos',
'1': 'Tu culo vacuno',
'0': 'Te la meto en el trasero',
'que': 'so',
'Que': 'so'}


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
	
  for numero in numeros_rimas.keys():
      if msg.endswith(numero):
          rima=numeros_rimas[numero]
          await mensaje.channel.send(rima)
          break


keep_alive()
client.run(os.getenv('TOKEN'))