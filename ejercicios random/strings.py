

def contar_vocales(cadena):
    contador_vocales=0
    vocales="aeiouAEIOU"
    for i in cadena:

        for a in vocales:

            if a==i:

                contador_vocales+=1

    return f"hay {contador_vocales} vocales en {cadena}"

print(contar_vocales("palabra"))

def invertir_Cadena(cadena):

    anedac=""

    for i in range(len(cadena)):
        posicion= len(cadena)-i-1
        anedac+= cadena[posicion]

    return anedac

print(invertir_Cadena("palabra"))

