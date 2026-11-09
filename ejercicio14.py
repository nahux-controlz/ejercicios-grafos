from graph import Graph
from casa_data import ambientes, distancias


def show_title(title):
    print()
    print(title)
    print('-' * len(title))


g = Graph(is_dir=False)

#A
for ambiente in ambientes:
    g.add_vertex(ambiente)

#B
for distancia in distancias:
    g.add_edge(distancia['metros'], distancia['origen'], distancia['destino'])

print('EJERCICIO 14 - AMBIENTES DE UNA CASA')
print(f'Grafo no dirigido con {len(g)} ambientes y {len(distancias)} conexiones (distancias en metros)')

show_title('a y b) Ambientes y sus conexiones')
con_cinco = []
minimo = None
for ambiente in ambientes:
    pos = g.search(ambiente, 'value')
    edges = g[pos].edges
    if len(edges) == 5:
        con_cinco.append(ambiente)
    if minimo is None or len(edges) < minimo:
        minimo = len(edges)
    detalle = []
    for edge in edges:
        detalle.append(f'{edge.destination} ({edge.weight} m)')
    print(f'  {ambiente:<15}{len(edges)} aristas: {", ".join(detalle)}')
print()
print(f'Cada ambiente tiene como mínimo {minimo} aristas y los que tienen 5 son: {" y ".join(con_cinco)}')

#C
show_title('c) Árbol de expansión mínima (Kruskal)')
min_tree = g.kruskal(ambientes[0])
metros_totales = 0
print(f'  {"Ambiente":<15}{"Ambiente":<15}{"Metros":>6}')
for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'  {origin:<15}{destination:<15}{weight:>6}')
    metros_totales += int(weight)
print(f'  Se necesitan {metros_totales} metros de cable para conectar todos los ambientes')

#D
show_title('d) Camino más corto desde la habitación 1 hasta la sala de estar')
resultado = g.shortest_path('habitación 1', 'sala de estar')
if resultado is not None:
    camino, metros = resultado
    print(f'  Camino: {" -> ".join(camino)}')
    print(f'  Se necesitan {metros} metros de cable de red para conectar el router con el Smart TV')
else:
    print('  No existe camino entre la habitación 1 y la sala de estar')
