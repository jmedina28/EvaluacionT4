from arbolbinario import insertar, barridopostorden, nodoHuffman
from sys import getsizeof

dic = {'A': '00', '3': '01', '1': '100', 'T': '110', 
    'F': '111','0': '1010', 'M': '1011'}

tabla = [['A', 0.2], ['F', 0.17], ['1', 0.13], ['3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]

def comparo(elemento):
    return elemento[1]

tabla.sort(key=comparo)

def comparacionnodo(elemento):
    return elemento.valor

bosque = []

for i in tabla:
    nodo = nodoHuffman(i[0], i[1])
    bosque.append(nodo)

for i in bosque:
    print(i.info, i.valor)

while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = nodoHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq, nodo.der = elemento1, elemento2
    bosque.append(nodo)
    bosque.sort(key=comparacionnodo)

def gtabla(raiz, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            print(raiz.info, cadena)
        else:
            cadena += '0'
            gtabla(raiz.izq, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            gtabla(raiz.der, cadena)

gtabla(bosque[0])

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
            decodificada += raiz_aux.info
            raiz_aux = arbol_huffman
        decodificada
    return decodificada

def codificar(cadena, dic):
    codificada = ''
    for caracter in cadena:
        codificada += dic[caracter]
    return codificada

if __name__ == "__main__":
    cadena = "TF103A0M"
    codificada = codificar(cadena, dic)
    print(codificada)
    print(getsizeof(codificada), getsizeof(b"1101111001010010010101011"))
    print('La cadena decodificada es la siguiente:')
    decodificada = decodificar(codificada, bosque[0])
    print(decodificada)