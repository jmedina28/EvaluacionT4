from cola import Cola, vacia, atencion, arribo

class nodoArbol(object):
    # nrr significa numero de registro relativo
    def __init__(self, info, nrr=None):
        self.izq, self.der = None, None
        self.info, self.nrr = info, nrr

class nodoHuffman(object):
    
    def __init__(self, info, valor):
        self.izq, self.der = None, None
        self.info, self.valor = info, valor

def insertar(raiz, dato, nrr=None):
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.info <= dato):
            raiz.der = insertar(raiz.der, dato, nrr)
        else:
            raiz.izq = insertar(raiz.izq, dato, nrr)
    return raiz