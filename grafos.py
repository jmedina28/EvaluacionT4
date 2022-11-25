from cola import Cola, vacia, atencion, arribo, nodoCola
from monticulos import MonticuloMinimo

def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]

class nodoArista():
    informacion, siguiente, peso = None, None, None

class nodoVertice():
    informacion, siguiente, visitado, adyacentes, datos = None, None, False, None, None