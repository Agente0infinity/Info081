contar_vocales(cadena):
    contador_vocales=0
    vocales="aeiouAEIOU"
    for i in cadena:

        for a in vocales:

            if a==i:

                contador_vocales+=1

    return f"hay {contar_vocales} vocales en {cadena}"

print(contar_vocales("palabra"))