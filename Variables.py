PREFIJO = "$"

GUILDS = [643940257879949322, 358991360529006592, 922646454944808981]

# Posibles frases motivadoras
FRASEMOT_TUP = ("mmmmm yeah",
                "Tomá la sopa",
                "momento lol",
                "sisisi",
                "nah",
                "bueno pero solo a veces",
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "jueguen Rimworld!!",
                "melocoton",
                "¿Cómo motivar a una persona frases? Resultado de imagen para frases motivadoras 101 frases para inspirar y motivar líderes y empleados Algún día es una enfermedad que llevará tus sueños a la tumba contigo Clic para tuitear.Cuanto más hacemos, más podemo",
                "Una botella de queeeee!????",
                "Es muy divertido lograr lo imposible. (????????)",
                "Also try Terraria",
                "Ese no mejor el de la izquierda",
                "cómo?",
                "Also try League of the Legends",
                "No lo tenés en rojo?",
                ":alien:",
                "ah",
                ":cowboy:",
                "mira vos che :rolling_eyes:",
                "asi :pinched_fingers:",
                "Al que madruga bla bla bla...",
                "Sabalero",
                "Toot toot",
                "¡Un revolver puede decir ¡BANG!, ¡PANG! e inclusive, ¡PUNG! pero nunca Y!",
                "El famoso trompetista de color",
                "Me pasó",
                "Buenísimo",
                "minceraft",
                "meningocococo",
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
                "spiderman tom hola",
                "martar gente",
                "harry styles",
                "*ruido de mate *",
                "created by obez~",
                """
Hora del dox:
IP: no se
IPv6: no se
N: no se
SS Number: no se
UPNP: no se
DMZ: bue
W: no se
MAC : no se
ISP: ya fue
""",
                """
IP: 92.28 213, 234
N: 43.7462
W: 12.4893
SS Number: 6979191519182016
IPv6: fe80::5dcd.ef69.fb22::d9888%12
UPNP: Enabled
DMZ: 10.112.42.15
MAC: 5A:78:3E7E00
ISP: Ucom Unversal
DNS: 8.8.8.8
ALT DNS: 1.1.1.8.1
DNS SUFFIX: Dlink
WAN: 100.23.10.15
WAN TYPE: Private Nat
GATEWAY: 192.168.0.1
SUBNET MASK:255.255.0.255
UDP OPEN PORTS. 8080, 80
TCP OPEN PORTS: 443
ROUTER VENDOR: ERICCSON
DEVICE VENDOR: WI
"""
                )

# Responde con el valor cuando termina con la clave
RIMAS = {
    "000": "Esto son puras rimas de albañil",
    "100": "La tengo como un electrotrén",
    "00": "Mis huevos somnolientos",
    "90": "La mia desorienta",
    "80": "La mia atormenta",
    "70": "La mia reglamenta",
    "60": "La mia representa",
    "50": "La mia es suculenta",
    "40": "La mia sabe a polenta",
    "30": "La mia sabe a menta",
    "20": "Mi pene en tu mente",
    "15": "Tu culo +15 papu lince",
    "14": ("Cuidado no la forces", "A vos te la metió Jorge", "jaja Alexelcapo"),
    "13": "En tu culo se me cuece",
    "12": "Te la meto sin que roce",
    "11": "la tengo de bronce",
    "10": "En el culo te la ves",
    "9": "En el culo se te mueve",
    "8": "El culo te abrocho",
    "7": "En el culo se te mete",
    "6": "En el culo os la veis",
    "5": "En el culo te la hinco",
    "4": "En tu culo mi aparato",
    "3": "En el culo te la ves",
    "2": ("Te la meto y me da tos.", "Esta es para vos", "A vos te la metió Dross", "Te culeo en Palamós", "Fuiste tocado por Dios", "Me rasco un huevo y tengo dos"),
    "1": "Tu culo vacuno",
    "0": "Te la meto en el trasero",
    "O.o": "o.O",
    "o.O": "O.o",
    "que": "so",
    "yeah": "sex",
    "yea": "sex",
    "yea sex": ":sunglasses:",
    "yeah sex": ":sunglasses:",
    "jf": "sos vos capo",
    "vusto": "bobo",
    "busto": "bobo",
    "hoal": "sisisaludo",
    "hola": "unsaludo",
}


# Lo que imprime la funcion $help
HELP_DICT = {
    "help rimas": f"{PREFIJO}help rimas *numero de pagina* para ver las posibles rimas. Ej: {PREFIJO}help rimas 2",
    "saludo": "Un saludo",
    "len": f"Devuelve la longitud de lo que pongas despues del comando. Ej: {PREFIJO}len hola = 4",
    "lenp": f"Te da la cantidad de palabras en una frase. Ej: {PREFIJO}lenp hola y chau = 3",
    "invite": "Manda link con la invitacion del bot",
    "git": "Repositorio del bot (para ver el código)",
    "frase": "La frase del momento!",
    "changelog": "Lista de los ultimos cambios",
    "poema": "Los 3359 caracteres que me motivan a seguir viviendo",
    "buenisimas": f"Top cualquier numero (max 25) de las cosas más buenisimas del mundo. Ej: {PREFIJO}buenisimas 7",
    "switch": "Activa o desactiva las rimas",
    "eng": "Traduce (mal) la frase que pongas (solo menos de 15 palabras). Si ponés `es´ despues del comando te lo traduce de ingles a español. Tambien podes responder a un mensaje con el comando y traducir ese mensaje.",
    "react": "Reacciona al mensaje que respondes con el emoji que le pasas",
    "p": f"Si estas en un canal de voz, entra y reproduce el audio que le digas. {PREFIJO}sonidos para ver la lista de sonidos posibles", "pr": f"Reproduce un audio aleatorio",
    "sonidos": "Te dice la lista de audios posibles"
}
