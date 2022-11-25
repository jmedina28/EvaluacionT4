
def lanzar():
    x = int(input("""Introduzca el número del ejercicio que desea ejecutar: 
    1. Ejercicio 1
    2. Ejercicio 2
    3. Ejercicio 3
    """))
    if(x == 1):
        from arbolbinario import nodoHuffman
        from sys import getsizeof
        from ejer1 import codificar, decodificar, gtabla, comparo, comparacionnodo
        dic = {'A': '00', '3': '01', '1': '100', 'T': '110',
       'F': '111', '0': '1010', 'M': '1011'}

        tabla = [['A', 0.2], ['F', 0.17], ['1', 0.13], [
            '3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]
        tabla.sort(key=comparo)
        bosque = []
        for i in tabla:
            nodo = nodoHuffman(i[0], i[1])
            bosque.append(nodo)
        while(len(bosque) > 1):
            elemento1 = bosque.pop(0)
            elemento2 = bosque.pop(0)
            nodo = nodoHuffman('', elemento1.valor+elemento2.valor)
            nodo.izq, nodo.der = elemento1, elemento2
            bosque.append(nodo)
            bosque.sort(key=comparacionnodo)
        gtabla(bosque[0])
        cadena = "TF103A0M"
        codificada = codificar(cadena, dic)
        print('La cadena codificada es la siguiente:' + str(codificada))
        getsizeof(codificada), getsizeof(b"1101111001010010010101011")
        decodificada = decodificar(codificada, bosque[0])
        print('La cadena decodificada es la siguiente:' + str(decodificada))
    elif(x == 2):
        import ejer2 