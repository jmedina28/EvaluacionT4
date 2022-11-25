from grafos import Grafo

grafo = Grafo(dirigido = False)

grafo.insertar_vertice("E", datos ={"pais": "Grecia", "tipo":"natural"})
grafo.insertar_vertice("T", datos ={"pais":"Turquia", "tipo":"natural"})
grafo.insertar_vertice("M", datos ={"pais":"Turquia", "tipo":"natural"})
grafo.insertar_vertice("J", datos ={"pais":"Irak", "tipo":"natural"})
grafo.insertar_vertice("C", datos ={"pais":"Grecia", "tipo":"natural"})
grafo.insertar_vertice("F", datos ={"pais":"Egipto", "tipo":"natural"})
grafo.insertar_vertice("P", datos ={"pais":"Egipto", "tipo":"natural"})

grafo.insertar_arista('E', 'T', 6)
grafo.insertar_arista('E', 'M', 3)
grafo.insertar_arista('M', 'J', 8)
grafo.insertar_arista('J', 'C', 2)
grafo.insertar_arista('J', 'F', 4)
grafo.insertar_arista('P', 'M', 9)

grafo.insertar_vertice('W', datos={'pais': 'Rumania','tipo': 'arquitectonica'})
grafo.insertar_vertice('Z', datos={'pais': 'Gran Bretania','tipo': 'arquitectonica'})
grafo.insertar_vertice('L', datos={'pais': 'Rusia','tipo': 'arquitectonica'})
grafo.insertar_vertice('X', datos={'pais': 'Espania','tipo': 'arquitectonica'})
grafo.insertar_vertice('R', datos={'pais': 'Estonia','tipo': 'arquitectonica'})
grafo.insertar_vertice('K', datos={'pais': 'Egipto','tipo': 'arquitectonica'})

grafo.insertar_arista('W', 'L', 6)
grafo.insertar_arista('W', 'Z', 6)
grafo.insertar_arista('Z', 'L', 7)
grafo.insertar_arista('L', 'X', 4)
grafo.insertar_arista('L', 'K', 4)
grafo.insertar_arista('K', 'R', 9)

paises = grafo.contar_maravillas()
for pais in paises:
    print(pais, paises[pais])

a_min = grafo.kruskal()

a_min = a_min[0].split('-')
peso_total = 0
for nodo in a_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print(f"El peso total es: {peso_total}")

if grafo.existe_paso('T', 'E'):
    resultados1 = grafo.dijkstra('T')
    camino = grafo.camino(resultados1, 'T', 'E')
    print(camino)
else:
    print('no se puede llega de T a E')

grafo.eliminar_arista('E', 'M')
grafo.eliminar_vertice('M')
grafo.bar_profundidad('J')
grafo.bar_profundidad('T')
print('------------------------------------------')
grafo.bar_profundidad('P')
grafo.bar_no_visitado()
grafo.adyacentes('U')
print(grafo.es_adyacente('U', 'E'))
print(grafo.es_adyacente('P', 'U'))