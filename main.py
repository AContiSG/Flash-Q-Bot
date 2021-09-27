import discord, os,random
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

#Responde con el valor cuando termina con la clave
RIMAS={
'000': 'Esto son puras rimas de albañil',
'100': 'La tengo como un electrotrén',
'00': 'Mis huevos somnolientos',
'90': 'La mia desorienta',
'80': 'La mia atormenta',
'70': 'La mia reglamenta',
'60': 'La mia representa',
'50': 'La mia es suculenta',
'40': 'La mia sabe a polenta',
'30': 'La mia sabe a menta',
'20': 'Mi pene en tu mente',
'15': 'Tu culo +15 papu lince',
'14': ['Cuidado no la forces', 'A vos te la metió Jorge'],
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
'2': ['Te la meto y me da tos.', 'Esta es para vos', 'A vos te la metió Dross', 'Te culeo en Palamós', 'Fuiste tocado por Dios :yum:'],
'1': 'Tu culo vacuno',
'0': 'Te la meto en el trasero',
'O.o':"o.O",
'o.O':"O.o",
'que': 'so',
'yeah': 'sex',
'yea': 'sex',
'yea sex': ':sunglasses:',
'yeah sex': ':sunglasses:'
}

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
'frasedia':
["mmmmm yeah","La vida es dura pero mas dura es la vida de los niños sirios, tomá la sopa",
"momento lol","like si te pasó","sisisi","nah","bueno pero solo a veces","KeyboardInterrupt",
"jueguen al Rimworld!!","melocoton","¿Cómo motivar a una persona frases? Resultado de imagen para frases motivadoras 101 frases para inspirar y motivar líderes y empleados Algún día es una enfermedad que llevará tus sueños a la tumba contigo Clic para tuitear.Cuanto más hacemos, más podemo",
 "Y", "Es muy divertido lograr lo imposible. (????????)"],
'changelog':"Nuevas funciones: hola, hoal, frasedia y changelog\n Añadida una función que me permite que un numero pueda tener varias rimas (solo está en el 2 para probar)\n Mejoré algunas pavadas\n Le tengo que cambiar el formato a esto!!!",
'len':longitud
}

#Comandos que NO devuelven una string (Sin Return)
COMANDOS_SR={
"help": funcion_help
}

HELP_DICT={
"$help": "$help rimas1 o $help rimas2 para ver las posibles rimas",
'$saludo':"Un saludo",
'$len':"Devuelve la longitud de la palabra. Ej: $len hola =4",
'$auris':"Y esos auris de virgo momo???? (video)",
'$atiendo':"Atendes boludos (video)",
'$arrepentir':"Samid vs Viale (qdep) (video)",
'$babadungo':"Legendaria cancion (video)",
'$gatotruco':"Cat trick (video)",
'$pl tato':"Musicarda dou (playlist)",
'$pl busto':"asdfg op (playlist)",
'$pl yuyu':"Anime Music (playlist)",
'$hola':"Mas saludos",
'$hoal':"Muchisimos saludos",
'$frasedia':"La frase del momento! (realmente no es una sola por dia lol!)",
'$changelog':"Importantísima funcion que te avisa de todos los muchísimos nuevos cambios de la ultima actualización!!(flashee programador)"
}

RIMAS1={
'-000': 'Esto son puras rimas de albañil',
'100': 'La tengo como un electrotrén',
'-00': 'Mis huevos somnolientos',
'90': 'La mia desorienta',
'80': 'La mia atormenta',
'70': 'La mia reglamenta',
'60': 'La mia representa',
'50': 'La mia es suculenta',
'40': 'La mia sabe a polenta',
'30': 'La mia sabe a menta',
'20': 'Mi pene en tu mente',
'15': 'Tu culo +15 papu lince',
'14': 'Cuidado no la forces',
'13': 'En tu culo se me cuece',
'12': 'Te la meto sin que roce',
'11': 'la tengo de bronce'}

RIMAS2={
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
'O.o':"o.O",
'o.O':"O.o",
'que': 'so',
'yeah': ':sunglasses: :sunglasses: :sunglasses: :sunglasses:',
'yeah sex': ':cowboy:',
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
                if isinstance(RIMAS[numero], list):
                    rima=random.choice(RIMAS[numero])
                    await mensaje.channel.send(rima)
                    break
#------------------------------Final------------------------------------------#

keep_alive()
client.run(os.getenv('TOKEN'))