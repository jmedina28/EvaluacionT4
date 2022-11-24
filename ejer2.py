from random import randint, choice
from cola import Cola, vacia, atencion, arribo
from arbolbinario import nodoArbol, insertar

a_nombres = None
a_tipo = None
a_numero = None

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
nombre = ['Bulbasaur', 'Charmander', 'Pikachu', 'Ivysaur', 'Charmeleon', 'Raichu', 'Venusaur', 
'Charizard', 'Mewtwo', 'Squirtle', 'Wartortle', 'Blastoise', 'Mew', 'Eevee', 'Jolteon', 'Tyrantum', 'Lycanroc']

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