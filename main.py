import discord, os
from keep_alive import keep_alive

client= discord.Client()


#-------------------------------Funciones------------------------------------#

def longitud(medible):
    return len(medible)

def analizar_contenido(msg,comando):
    linea=msg.split(" ")
    return linea[1] #retorna solo la primer palabra despues del comando


#---------------------------------V. globales--------------------------------#

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
'que': 'so'
}

COMANDOS_SIMPLES={
'saludo':"hoal",
'auris':"https://www.youtube.com/watch?v=ptJJG8ucn48",
'atiendo':"https://www.youtube.com/watch?v=i5Vdl_unhHQ",
'arrepentir':"https://www.youtube.com/watch?v=RcAP6hl7T0g",
'babadungo':"https://www.youtube.com/watch?v=y-BWKxp322w",
'O.o':"o.O",
'o.O':"O.o",
'len':longitud,
}

PREFIJO="$"

SWITCH_RIMAS=True


#-------------------------------Al ejecutar-----------------------------------#

@client.event
async def on_ready():
    print('{0.user} se inicio correctamente.'.format(client))

#-------------------------------On message------------------------------------#

@client.event
async def on_message(mensaje):
    if mensaje.author == client.user:
        return

    msg = mensaje.content
    
    for comando in COMANDOS_SIMPLES.keys():
        if msg.startswith(PREFIJO+comando):
            if isinstance(COMANDOS_SIMPLES[comando], str):
                await mensaje.channel.send(COMANDOS_SIMPLES[comando])

            else:
                await mensaje.channel.send(COMANDOS_SIMPLES[comando](analizar_contenido(msg,comando)))
                
                
    if SWITCH_RIMAS:  
        for numero in RIMAS.keys():
            if msg.endswith(numero):
                rima=RIMAS[numero]
                await mensaje.channel.send(rima)
                break

#------------------------------Final------------------------------------------#

keep_alive()
client.run(os.getenv('TOKEN'))