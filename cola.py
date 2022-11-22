class nodoCola():
    def __init__(self):
        self.dato = None
        self.siguiente = None

class Cola():

    def __init__(self):
        self.frente = None 
        self.ultimo = None
        self.nelementos = 0

def vacia(cola):
    return cola.nelementos == None