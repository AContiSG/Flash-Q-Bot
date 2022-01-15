import discord, os, random
import requests
from bs4 import BeautifulSoup
from keep_alive import keep_alive

client = discord.Client()

#-------------------------------Funciones------------------------------------#

def longitud(medible):
    #Mide los caracteres de la palabra ingresada
    return len(medible[5:])

def crear_TUPLA_RIMAS():
    #Crea una tupla de listas de 14 items con las keys de RIMAS
    lista = [[]]
    contador = 0
    pagina = 0
    for rima in RIMAS.keys():
        if contador == 13:
            lista[pagina].append(rima)
            lista.append([])
            contador = 0
            pagina += 1
        else:
            lista[pagina].append(rima)
            contador += 1
    return tuple(lista)

def analizar_contenido(msg, numero):
    #Retorna la palabra que especifica el numero o todas si este es "n"
    linea = msg.split(" ")
    if numero != "n":
        try:
            if linea[int(numero)]:
                return linea[int(numero)]
        except:
            return None
    else:
        return linea

def sacarTituloRandom():
    # Da el titulo de una pagina aleatoria de Wikipedia 
    # by yuyu
    urlRandom = requests.get(url= "https://es.wikipedia.org/wiki/Especial:Aleatoria")
    soup = BeautifulSoup(urlRandom.content, 'html.parser')
    titulo = soup.find(id= "firstHeading").string
    return titulo

def activar_desactivar_rimas(mensaje):
    if SWITCH_RIMAS:
        SWITCH_RIMAS.clear()
        return "Rimas desactivadas"
    else:
        SWITCH_RIMAS.append(1)
        return "Rimas activadas"

async def funcion_help(mensaje):
    em_help = discord.Embed(
        title = "Help",
        colour = discord.Colour.light_gray()
        )
    
    contenido_analizado_1 = analizar_contenido(mensaje.content, 1)
    
    if contenido_analizado_1 == "rimas":
        if analizar_contenido(mensaje.content, 2) != None:
            pagina_deseada = int(analizar_contenido(mensaje.content, 2)) -1
        else:
            pagina_deseada = 0
        
        for rimas in TUPLA_RIMAS[pagina_deseada]:
            if isinstance(RIMAS[rimas], tuple):
                suma_rimas = ""
                for item in RIMAS[rimas]:
                    suma_rimas += item + " / "
                em_help.add_field(name = rimas, value = suma_rimas, inline = False)
            if isinstance(RIMAS[rimas], str):
                em_help.add_field(name = rimas, value = RIMAS[rimas], inline = False)
            
        em_help.set_footer(text = f"Rimas {pagina_deseada + 1}")
        await mensaje.channel.send(embed = em_help)

            
    if contenido_analizado_1 == "comandos" or contenido_analizado_1 == None:
        for comandos in HELP_DICT.keys():
            em_help.add_field(name = PREFIJO + comandos, value = HELP_DICT[comandos], inline = False)
        em_help.set_footer(text = "Comandos")
        await mensaje.channel.send(embed = em_help)

async def changelog(mensaje):
    em_changelog = discord.Embed(
        title = "Changelog",
        colour = discord.Colour.light_gray()
        )
    
    em_changelog.add_field(name = "Ajustes",inline=False, value = f"""
    - Pavadas
    - Preparacion para una futura forma de cambiar el prefijo con el que llamar a los comandos (actualmente {PREFIJO})
    """)
    em_changelog.add_field(name = "Nuevo",inline=False, value = f"""
    - Conseguí que se puedan desactivar las rimas del orto!!!! {PREFIJO}switch
    - Función de lista de las cosas más buenisimas (sacadas aleatoriamente de wikipedia) {PREFIJO}buenisimas
    - Nuevas frases en {PREFIJO}frase
    """)
    em_changelog.add_field(name = "Sacado",inline=False, value = """
    - creo q nada pero no me acuerdo 
    """)
    em_changelog.set_footer(text = "v.1.4")
    
    await mensaje.channel.send(embed = em_changelog)
    
async def poema(mensaje):
    #Lo encontré en un comentario de YT, simplemente arte
    POEMA_trece1="Dijo 13? Aquí tiene pa que me la bese, entre más me la beses más me crece, busca un cura pa que me la rece, y trae un martillo pa que me la endereces, por el chiquito se te aparece toas las veces y cuando te estreses aquí te tengo éste pa que te desestreses, con este tallo el jopo se te esflorece, se cumple el ciclo hasta que anochece, to los días y toas las veces, de tanto entablar la raja del jopo se te desaparece, porque este sable no se compadece, si pides ñapa se te ofrece, y si repites se te agradece, no te hace rico pero tampoco te empobrece, no te hace inteligente pero tampoco te embrutece, y no paro aquí compa que éste nuevamente se endurece, hasta que amanece, cambie esa cara que parece que se entristece, si te haces viejo éste te rejuvenece, no te hago bulla porque depronto te ensordece, y eso cuadro no te favorece, pero tranquilo que éste te abastece, porque allá abajo se te humedece, viendo como el que me cuelga resplandece, si a ti te da miedo a mí me enorgullece, y así toas las vece ¿que te parece?, y tranquilo mijo que aquí éste reaparece, no haga fuerza porque éste se sobrecrece, una fresadora te traigo pa que me la freses, así se fortalece y de nuevo la historia se establece, que no se te nuble la vista porque éste te la aclarece, y sino le entendiste nuevamente la explicación se te ofrece, pa que por el chiquito éste de nuevo te empiece..."
    POEMA_trece2="Aquí tienes para que me la beses, entre más me la beses más me crece, busca un cura para que me la rece, un martillo para que me la endereces, un chef para que me la aderece, 8000 mondas por el culo se te aparecen, si me la sobas haces que se me espese, si quieres la escaneas y te la llevas para que en tu hoja de vida la anexes, me culeo a tu maldita madre y qué te parece le meti la monda a tú mamá hace 9 meses y después la puse a escuchar René de Calle 13  Te la meto por debajo del agua como los peces, y aquella flor de monda que en tu culo crece, reposa sobre tus nalgas a veces y descansa en paz en tu chicorio cuando anochece Que te parece, te lo meti antes de los 9 meses te meto la verga pa que el tunel del orto se te enderece, de tanta monda hasta tu novia va a queda preña de mi por 9 meses, te la empujo y te la pongo pa que me la peses, y te meto la guamayeta un millon de veces que de tanta monda van a respirar hasta los peces.si te pareció poco... los dobladillos del culo al leer esto texto se te estremecen, esa raja seca una mondaquera se merece, tranquila que sigo como jeison en viernes 13, la cabeza de la mondá después se me adormece, pero tranquila que eso no te favorece, si se despierta te va regar de leche y después me agradeces, el chiquito se te esflorece, tranquila que de mondá en éste grupo no se carece y si te la meten por el oído te en ensordeces y si te la meten entre todos te desfortaleces y eso no te conviene porque te enflaqueces pero tranquila que esos pelos del culo vuelven y te crecen como campo te reflorece y a tu maldit4 madre se la empujo a veces, ya que el culo se le enmugrece y si me ve la mondá nuevamente se aloquece y eso no te conviene porque me vas hacer que de nuevo contigo empiece te lo meto desde que amanece hasta que anochece,  sin que se te humedece y como tabaco de marihuana te embobece,  y éste como bendición de Dios te abastece, se me endurece nuevamente y deja de hacerte la paja porque ésta enseguece."
    
    await mensaje.channel.send(POEMA_trece1)
    await mensaje.channel.send(POEMA_trece2)    

async def lista_buenisimas(mensaje):
    if analizar_contenido(mensaje.content, 1) == None:
        limite_top = 10
    elif int(analizar_contenido(mensaje.content, 1)) > 25:
        limite_top = 25
    else:
        limite_top = int(analizar_contenido(mensaje.content, 1))

    await mensaje.channel.send("La lista tarda un poco en crearse, espera un cacho")

    em_buenisimas = discord.Embed(
        title = f"Top {limite_top} cosas más buenisimas",
        colour = discord.Colour.light_gray()
        )
    em_buenisimas.add_field(name = 1, value = "Matar gente", inline = False)

    for x in range(2, limite_top + 1):
        em_buenisimas.add_field(name = x, value = sacarTituloRandom(), inline = False)
    
    em_buenisimas.set_footer(text = "Ta wenísimo")
    await mensaje.channel.send(embed = em_buenisimas)


#---------------------------------V. globales--------------------------------#
PREFIJO = "$"

#Posibles frases motivadoras
FRASEMOT_TUP = ("mmmmm yeah",
"Tomá la sopa",
"momento lol",
"like si te pasó",
"sisisi",
"nah",
"bueno pero solo a veces",
"KeyboardInterrupt",
"jueguen Rimworld!!",
"melocoton",
"¿Cómo motivar a una persona frases? Resultado de imagen para frases motivadoras 101 frases para inspirar y motivar líderes y empleados Algún día es una enfermedad que llevará tus sueños a la tumba contigo Clic para tuitear.Cuanto más hacemos, más podemo",
"Una botella de queeeee!????",
"Es muy divertido lograr lo imposible. (????????)",
"Also try Terraria",
"Ese no mejor el de la izquierda",
"No lo tenés en rojo?",
":alien:",
"asi :pinched_fingers:",
"Al que madruga bla bla bla...",
"179.235.61.185",
"Sabalero",
"Toot toot",
"¡Un revolver puede decir ¡BANG!, ¡PANG! e inclusive, ¡PUNG! pero nunca Y!",
"El famoso trompetista de color",
"ajajajje",
"Me pasó",
"Buenísimo",
"minceraft",
"meningococo",
"hue hue hue hue",
"?",
"un saludo a la flia",
"chaucha",
"ramparte",
"""
Lactuca sativa, conocida comúnmente como *lechuga*, es una planta herbácea propia de las regiones semitempladas que se cultiva como alimento. Debido a las muchas variedades que existen y a su cultivo cada vez mayor en invernaderos, se puede consumir durante todo el año.

Descripción
Plantas anuales o bienales que pueden llegar a medir 1 m de altura. La raíz es pivotante y se ramifica unos 25 cm.
Desarrolla una roseta basal de hojas obovadas —en ocasiones dispuestas apretadamente como los repollos— con márgenes dentado-crenados o según las variedades, lisos, ondulados o aserrados. Cuando llega a la etapa reproductiva de la roseta surge el tallo floral con hojas pequeñas aovadas, que se ramifica a cierta altura, para producir las inflorescencias terminales, formadas por capítulos en panículas o corimbos de color amarillo (parecidos al diente de león). Las flores, de unos 10-15 mm, son liguladas con involucros de brácteas escamosas, tienen 5 estambres. El fruto es un aquenio de 6-8 mm, obovado y comprimido. Las diminutas semillas tienen un vilano plumoso.
""",
"tom hola",
"martar gente",
"harry styles",
"*ruido de mate *",
"created by obez~"
)

#Responde con el valor cuando termina con la clave
RIMAS = {
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
'14': ('Cuidado no la forces', 'A vos te la metió Jorge', 'jaja Alexelcapo'),
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
'2': ('Te la meto y me da tos.', 'Esta es para vos', 'A vos te la metió Dross', 'Te culeo en Palamós', 'Fuiste tocado por Dios','Me rasco un huevo y tengo dos'),
'1': 'Tu culo vacuno',
'0': 'Te la meto en el trasero',
'O.o':"o.O",
'o.O':"O.o",
'que': 'so',
'yeah': 'sex',
'yea': 'sex',
'yea sex': ':sunglasses:',
'yeah sex': ':sunglasses:',
'jf': "sos vos capo",
'vusto': 'bobo',
'busto':'bobo'
}

#Comandos que devuelven una string 
COMANDOS_SIMPLES = {
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
'frase':FRASEMOT_TUP,
'len':longitud,
'invite':"https://discord.com/api/oauth2/authorize?client_id=883480644053774337&permissions=34359856192&scope=bot",
"git": "https://github.com/AContiSG/Flash-Q-Bot",
"switch":activar_desactivar_rimas
}

#Comandos que NO devuelven una string (Sin Return)
COMANDOS_SR = {
"help": funcion_help,
'changelog': changelog,
"poema":poema,
"buenisimas": lista_buenisimas
}

#Lo que imprime la funcion $help
HELP_DICT = {
"help rimas": f"{PREFIJO}help rimas *numero de pagina* para ver las posibles rimas. Ej: {PREFIJO}help rimas 2",
'saludo':"Un saludo",
'len':f"Devuelve la longitud de lo que pongas despues del comando. Ej: {PREFIJO}len hola = 4",
'auris':"Y esos auris de virgo momo???? (video)",
'atiendo':"Atendes boludos (video)",
'arrepentir':"Samid vs Viale (qdep) (video)",
'babadungo':"Legendaria cancion (video)",
'gatotruco':"Cat trick (video)",
'invite':"Manda link con la invitacion del bot",
"git": "Repositorio del bot (para ver el código)",
'hola':"Mas saludos",
'hoal':"Muchisimos saludos",
'frase':"La frase del momento!",
'changelog':"Lista de los ultimos cambios",
"poema":"Los 3359 caracteres que me motivan a seguir viviendo",
"buenisimas": f"Top cualquier numero (max 25) de las cosas más buenisimas del mundo. Ej: {PREFIJO}buenisimas 7",
"switch":"Activa o desactiva las rimas"
}

#Tupla de listas con las keys de RIMAS
TUPLA_RIMAS = crear_TUPLA_RIMAS()

SWITCH_RIMAS = [True]

#-------------------------------Al ejecutar-----------------------------------#

@client.event
async def on_ready():
    print('{0.user} se inicio correctamente.'.format(client))

#-------------------------------On message------------------------------------#

@client.event
async def on_message(mensaje):
    msg = mensaje.content

    if mensaje.author == client.user:
        return
    

    elif client.user.mentioned_in(mensaje):
    #Al mencionarlo
        await mensaje.channel.send(f"Atiendo boludos ({PREFIJO}help para la lista de comandos)")
        return
    

    elif msg.startswith(PREFIJO):
    #Comandos
        for comando in COMANDOS_SIMPLES.keys():
            if msg.startswith(PREFIJO + comando):
                if isinstance(COMANDOS_SIMPLES[comando], str):
                    await mensaje.channel.send(COMANDOS_SIMPLES[comando])
                    return
                if isinstance(COMANDOS_SIMPLES[comando], tuple):
                    await mensaje.channel.send(random.choice(COMANDOS_SIMPLES[comando]))
                    return
                else:
                    await mensaje.channel.send(COMANDOS_SIMPLES[comando](msg))
                    return

        for comando in COMANDOS_SR.keys():
            if msg.startswith(PREFIJO + comando):
                await COMANDOS_SR[comando](mensaje)
                return


    elif SWITCH_RIMAS:
    #Si empieza con
        for numero in RIMAS.keys():
            if msg.endswith(numero) and not msg.startswith(PREFIJO):
                if isinstance(RIMAS[numero], str):
                    rima = RIMAS[numero]
                    await mensaje.channel.send(rima)
                    return
                elif isinstance(RIMAS[numero], tuple):
                    rima = random.choice(RIMAS[numero])
                    await mensaje.channel.send(rima)
                    return
#------------------------------Final------------------------------------------#

keep_alive()
client.run(client.run(os.getenv('TOKEN')))