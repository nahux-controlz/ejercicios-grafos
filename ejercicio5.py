from graph import Graph
from red_data import equipos, conexiones

TIPOS = ['pc', 'notebook', 'servidor', 'router', 'switch', 'impresora']
COMPUTADORAS = ['pc', 'notebook']


def show_title(title):
    print()
    print(title)
    print('-' * len(title))


def show_sequence(label, values, width=95):
    # muestra los vertices separados por flechas y corta las lineas largas
    line = label + values[0]
    for value in values[1:]:
        if len(line) + len(value) + 4 > width:
            print(line)
            line = ' ' * len(label) + '-> ' + value
        else:
            line += ' -> ' + value
    print(line)


def show_traversals(graph):
    for notebook in ['Red Hat', 'Debian', 'Arch']:
        print()
        print(f'Desde {notebook}:')
        show_sequence('  Profundidad: ', graph.deep_list(notebook))
        show_sequence('  Amplitud:    ', graph.amplitude_list(notebook))


def show_paths(graph, origins, destination):
    # muestra el camino mas corto de cada origen al destino y devuelve el de menor costo
    best = None
    print(f'  {"Desde":<10}{"Costo":>5}   Camino')
    for origin in origins:
        camino, costo = graph.shortest_path(origin, destination)
        print(f'  {origin:<10}{costo:>5}   {" -> ".join(camino)}')
        if best is None or costo < best[1]:
            best = [origin, costo]
    return best


def type_of(graph, value):
    pos = graph.search(value, 'value')
    return graph[pos].other_values


g = Graph(is_dir=False)

#A
for equipo in equipos:
    g.add_vertex(equipo['nombre'], equipo['tipo'])

for conexion in conexiones:
    g.add_edge(conexion['peso'], conexion['origen'], conexion['destino'])

print('EJERCICIO 5 - ESQUEMA DE RED')
print(f'Grafo no dirigido con {len(g)} equipos y {len(conexiones)} conexiones')

show_title('a) Equipos de la red según su tipo')
for tipo in TIPOS:
    nombres = []
    for vertex in g:
        if vertex.other_values == tipo:
            nombres.append(vertex.value)
    print(f'  {tipo:<11}{", ".join(nombres)}')

#B
show_title('b) Barridos en profundidad y amplitud desde las notebooks')
show_traversals(g)

#C
show_title('c) Camino más corto para imprimir desde Manjaro, Red Hat y Fedora')
show_paths(g, ['Manjaro', 'Red Hat', 'Fedora'], 'Impresora')

#D
show_title('d) Árbol de expansión mínima (Kruskal)')
min_tree = g.kruskal(equipos[0]['nombre'])
peso_total = 0
print(f'  {"Equipo":<12}{"Equipo":<12}{"Peso":>5}')
for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'  {origin:<12}{destination:<12}{weight:>5}')
    peso_total += int(weight)
print(f'  Peso total del árbol: {peso_total}')

#E
show_title('e) PC con el camino más corto hasta el servidor Guaraní')
pcs = []
for vertex in g:
    if vertex.other_values == 'pc':
        pcs.append(vertex.value)
mejor = show_paths(g, pcs, 'Guaraní')
print(f'  Respuesta: {mejor[0]} (costo {mejor[1]})')

#F
show_title('f) Computadora del Switch 1 con el camino más corto al servidor MongoDB')
computadoras = []
pos_switch = g.search('Switch 1', 'value')
for edge in g[pos_switch].edges:
    if type_of(g, edge.destination) in COMPUTADORAS:
        computadoras.append(edge.destination)
mejor = show_paths(g, computadoras, 'MongoDB')
print(f'  Respuesta: {mejor[0]} (costo {mejor[1]})')

#G
show_title('g) Impresora conectada al Router 2: se repite el punto b')
peso = g.delete_edge('Impresora', 'Switch 1').weight
g.add_edge(peso, 'Impresora', 'Router 2')
print(f'Se quitó la conexión Impresora - Switch 1 y se agregó Impresora - Router 2 (peso {peso}).')
show_traversals(g)
