def calificaciones_onepiece():
    suma_calificacion = 0 
    for i in range(3):

        calificacion=float("ingresa tu calificacion nakama")

        suma_calificacion += calificacion

    return suma_calificacion/3

def choripan():
    choripanes_tragados = 0
    respuesta=input("¿quieres choripan")

    while respuesta.lower() == "si":
        choripanes_tragados += 1
        print("come tu choripan")
        respuesta=input("¿quieres choripan?")

        if choripanes_tragados == 2:

            break

def par_impar(numero):

    if numero%2 == 0:

        return f" {numero} es par"
    
    else:

        return f" {numero} es impar"

    
