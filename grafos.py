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

class Grafo():

    def __init__(self, dirigido=True):
        self.__inicio = None
        self.__tamanio = 0
        self.__dirigido = dirigido


    def insertar_vertice(self, dato, campo=None, datos=None):
        nodo = nodoVertice()
        nodo.informacion = dato
        nodo.datos = datos
        nodo.adyacentes = Arista()

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

    def insertar_arista(self, origen, destino, peso):
        vert_origen = self.busqueda_vertice(origen)
        vert_destino = self.busqueda_vertice(destino)
        if(vert_origen and vert_destino):
            vert_origen.adyacentes.insertar_arista(destino, peso)
            if not self.__dirigido:
                vert_destino.adyacentes.insertar_arista(origen, peso)

    def tamanio(self):
        return self.__tamanio

    def bar_vertice(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.informacion)
            aux = aux.siguiente
    
    def marcar_no_visitado(self):
        aux = self.__inicio
        while(aux is not None):
            aux.visitado = False
            aux = aux.siguiente

    def busqueda_vertice(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.informacion, campo) == buscado):
                pos = aux
            aux = aux.siguiente

        return pos

    def bar_no_visitado(self):
        aux = self.__inicio
        while(aux is not None):
            if not aux.visitado:
                print(aux.informacion)
            aux = aux.siguiente

    def eliminar_vertice(self, clave, campo=None):
        dato = None
        if self.__inicio is not None:
            if(criterio(self.__inicio.informacion, campo) == clave):
                dato = self.__inicio.informacion
                self.__inicio = self.__inicio.siguiente
            else:
                anterior = self.__inicio
                actual = self.__inicio.siguiente
                while(actual is not None and criterio(actual.informacion, campo) != clave):
                    anterior = anterior.siguiente
                    actual = actual.siguiente

                if(actual is not None):
                    dato = actual.informacion
                    anterior.siguiente = actual.siguiente
            if dato:
                self.__tamanio -= 1 

            aux = self.__inicio
            while(aux is not None):
                aux.adyacentes.eliminar_arista(clave)
                aux = aux.siguiente
            
        return dato

    def eliminar_arista(self, origen, destino):
        vert_origen = self.busqueda_vertice(origen)
        valor, peso = None, None
        if vert_origen:
            valor, peso = vert_origen.adyacentes.eliminar_arista(destino)
            if valor:
                vert_destino = self.busqueda_vertice(destino)
                vert_destino.adyacentes.eliminar_arista(origen)

        return peso

    def obtener_elemento_vertice(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.siguiente
            return aux.informacion            
        else:
            return None
    
    def es_adyacente(self, origen, destino):
        resultado = False
        vert_origen = self.busqueda_vertice(origen)
        if vert_origen:
            aux = vert_origen.adyacentes.busqueda_arista(destino)
            if aux:
                resultado = True
        return resultado

    def adyacentes(self, origen):
        vert_origen = self.busqueda_vertice(origen)
        if vert_origen:
            vert_origen.adyacentes.bar_aristas()

    def existe_paso(self, origen, destino):
        resultado = False
        vert_origen = self.busqueda_vertice(origen)
        if not vert_origen.visitado:
            vert_origen.visitado = True
            print(vert_origen.informacion)
            adyacentes = vert_origen.adyacentes.get_inicio()
            while adyacentes is not None and not resultado:
                if adyacentes.informacion == destino:
                    resultado = True
                else:
                    resultado = self.existe_paso(adyacentes.informacion, destino)
                adyacentes = adyacentes.siguiente
        return resultado

    def bar_profundidad(self, origen):
        vert_origen = self.busqueda_vertice(origen)
        if not vert_origen.visitado:
            print(vert_origen.informacion)
            vert_origen.visitado = True
            adyacentes = vert_origen.adyacentes.get_inicio()
            while adyacentes is not None:
                self.bar_profundidad(adyacentes.informacion)
                adyacentes = adyacentes.siguiente
    
    def bar_amplitud(self, origen):
        self.marcar_no_visitado()
        vert_origen = self.busqueda_vertice(origen)
        pendientes = Cola()
        if not vert_origen.visitado:
            vert_origen.visitado = True
            pendientes.arribo(vert_origen)
            while not pendientes.vacia():
                vertice_actual = pendientes.atencion()
                print(vertice_actual.informacion)
                adyacentes = vertice_actual.adyacentes.get_inicio()
                while adyacentes is not None:
                    adyacente = self.busqueda_vertice(adyacentes.informacion)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        pendientes.arribo(adyacente)
                    adyacentes = adyacentes.siguiente

    def kruskal(self):
        def buscar_en_bosque(bosque, buscado):
            for arbol in bosque:
                if buscado in arbol:
                    return arbol
        bosque = []
        aristas = MonticuloMinimo()
        aux = self.__inicio
        while aux is not None:
            bosque.append(str(aux.informacion))
            adyacentes = aux.adyacentes.get_inicio()
            while adyacentes is not None:
                aristas.arribo([aux.informacion, adyacentes.informacion], adyacentes.peso)
                adyacentes = adyacentes.siguiente
            aux = aux.siguiente

        while len(bosque) > 1 and aristas.tamanio > 0:
            arista, peso = aristas.quitar()
            origen = buscar_en_bosque(bosque, arista[0])
            destino = buscar_en_bosque(bosque, arista[1])
            if origen is not None and destino is not None:
                if origen != destino:
                    bosque.remove(origen)
                    bosque.remove(destino)
                    if ';' not in origen and ';' not in destino:
                        bosque.append(f'{origen};{destino};{peso}')
                    elif ';' in origen and ';' not in destino:
                        bosque.append(origen+f'-{arista[0]};{destino};{peso}')
                    elif ';' not in origen and ';' in destino:
                        bosque.append(destino+f'-{origen};{arista[1]};{peso}')
                    else:
                        bosque.append(origen+'-'+destino+f'-{arista[0]};{arista[1]};{peso}')

        return bosque

    def dijkstra(self, origen):
        from math import inf
        no_visitado = MonticuloMinimo()
        camino = {}

        aux = self.__inicio
        while aux is not None:
            if aux.informacion == origen:
                no_visitado.agregar([aux, None], 0)
            else:
                no_visitado.agregar([aux, None], inf)
            aux = aux.siguiente

        while no_visitado.tamanio > 0:
            elemento, peso = no_visitado.quitar()
            vertice, previo = elemento[0], elemento[1]
            camino[vertice.informacion] = {'previo': previo, 'peso': peso}
            adyacentes = vertice.adyacentes.get_inicio()
            while adyacentes is not None:
                buscado = no_visitado.buscar(adyacentes.informacion)
                if buscado:
                    if no_visitado.vector[buscado][1] > peso + adyacentes.peso:
                        no_visitado.vector[buscado][1] = peso + adyacentes.peso
                        no_visitado.vector[buscado][0][1] = vertice.informacion
                        no_visitado.flotar(buscado)
                adyacentes = adyacentes.siguiente
        return camino

    def camino(self, resultados, origen, destino):
        camino_mas_corto = {'camino': [],
                            'costo': None}
        if destino in resultados:
            vert_destino = resultados[destino]
            camino_mas_corto['costo'] = vert_destino['peso']
            camino_mas_corto['camino'].append(destino)
            while vert_destino['previo'] is not None:
                camino_mas_corto['camino'].append(vert_destino['previo'])
                vert_destino = resultados[vert_destino['previo']]
            camino_mas_corto['camino'].reverse()
        return camino_mas_corto