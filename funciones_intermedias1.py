# 1. Actualizar valores en diccionarios y listas#

matriz = [[10, 15, 20], [3, 7, 14]]

matriz[1][0] = 6

print(matriz)

#cantantes#

cantantes = [
    {'nombre': 'Ricky Martin', 'pais': 'Puerto Rico'},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
    ]   

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

#ciudades#
ciudades = {
    'Mexico': ['Ciudad de Mexico', 'Guadalajara', 'Cancun'],
    'Chile': ['Santiago', 'Concepcion', 'Vina del Mar']
}

ciudades['Mexico'][2] = 'Monterrey'
print(ciudades)

#coordinadas#
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]['latitud'] = 9.9355431
print(coordenadas)

#2. Iterar a traves de una lista de diccionarios#

def iterarDiccionario(lista):
    for diccionario in lista:
        elementos = ["{}-{}".format(llave, valor) for llave, valor in diccionario.items()]
        print(", ".join(elementos))

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "Jose Jose", "pais": "Mexico"},
    {"nombre": "Juan Luis Guerra", "pais": "Republica Dominicana"}
]

iterarDiccionario(cantantes)

#3. Obtener valores de una lista de diccionarios#

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "Jose Jose", "pais": "Mexico"},
    {"nombre": "Juan Luis Guerra", "pais": "Republica Dominicana"}
]

print("Valores para 'nombre':")
iterarDiccionario2("nombre", cantantes)

print("\nValores para 'pais':")
iterarDiccionario2("pais", cantantes)


#4. Iterar a traves de un diccionario con valores de lista#
def imprimirInformacion(diccionario):
    for clave, valores in diccionario.items():
        print("{} {}".format(len(valores), clave.upper()))
        for valor in valores:
            print(valor)
        print()  

costa_rica = {
    "ciudades": ["San Jose", "Limon", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)
