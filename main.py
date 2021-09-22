import discord, os,random
from Diccionarios import *
from keep_alive import keep_alive

client= discord.Client()


#-------------------------------Funciones------------------------------------#

def longitud(medible):
    #mide los caracteres de la palabra ingresada
    return len(medible)

def analizar_contenido(msg):
    #retorna solo la primer palabra despues del comando
    linea=msg.split(" ")
    linea.append(" ")
    if linea[1] != " ":
        return linea[1]
    else:
        return None

async def funcion_help(mensaje):
    embedh= discord.Embed(
        title = "Help",
        colour= discord.Colour.light_gray()
        )
    
    if analizar_contenido(mensaje.content)=="rimas1" or analizar_contenido(mensaje.content)=="rimas":
        for rimas in RIMAS1.keys():
            embedh.add_field(name= rimas,value= RIMAS1[rimas], inline=False)
        embedh.set_footer(text="rimas 1")
        await mensaje.channel.send(embed=embedh)

    if analizar_contenido(mensaje.content)=="rimas2":
        for rimas in RIMAS2.keys():
            embedh.add_field(name= rimas,value= RIMAS2[rimas], inline=False)
        embedh.set_footer(text="rimas 2")
        await mensaje.channel.send(embed=embedh)
            
    if analizar_contenido(mensaje.content)=="comandos" or analizar_contenido(mensaje.content) == None:
        for comandos in HELP_DICT.keys():
            embedh.add_field(name= comandos,value= HELP_DICT[comandos], inline=False)
        embedh.set_footer(text="Comandos")
        await mensaje.channel.send(embed=embedh)


#---------------------------------V. globales--------------------------------#

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
    
    if msg.startswith(PREFIJO):
    #Comandos
        for comando in COMANDOS_SIMPLES.keys():
            if msg.startswith(PREFIJO+comando):
                if isinstance(COMANDOS_SIMPLES[comando], str):
                    await mensaje.channel.send(COMANDOS_SIMPLES[comando])
                    break
                if isinstance(COMANDOS_SIMPLES[comando], list):
                    await mensaje.channel.send(random.choice(COMANDOS_SIMPLES[comando]))
                    break
                else:
                    await mensaje.channel.send(COMANDOS_SIMPLES[comando](analizar_contenido(msg)))
                    break

        for comando in COMANDOS_SR.keys():
            if msg.startswith(PREFIJO+comando):
                await COMANDOS_SR[comando](mensaje)
                break

    
    if SWITCH_RIMAS:
    #Si empieza con
        for numero in RIMAS.keys():
            if msg.endswith(numero) and not msg.startswith(PREFIJO):
                if isinstance(RIMAS[numero], str):
                    rima=RIMAS[numero]
                    await mensaje.channel.send(rima)
                    break
                if isinstance(RIMAS[numero], list):
                    rima=random.choice(RIMAS[numero])
                    await mensaje.channel.send(rima)
                    break
                break
#------------------------------Final------------------------------------------#

keep_alive()
client.run(os.getenv('TOKEN'))