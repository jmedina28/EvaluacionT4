from random import randint, choice
from arbolbinario import nodoArbol, insertar
from cola import Cola, vacia, atencion, arribo

arbol_numero = None
arbol_nombres = None
arbol_tipo = None

class Pokemon():
    
    def __init__(self, numero, nombre, tipo, debilidad):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.debilidad = debilidad

tipo = ['agua', 'fuego', 'tierra', 'electrico']
debilidad = ['agua', 'fuego', 'tierra', 'electrico', 'Jolteon','Tyrantum', 'Lycanroc']
nombre = ['Bulbasaur', 'Charmander', 'Pikachu', 'Ivysaur', 'Charmeleon', 'Raichu', 
'Venusaur', 'Charizard', 'Mewtwo', 'Squirtle', 'Wartortle', 'Blastoise', 'Mew', 'Eevee', 'Jolteon', 'Tyrantum', 'Lycanroc']

for i in range (0, len(nombre)):
    poke = Pokemon(nombre[i], randint(1, 100), choice(tipo), choice(debilidad))
    arbol_numero = insertar(arbol_numero, [poke, poke.numero])
    arbol_nombres = insertar(arbol_nombres, [poke, poke.nombre])
    arbol_tipo = insertar(arbol_tipo, [poke, poke.tipo])