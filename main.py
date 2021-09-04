import discord, os
from keep_alive import keep_alive

client= discord.Client()

RIMAS={
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

COMANDOS_SIMPLES={
'saludo':"hoal",
'auris':"https://www.youtube.com/watch?v=ptJJG8ucn48",
'atiendo':"https://www.youtube.com/watch?v=i5Vdl_unhHQ",
'arrepentir':"https://www.youtube.com/watch?v=RcAP6hl7T0g",
'babadungo':"https://www.youtube.com/watch?v=y-BWKxp322w",
'0.o':"o.0",
'o.0':"0.o"
}

PREFIJO="$"

@client.event
async def on_ready():
    print('{0.user} se inicio correctamente.'.format(client))

@client.event
async def on_message(mensaje):
    if mensaje.author == client.user:
        return

    msg = mensaje.content
    
    for comando in COMANDOS_SIMPLES.keys():
        if msg.startswith(PREFIJO+comando):
            mandar_comando=COMANDOS_SIMPLES[comando]
            await mensaje.channel.send(mandar_comando)

    for numero in RIMAS.keys():
        if msg.endswith(numero):
            rima=RIMAS[numero]
            await mensaje.channel.send(rima)
            break


keep_alive()
client.run(os.getenv('TOKEN'))