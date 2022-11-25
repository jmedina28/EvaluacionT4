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