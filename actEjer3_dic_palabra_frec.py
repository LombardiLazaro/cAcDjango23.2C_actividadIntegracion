#-3
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

# cadena = 'Hola, hola: hola.'
# print(dic_palabra_frec(cadena))
