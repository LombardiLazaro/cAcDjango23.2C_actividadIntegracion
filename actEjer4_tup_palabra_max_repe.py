#-4
def dic_palabra_frec(cadena):
    cadena = cadena.lower()
    palabras = cadena.split()

    frecuencia = {}

    for palabra in palabras:
		
        if palabra[-1] in [".", ",", ":"]:
            palabra = palabra[:-1]
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia
    
def tup_palabra_max_repe(frecuencia):
    max_frec = 0
    palabra_max_frec = ""

    for palabra in frecuencia:
        if frecuencia[palabra] > max_frec:
            max_frec = frecuencia[palabra]
            palabra_max_frec = palabra

    return (palabra_max_frec, max_frec)

# cadena = 'Hola, hola: hola.'
# frecuencia = dic_palabra_frec(cadena)
# palabra, frecuencia = tup_palabra_max_repe(frecuencia)
# print(palabra, frecuencia)
