import discord, os

client= discord.Client()

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


client.run(os.getenv('TOKEN'))