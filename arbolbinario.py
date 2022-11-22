from cola import Cola, vacia, atencion, arribo

class nodoArbol(object):

    def __init__(self, info, nrr=None):
        self.izq, self.der = None, None
        self.info, self.nrr = info, nrr