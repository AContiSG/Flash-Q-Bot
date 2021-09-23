import discord, os,random
from keep_alive import keep_alive
from diccionarios import *

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

#Comandos que devuelven una string 
COMANDOS_SIMPLES={
'saludo':"hoal",
'auris':"https://www.youtube.com/watch?v=ptJJG8ucn48",
'atiendo':"https://www.youtube.com/watch?v=i5Vdl_unhHQ",
'arrepentir':"https://www.youtube.com/watch?v=RcAP6hl7T0g",
'babadungo':"https://www.youtube.com/watch?v=y-BWKxp322w",
'gatotruco':"https://www.youtube.com/watch?v=V08RzyPWurE",
'pl tato':"https://www.youtube.com/playlist?list=PLFsa3redc-GX4A7yDx9ZjESAz8mt_wWJK",
'pl busto':"https://www.youtube.com/playlist?list=PLz-W7ibs4AmjFzD3tO4o9DBtVMb-UgZ54",
'pl yuyu':"https://www.youtube.com/playlist?list=PLXSQn9CA1N0j7Z_8iJLrPUTnl0zG5TpRN",
'hoal':"sisisaludo",
'hola':"unsaludo",
'frasedia':FRASEDIA_TUP,
'changelog':"Nuevas funciones: hola, hoal, frasedia y changelog\n Añadida una función que me permite que un numero pueda tener varias rimas (solo está en el 2 para probar)\n Mejoré algunas pavadas\n Le tengo que cambiar el formato a esto!!!",
'len':longitud
}

#Comandos que NO devuelven una string (Sin Return)
COMANDOS_SR={
"help": funcion_help
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

    
    if SWITCH_RIMAS:
    #Si empieza con
        for numero in RIMAS.keys():
            if msg.endswith(numero) and not msg.startswith(PREFIJO):
                if isinstance(RIMAS[numero], str):
                    rima=RIMAS[numero]
                    await mensaje.channel.send(rima)
                    break
                if isinstance(RIMAS[numero], tuple):
                    rima=random.choice(RIMAS[numero])
                    await mensaje.channel.send(rima)
                    break
#------------------------------Final------------------------------------------#

keep_alive()
client.run(os.getenv('TOKEN'))