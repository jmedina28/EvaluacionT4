class nodoCola():
    def __init__(self):
        self.informacion = None
        self.siguiente = None

class Cola():

    def __init__(self):
        self.primero = None 
        self.ultimo = None
        self.nelementos = 0

def vacia(cola):
    return cola.nelementos == None

def atencion(cola):
    aux = cola.primero.informacion
    cola.primero = cola.primero.siguiente
    if(cola.primero is None):
        cola.ultimo = None
    cola.nelementos -= 1
    return aux

def arribo(cola, dato):
    nodo = nodoCola()
    nodo.informacion = dato
    if(cola.ultimo is None):
        cola.primero = nodo
    else:
        cola.ultimo.siguiente = nodo
    cola.ultimo = nodo
    cola.nelementos += 1