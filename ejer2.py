from random import randint, choice
from cola import Cola, vacia, atencion, arribo
from arbolbinario import nodoArbol, insertar
import csv

a_nombres = None
a_tipo = None
a_numero = None

def cargar_datos():
    global nombre
    nombre = []
    with open('pokemon.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            nombre.append(fila[1].lower())

cargar_datos()
class Pokemon():
    
    def __init__(self, nombre, numero, tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad
    
    def __str__(self):
       return self.nombre + ' ' + str(self.numero) + ' ' + self.tipo + ' ' + self.debilidad


tipo = ['agua', 'fuego', 'tierra', 'electrico']
debilidades = ['agua', 'fuego', 'tierra', 'electrico', 'Jolteon','Tyrantum', 'Lycanroc']

for i in range (0, len(nombre)):
    poke = Pokemon(nombre[i].lower(), randint(1, 100), choice(tipo), choice(debilidades))
    a_nombres = insertar(a_nombres, [poke, poke.nombre])
    a_tipo = insertar(a_tipo, [poke, poke.tipo])
    a_numero = insertar(a_numero, [poke, poke.numero])
    
def orden_numero(raiz):
    if(raiz is not None):
        orden_numero(raiz.izq)
        print(raiz.informacion[1], raiz.informacion[0])
        orden_numero(raiz.der)
print('El listado de todos los pokemons ordenados por número es el siguiente:')
orden_numero(a_numero)

def busqueda_prox_poke(raiz, busqueda):
    if(raiz is not None):
        if(raiz.informacion[1][0:len(busqueda)] == busqueda):
            print(raiz.informacion[1])
        busqueda_prox_poke(raiz.izq, busqueda)
        busqueda_prox_poke(raiz.der, busqueda)

x = input('Introduzca el nombre parcial que desea buscar:')
print('El listado de los pokemons con ese nombre parcial es el siguiente:')
busqueda_prox_poke(a_nombres, x.lower())

def busqueda_prox_pokemon2(raiz, busqueda):
    if(raiz is not None):
        if(raiz.informacion[1][0:len(busqueda)] == busqueda):
            print(raiz.informacion[0].nombre)
        busqueda_prox_pokemon2(raiz.izq, busqueda)
        busqueda_prox_pokemon2(raiz.der, busqueda)

x = input('Introduzca el tipo de Pokemon que desea buscar:')
print('Todos los Pokemons de tipo', x, 'son los siguientes:')
busqueda_prox_pokemon2(a_tipo, x.lower())

def orden_numero2(raiz):
    if(raiz is not None):
        orden_numero2(raiz.izq)
        print(raiz.informacion[0])
        orden_numero2(raiz.der)

print('Lista en orden creciente en función del número asignado a cada Pokemon:')
orden_numero2(a_numero)

def orden_nombre(raiz):
    if(raiz is not None):
        orden_nombre(raiz.izq)
        print(raiz.informacion[0])
        orden_nombre(raiz.der)

print('Lista ordenada de forma creciente a nivel alfabético de los Pokemons:')
orden_nombre(a_nombres)

def nivel_nombre(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not vacia(cola)):
        nodo = atencion(cola)
        print(nodo.informacion[0])
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)

print('Lista en orden por nivel de los Pokemons:')
nivel_nombre(a_nombres)

def busqueda_prox_pokemon3(raiz, buscado):
    if(raiz is not None):
        if(raiz.informacion[0].debilidad[0:len(buscado)] == buscado):
            print(raiz.informacion[0].nombre)
        busqueda_prox_pokemon3(raiz.izq, buscado)
        busqueda_prox_pokemon3(raiz.der, buscado)

print('Debiles contra Jolteon: ')
busqueda_prox_pokemon3(a_nombres, 'Jolteon')

print('Debiles contra Lycanroc: ')
busqueda_prox_pokemon3(a_nombres, 'Lycanroc')

print('Debiles contra Tyrantrum: ')
busqueda_prox_pokemon3(a_nombres, 'Tyrantrum')

contador = 0

def orden_tipo(raiz, contador):
    if(raiz is not None):
        if raiz.informacion[0].tipo == 'fuego':
            contador += 1
        orden_tipo(raiz.izq, contador)
        print(raiz.informacion[0].nombre, raiz.informacion[0].tipo)
        orden_tipo(raiz.der, contador)
    return contador

print('Pokemons y su tipo:')
contador = orden_tipo(a_nombres, contador)
print('Cantidad de Pokemons del tipo fuego:',contador)