class nodoCola():
    def __init__(self):
        self.dato = None
        self.siguiente = None

class Cola():

    def __init__(self):
        self.primero = None 
        self.ultimo = None
        self.nelementos = 0

def vacia(cola):
    return cola.nelementos == None

def atencion(cola):
    aux = cola.primero.info
    cola.primero = cola.primero.sig
    if(cola.primero is None):
        cola.ultimo = None
    cola.nelementos -= 1
    return aux