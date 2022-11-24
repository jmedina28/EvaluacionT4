import random
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