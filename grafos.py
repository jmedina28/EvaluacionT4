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

class Arista():
    
    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0

    def get_inicio(self):
        return self.__inicio

    def insertar_arista(self, dato, peso, campo=None):
        nodo = nodoArista()
        nodo.informacion = dato
        nodo.peso = peso

        if(self.__inicio is None or criterio(nodo.informacion, campo) < criterio(self.__inicio.informacion, campo)):
            nodo.siguiente = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.siguiente
            while(actual is not None and criterio(nodo.informacion, campo) > criterio(actual.informacion, campo)):
                anterior = anterior.siguiente
                actual = actual.siguiente
            nodo.siguiente = actual
            anterior.siguiente = nodo

        self.__tamanio += 1

    def tamanio(self):
        return self.__tamanio

    def barrido_aristas(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.informacion, aux.peso)
            aux = aux.siguiente
    
    def busqueda_arista(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.informacion, campo) == buscado):
                pos = aux
            aux = aux.siguiente

        return pos

    def eliminar_arista(self, clave, campo=None):
        dato, peso = None, None
        if self.__inicio is not None:
            if(criterio(self.__inicio.informacion, campo) == clave):
                dato = self.__inicio.informacion
                peso = self.__inicio.peso
                self.__inicio = self.__inicio.siguiente
            else:
                anterior = self.__inicio
                actual = self.__inicio.siguiente
                while(actual is not None and criterio(actual.informacion, campo) != clave):
                    anterior = anterior.siguiente
                    actual = actual.siguiente

                if(actual is not None):
                    dato = actual.informacion
                    peso = actual.peso
                    anterior.siguiente = actual.siguiente
            if dato:
                self.__tamanio -= 1 

        return dato, peso 

    def obtener_elemento_arista(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.siguiente
            return aux.informacion            
        else:
            return None