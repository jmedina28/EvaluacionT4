from tda.cola import Cola, vacia, atencion, arribo

class nodoArbol(object):
    # nrr significa numero de registro relativo
    def __init__(self, informacion, nrr=None):
        self.izq, self.der = None, None
        self.informacion, self.nrr = informacion, nrr
        self.altura = 0

class nodoHuffman(object):
    
    def __init__(self, informacion, valor):
        self.izq, self.der = None, None
        self.informacion, self.valor = informacion, valor

def insertar(raiz, dato, nrr=None):
    
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.informacion[1] > dato[1]):
            raiz.izq = insertar(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar(raiz.der, dato, nrr)
    raiz = balanceo(raiz)
    actualtura(raiz)
    return raiz

def recorrido(raiz):

    if(raiz is not None):
        recorrido(raiz.izq)
        print(raiz.informacion)
        recorrido(raiz.der)

def balanceo(raiz):
    
    if(raiz is not None):
        if(altura(raiz.izq)-altura(raiz.der) == 2):
            if(altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotacion_simple(raiz, True)
            else:
                raiz = rotacion_doble(raiz, True)
        elif(altura(raiz.der)-altura(raiz.izq) == 2):
            if(altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotacion_simple(raiz, False)
            else:
                raiz = rotacion_doble(raiz, False)
    return raiz

def altura(raiz):
    
    if(raiz is None):
        return -1
    else:
        return raiz.altura

def actualtura(raiz):

    if(raiz is not None):
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1
    
def rotacion_simple(raiz, control):
    
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualtura(raiz)
    actualtura(aux)
    raiz = aux
    return raiz

def rotacion_doble(raiz, control):
    
    if control:
        raiz.izq = rotacion_simple(raiz.izq, False)
        raiz = rotacion_simple(raiz, True)
    else:
        raiz.der = rotacion_simple(raiz.der, True)
        raiz = rotacion_simple(raiz, False)
    return raiz