from arbolbinario import nodoHuffman
from sys import getsizeof


def comparo(elemento):
    return elemento[1]


def comparacionnodo(elemento):
    return elemento.valor


def gtabla(raiz, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            print(raiz.informacion, cadena)
        else:
            cadena += '0'
            gtabla(raiz.izq, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            gtabla(raiz.der, cadena)


def decodificar(cadena, arbol_huffman):
    decodificada, pos = '', 0
    raiz_aux = arbol_huffman
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            decodificada += raiz_aux.informacion
            raiz_aux = arbol_huffman
        decodificada
    return decodificada


def codificar(cadena, dic):
    codificada = ''
    for caracter in cadena:
        codificada += dic[caracter]
    return codificada