import discord
import os
import random
import requests
import time
from bs4 import BeautifulSoup
from keep_alive import keep_alive
from translate import Translator
from Variables import PREFIJO, FRASEMOT_TUP, HELP_DICT, RIMAS

client = discord.Client()

#-------------------------------Funciones------------------------------------#


def longitud(msg):
    # Mide los caracteres de la palabra ingresada
    return len(msg[5:])


def longitud_palabras(msg):
    # Mide la cantidad de palabras ingresadas
    return len(analizar_contenido(msg, "n")[1:])


def dividir_listas(lista_dividible, tipo):
    # Divide una lista grande en una tupla de listas
    if tipo == "rimas":
        tamaño_pag = 13
    elif tipo == "sonidos":
        tamaño_pag = 20
    lista = [[]]
    contador = 0
    pagina = 0
    for rima in lista_dividible:
        if contador == tamaño_pag:
            lista[pagina].append(rima)
            lista.append([])
            contador = 0
            pagina += 1
        else:
            lista[pagina].append(rima)
            contador += 1
    return tuple(lista)


def sacar_despues_puntito(punteado):
    # La mejor funcion(saca puntitos)coincido
    despunteado = ""
    for letra in punteado:
        if letra == ".":
            return despunteado
        despunteado += letra

    return despunteado


def analizar_contenido(msg, numero):
    # Retorna la palabra que especifica el numero o todas si este es "n"
    linea = msg.split(" ")
    if numero != "n":
        try:
            if linea[int(numero)]:
                return linea[int(numero)]
        except:
            return None
    else:
        return linea


async def agregar_reaccion(mensaje):
    # FIXME Tengo que hacer algo mejor, esto es solo un test
    try:
        mensaje_reaccionable = await mensaje.channel.fetch_message(mensaje.reference.message_id)
    except:
        mensaje_reaccionable = mensaje

    emoji = analizar_contenido(mensaje.content, 1)
    try:
        if emoji:
            await mensaje_reaccionable.add_reaction(emoji)
    except:
        return


async def traducir_mal(mensaje):
    # Tambien se puede usar con respuestas
    try:
        from_lan = "es"
        to_lan = "en"
        if analizar_contenido(mensaje.content, 1) == "es":
            from_lan = "en"
            to_lan = "es"
        mensaje = await mensaje.channel.fetch_message(mensaje.reference.message_id)
        empezar = 0
    except:
        empezar = 1
        from_lan = "es"
        to_lan = "en"

    palabras_traducir = analizar_contenido(mensaje.content, "n")[empezar:]
    if palabras_traducir[0] == "es":
        from_lan = "en"
        to_lan = "es"
        palabras_traducir = palabras_traducir[1:]

    if palabras_traducir and len(palabras_traducir) < 16:
        traductor = Translator(from_lang=from_lan, to_lang=to_lan,
                               provider="mymemory", email="meyom30301@altcen.com")
        traduccion = ""

        aviso = await mensaje.channel.send("Tarda un poco en traducir")

        for palabra in palabras_traducir:
            traduccion += traductor.translate(palabra) + " "
        await aviso.delete()
        await mensaje.channel.send(traduccion)

    elif len(palabras_traducir) > 16:
        await mensaje.channel.send("Menos de 15 palabras o me explota el bot")


def sacarTituloRandom():
    # Da el titulo de una pagina aleatoria de Wikipedia
    # by yuyu
    urlRandom = requests.get(
        url="https://es.wikipedia.org/wiki/Especial:Aleatoria")
    soup = BeautifulSoup(urlRandom.content, "html.parser")
    titulo = soup.find(id="firstHeading").string
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
        title="Help",
        colour=discord.Colour.light_gray()
    )

    contenido_analizado_1 = analizar_contenido(mensaje.content, 1)

    if contenido_analizado_1 == "rimas":
        numero_pag = analizar_contenido(mensaje.content, 2)

        if numero_pag:
            pagina_deseada = int(numero_pag) - 1
        else:
            numero_pag = 1
            pagina_deseada = 0

        if int(numero_pag) > len(TUPLA_RIMAS) or int(numero_pag) < 1:
            await mensaje.channel.send("Esa pagina no existe")
            return

        for rimas in TUPLA_RIMAS[pagina_deseada]:
            if isinstance(RIMAS[rimas], tuple):
                suma_rimas = ""
                for item in RIMAS[rimas]:
                    suma_rimas += item + " / "
                em_help.add_field(name=rimas, value=suma_rimas, inline=False)
            if isinstance(RIMAS[rimas], str):
                em_help.add_field(name=rimas, value=RIMAS[rimas], inline=False)

        em_help.set_footer(text=f"Rimas {pagina_deseada + 1}")
        await mensaje.channel.send(embed=em_help)

    elif contenido_analizado_1 == "comandos" or contenido_analizado_1 == None:
        for comandos in HELP_DICT.keys():
            em_help.add_field(name=PREFIJO + comandos,
                              value=HELP_DICT[comandos], inline=False)
        em_help.set_footer(text="Comandos")
        await mensaje.channel.send(embed=em_help)


async def changelog(mensaje):
    version = "v1.5.4"
    em_changelog = discord.Embed(
        title=f"{version}: changelog",
        description=f"Sonidos randoms :sunglasses:",
        colour=discord.Colour.light_gray()
    )

    em_changelog.add_field(name="Nuevo", inline=False, value=f"""
    - {PREFIJO}pr, reproduce un audio aleatorio.
    - Un par de audios nuevos.
    - Nada más xd.
    """)

    em_changelog.set_footer(text=f"{version}")

    await mensaje.channel.send(embed=em_changelog)


async def poema(mensaje):
    # Lo encontré en un comentario de YT, simplemente arte
    POEMA_trece1 = "Dijo 13? Aquí tiene pa que me la bese, entre más me la beses más me crece, busca un cura pa que me la rece, y trae un martillo pa que me la endereces, por el chiquito se te aparece toas las veces y cuando te estreses aquí te tengo éste pa que te desestreses, con este tallo el jopo se te esflorece, se cumple el ciclo hasta que anochece, to los días y toas las veces, de tanto entablar la raja del jopo se te desaparece, porque este sable no se compadece, si pides ñapa se te ofrece, y si repites se te agradece, no te hace rico pero tampoco te empobrece, no te hace inteligente pero tampoco te embrutece, y no paro aquí compa que éste nuevamente se endurece, hasta que amanece, cambie esa cara que parece que se entristece, si te haces viejo éste te rejuvenece, no te hago bulla porque depronto te ensordece, y eso cuadro no te favorece, pero tranquilo que éste te abastece, porque allá abajo se te humedece, viendo como el que me cuelga resplandece, si a ti te da miedo a mí me enorgullece, y así toas las vece ¿que te parece?, y tranquilo mijo que aquí éste reaparece, no haga fuerza porque éste se sobrecrece, una fresadora te traigo pa que me la freses, así se fortalece y de nuevo la historia se establece, que no se te nuble la vista porque éste te la aclarece, y sino le entendiste nuevamente la explicación se te ofrece, pa que por el chiquito éste de nuevo te empiece..."
    POEMA_trece2 = "Aquí tienes para que me la beses, entre más me la beses más me crece, busca un cura para que me la rece, un martillo para que me la endereces, un chef para que me la aderece, 8000 mondas por el culo se te aparecen, si me la sobas haces que se me espese, si quieres la escaneas y te la llevas para que en tu hoja de vida la anexes, me culeo a tu maldita madre y qué te parece le meti la monda a tú mamá hace 9 meses y después la puse a escuchar René de Calle 13  Te la meto por debajo del agua como los peces, y aquella flor de monda que en tu culo crece, reposa sobre tus nalgas a veces y descansa en paz en tu chicorio cuando anochece Que te parece, te lo meti antes de los 9 meses te meto la verga pa que el tunel del orto se te enderece, de tanta monda hasta tu novia va a queda preña de mi por 9 meses, te la empujo y te la pongo pa que me la peses, y te meto la guamayeta un millon de veces que de tanta monda van a respirar hasta los peces.si te pareció poco... los dobladillos del culo al leer esto texto se te estremecen, esa raja seca una mondaquera se merece, tranquila que sigo como jeison en viernes 13, la cabeza de la mondá después se me adormece, pero tranquila que eso no te favorece, si se despierta te va regar de leche y después me agradeces, el chiquito se te esflorece, tranquila que de mondá en éste grupo no se carece y si te la meten por el oído te en ensordeces y si te la meten entre todos te desfortaleces y eso no te conviene porque te enflaqueces pero tranquila que esos pelos del culo vuelven y te crecen como campo te reflorece y a tu maldit4 madre se la empujo a veces, ya que el culo se le enmugrece y si me ve la mondá nuevamente se aloquece y eso no te conviene porque me vas hacer que de nuevo contigo empiece te lo meto desde que amanece hasta que anochece,  sin que se te humedece y como tabaco de marihuana te embobece,  y éste como bendición de Dios te abastece, se me endurece nuevamente y deja de hacerte la paja porque ésta enseguece."

    await mensaje.channel.send(POEMA_trece1)
    await mensaje.channel.send(POEMA_trece2)


async def lista_buenisimas(mensaje):
    # Imprime por pantalla una lista de cosas buenisimas
    if analizar_contenido(mensaje.content, 1) == None or int(analizar_contenido(mensaje.content, 1)) < 1:
        limite_top = 10
    elif int(analizar_contenido(mensaje.content, 1)) > 25:
        limite_top = 25
    else:
        limite_top = int(analizar_contenido(mensaje.content, 1))

    aviso = await mensaje.channel.send("La lista tarda un poco en crearse, espera un cacho")

    em_buenisimas = discord.Embed(
        title=f"Top {limite_top} cosas más buenisimas",
        colour=discord.Colour.light_gray()
    )
    em_buenisimas.add_field(name=1, value="Matar gente", inline=False)

    for x in range(2, limite_top + 1):
        em_buenisimas.add_field(
            name=x, value=sacarTituloRandom(), inline=False)

    em_buenisimas.set_footer(text="Ta wenísimo")

    await aviso.delete()
    await mensaje.channel.send(embed=em_buenisimas)


def lista_sonidos():
    directory = 'Sonidos'
    lista = []
    for filename in os.scandir(directory):
        if filename.is_file():
            lista.append(sacar_despues_puntito(filename.name))
    return lista


async def sonidos(mensaje):
    em_sonidos = discord.Embed(
        title="Sonidos posibles",
        colour=discord.Colour.light_gray()
    )

    numero_pag = analizar_contenido(mensaje.content, 1)

    if numero_pag:
        pagina_deseada = int(numero_pag) - 1
    else:
        numero_pag = 1
        pagina_deseada = 0

    if int(numero_pag) > len(TUPLA_SONIDOS) or int(numero_pag) < 1:
        await mensaje.channel.send("Esa pagina no existe")
        return

    for sonido in TUPLA_SONIDOS[pagina_deseada]:
        em_sonidos.add_field(name=sonido, value=f"{PREFIJO}p {sonido}")

    em_sonidos.set_footer(text=f"Sonidos {pagina_deseada + 1}")
    await mensaje.channel.send(embed=em_sonidos)


async def play_random(mensaje):
    try:
        voice_channel = mensaje.author.voice.channel
    except:
        await mensaje.channel.send(str(mensaje.author.name) + " no estas en un canal pelandrún (no se que es pelandrún).")
        return

    nombre_archivo = random.choice(LISTA_SONIDOS)

    try:
        vc = await voice_channel.connect()
    except:
        await mensaje.channel.send("Baja un cambio ya esta sonando algo.")
        return
    try:
        vc.play(discord.FFmpegPCMAudio(
            source=f"Sonidos/{nombre_archivo}.wav", options="-filter:a loudnorm"))
    except:
        await vc.disconnect()
    # zzz mientras esta andando
    while vc.is_playing():
        time.sleep(0.3)
    await vc.disconnect()


async def play_sonido(mensaje):
    # Reproduce audios de la carpeta Sonidos.
    try:
        voice_channel = mensaje.author.voice.channel
    except:
        await mensaje.channel.send(str(mensaje.author.name) + " no estas en un canal pelandrún (no se que es pelandrún).")
        return

    contenido = analizar_contenido(mensaje.content, 1)

    if not contenido or not contenido in LISTA_SONIDOS:
        return

    nombre_archivo = sacar_despues_puntito(contenido)

    try:
        vc = await voice_channel.connect()
    except:
        await mensaje.channel.send("Baja un cambio ya esta sonando algo.")
        return
    try:
        vc.play(discord.FFmpegPCMAudio(
            source=f"Sonidos/{nombre_archivo}.wav", options="-filter:a loudnorm"))
    except:
        await vc.disconnect()
    # zzz mientras esta andando
    while vc.is_playing():
        time.sleep(0.3)
    await vc.disconnect()

#---------------------------------V. globales--------------------------------#

# Comandos que devuelven una string
COMANDOS_SIMPLES = {
    "saludo": "hoal",
    "pl tato": "https://www.youtube.com/playlist?list=PLFsa3redc-GX4A7yDx9ZjESAz8mt_wWJK",
    "pl busto": "https://www.youtube.com/playlist?list=PLz-W7ibs4AmjFzD3tO4o9DBtVMb-UgZ54",
    "pl yuyu": "https://www.youtube.com/playlist?list=PLXSQn9CA1N0j7Z_8iJLrPUTnl0zG5TpRN",
    "frase": FRASEMOT_TUP,
    "lenp": longitud_palabras,
    "len": longitud,
    "invite": "https://discord.com/api/oauth2/authorize?client_id=883480644053774337&permissions=34359856192&scope=bot",
    "git": "https://github.com/AContiSG/Flash-Q-Bot",
    "switch": activar_desactivar_rimas
}

# Comandos que NO devuelven una string (Sin Return)
COMANDOS_SR = {
    "help": funcion_help,
    "changelog": changelog,
    "poema": poema,
    "buenisimas": lista_buenisimas,
    "eng": traducir_mal,
    "react": agregar_reaccion,
    "p": play_sonido,
    "pr": play_random,
    "sonidos": sonidos
}

LISTA_SONIDOS = lista_sonidos()

# Tuplas de listas
TUPLA_RIMAS = dividir_listas(RIMAS.keys(), "rimas")
TUPLA_SONIDOS = dividir_listas(LISTA_SONIDOS, "sonidos")

SWITCH_RIMAS = [True]

#-------------------------------Al ejecutar-----------------------------------#


@client.event
async def on_ready():
    print("{0.user} se inicio correctamente.".format(client))

#-------------------------------On message------------------------------------#


@client.event
async def on_message(mensaje):
    msg = mensaje.content

    if mensaje.author == client.user:
        return

    elif msg.startswith(PREFIJO):
        # Comandos
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

    elif client.user.mentioned_in(mensaje):
        # Al mencionarlo
        await mensaje.channel.send(f"Atiendo boludos ({PREFIJO}help para la lista de comandos)")
        return

    elif SWITCH_RIMAS:
        # Si empieza con
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
client.run(os.getenv("TOKEN"))
