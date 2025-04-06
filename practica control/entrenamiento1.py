
matriz = [
    [1, 2, 3, 5],
    [8, 13, 21, 34],
    [55, 89, 144, 233],
    [1, 1, 2, 3]
]

n = 3

laberinto = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
nodo_inicio = 'A'


def imprimir_pares_parentesis(numero_permutaciones: int)-> list:
    lista=[]
    string_base_one=")"
    string_base_two="("
    if numero_permutaciones==1:
        lista.append(")")
        lista.append("(")

        return lista
    else:
      
        
        lista.extend(extender(string_base_one,numero_permutaciones-1))
        lista.extend(extender(string_base_two,numero_permutaciones-1))

        return lista
def extender(string_base,numero_permutaciones):

    if numero_permutaciones==1:
        listita=[string_base+"(",string_base+")"]
        return listita
    
    else:
        listita=[]
        string_base1=string_base+")"
        string_base2=string_base+"("
        listita.extend(extender(string_base1,numero_permutaciones-1))
        listita.extend(extender(string_base2,numero_permutaciones-1))
        return listita


print(imprimir_pares_parentesis(4))

def laberinto(laberinto_matriz:list)->list:
    recorrido=crear_ruta(laberinto_matriz)

    imprimir_recorrido()
def crear_ruta(laberinto_matriz:list)->list:
    recorrido.append(analizar_ruta(1))
def analizar_ruta():


    

def retroceder():

def imprimir_recorrido():




        
        


   
    

   

    

       

