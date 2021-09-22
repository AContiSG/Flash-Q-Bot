from os import system
from main import *

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
'14': 'Cuidado no la forces',
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
'2': ['Te la meto y me da tos.', 'Esta es para vos'],
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
"jueguen al Rimworld!!","melocoton","¿Cómo motivar a una persona frases? Resultado de imagen para frases motivadoras 101 frases para inspirar y motivar líderes y empleados Algún día es una enfermedad que llevará tus sueños a la tumba contigo ﻿Clic para tuitear.Cuanto más hacemos, más podemo",
 "Y", "Es muy divertido lograr lo imposible. (????????)"],
'changelog':"Nuevas funciones: hola, hoal, frasedia y changelog\n Añadí una función que me permite que un numero pueda tener varias rimas (solo está en el 2 para probar) \n Mejoré algunas pavadas \n Le tengo que cambiar el formato a esto!!!",
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
'hola':"unsaludo",
'hola':"Mas saludos",
'hoal':"Muchisimos saludos",
'frasedia': "La frase del momento! (realmente no es una sola por dia lol!) ",
'changelog':"Importantísima funcion que te avisa de todos los muchísimos nuevos cambios de la ultima actualización!!(flashee programador)"
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
