from data_base import *
from graph import *
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print(30 * '-')

europe_map = nx.Graph()

for country, coordinates in country_coordinates.items():
    europe_map.add_node(country, pos=coordinates)
    
for country, neighbors in countries.items():
    for neighbor, weight in neighbors:
        europe_map.add_edge(country, neighbor, weight=weight)
        europe_map.add_edge(neighbor, country, weight=weight)

graph = Graph(countries)
graph.CountVertices()
graph.CountEdges()

plt.figure(figsize=(15, 12))
pos = nx.get_node_attributes(europe_map, 'pos')
nx.draw(europe_map, pos, with_labels=True, node_size=600, node_color='lightblue', font_size=6, font_weight='bold', edge_color='gray', width=0.5)

plt.savefig("europe_map.png")

#------------------------------------------------------------------------------------------------------------
print(10 * ' ' + "Задание 1\n" + '-' * 30)

planar_map = nx.Graph()

for country, neighbors in countries.items():
    for neighbor in neighbors:
        planar_map.add_edge(country, neighbor[0])

pos = nx.planar_layout(planar_map)

plt.figure(figsize=(15, 12))
nx.draw(planar_map, pos, with_labels=True, node_size=200, node_color='lightblue', font_size=6, font_weight='bold', edge_color='gray', width=0.5)

plt.savefig("planar_graph.png")

print(f"Граф получился планарным. Посмотрим утверждения, необходимые для планарности:\n1. Для любого связного планарного графа выполняется неравенство m <= 3n - 6. Подставим и проверим: {graph.GetEdges()} <= {3 * graph.GetVertices() - 6}")
print(f"2. В любом планарном графе есть вершина, степень которой не превосходит 5.")
print(30 * '-')

#------------------------------------------------------------------------------------------------------------
print(10 * ' ' + "Задание 2\n" + '-' * 30)

connected_components = list(nx.connected_components(europe_map))
largest_component = max(connected_components, key=len)
temp_graph = europe_map.subgraph(largest_component).copy()

print(f"Количество рёбер в графе: {graph.GetEdges()}")

print(f"Количество вершин в графе: {graph.GetVertices()}")

graph.CountMinDeg()
print(f"Минимальная степень вершины в графе: {graph.GetMinDeg()}")

graph.CountMaxDeg()
print(f"Максимальная степень вершины в графе: {graph.GetMaxDeg()}")

radius = nx.radius(temp_graph)
graph.SetRadius(radius)
print(f"Радиус: {graph.GetRadius()}")

diameter = nx.diameter(temp_graph)
graph.SetDiameter(diameter)
print(f"Диаметр: {graph.GetDiameter()}")

centers = nx.center(temp_graph)
graph.SetCenter(centers)
centers_string = ', '.join(graph.GetCenter())
print(f"Центры: {centers_string}")

components = nx.number_connected_components(europe_map)
graph.SetComponents(components)
graph.SetCyclomaticNumber(graph.GetEdges() - graph.GetVertices() + graph.GetComponents())
print(f"Цикломатическое число графа: {graph.GetCyclomaticNumber()}")

print(30 * '-')
#------------------------------------------------------------------------------------------------------------
print(10 * ' ' + "Задание 3\n" + '-' * 30)

color_graph = europe_map

colors = nx.coloring.greedy_color(color_graph, strategy='largest_first', interchange=True)

graph.SetChromaticNumber(max(colors.values()) + 1)

print(f"Хроматическое число: {graph.GetChromaticNumber()}")

plt.figure(figsize=(15, 12))
pos = nx.get_node_attributes(color_graph, 'pos')
nx.draw(color_graph, pos, with_labels=True, node_size=600, node_color=list(colors.values()), cmap=plt.cm.rainbow, font_size=6, font_weight='bold', edge_color='gray', width=0.5)
plt.savefig("color_graph.png")

print(30 * '-')
#------------------------------------------------------------------------------------------------------------
print(10 * ' ' + "Задание 4\n" + '-' * 30)

all_components = list(nx.connected_components(europe_map))
for i, component in enumerate(all_components, start=1):
    print(f"Компонента связности {i}: {', '.join(component)}")

print(30 * '-')
#------------------------------------------------------------------------------------------------------------
print(10 * ' ' + "Задание 5\n" + '-' * 30)

graph.SetPendantNodes([node for node in europe_map.nodes() if europe_map.degree[node] == 1])

print(f"Количество висячих вершин: {len(graph.GetPendantNodes())}")
print("Висячие вершины:")
for node in graph.GetPendantNodes():
    print(node)
    
print(30 * '-')
#------------------------------------------------------------------------------------------------------------
print(10 * ' ' + "Задание 6\n" + '-' * 30)

print("Граф двудольный тогда и только тогда, когда в нем нет нечетных циклов.\nВозьмем, например, Франция-Испания-Андора. Это нечетный цикл.\nГраф не двудольный!")

print(30 * '-')
#------------------------------------------------------------------------------------------------------------
print(10 * ' ' + "Задание 9\n" + '-' * 30)

print("Граф не может быть Гамильтонов, так как имеются висячие вершины. \nНапример: Дания, Ватикан, Монако, Португалия и Сан-Марино")

print(30 * '-')
#------------------------------------------------------------------------------------------------------------
print(10 * ' ' + "Задание 10\n" + '-' * 30)

if nx.is_eulerian(temp_graph):
    eulerian_cycle = list(nx.eulerian_circuit(temp_graph))
    shortest_closed_path = [eulerian_cycle[i][0] for i in range(len(eulerian_cycle))] + [eulerian_cycle[0][0]]
    print("Кратчайший замкнутый путь U:", shortest_closed_path)
else:
    print("Граф не имеет эйлерова цикла.")

print(30 * '-')
#------------------------------------------------------------------------------------------------------------
print(10 * ' ' + "Задание 11\n" + '-' * 30)

connected_components = list(nx.connected_components(europe_map))
largest_component = max(connected_components, key=len)

subgraph = europe_map.subgraph(largest_component).copy()

minimum_spanning_tree = nx.minimum_spanning_tree(subgraph)

plt.figure(figsize=(15, 12))
pos = nx.spring_layout(subgraph)
nx.draw_networkx_edges(minimum_spanning_tree, pos, edge_color='blue', width=1.0, alpha=0.7)
nx.draw_networkx_nodes(subgraph, pos, node_size=150, node_color='lightblue')
nx.draw_networkx_labels(subgraph, pos, font_size=5, font_weight='bold')

plt.savefig("minimum_spanning_tree.png")

print("См. граф в директории проекта.")

print(30 * '-')
#------------------------------------------------------------------------------------------------------------
print(10 * ' ' + "Задание 12\n" + '-' * 30)

max_clique = max(nx.find_cliques(europe_map), key=len)
print("Максимальная клика в графе:", ", ".join(max_clique), "\nДлина = 4")

print(30 * '-')
#------------------------------------------------------------------------------------------------------------
print(10 * ' ' + "Задание 13\n" + '-' * 30)

def PruferCode(graph):
    max_spanning_tree = nx.minimum_spanning_tree(graph)
    tree = nx.Graph(max_spanning_tree.edges())
    prufer = []
    while len(tree) > 2:
        leaf_candidates = [node for node in tree if tree.degree[node] == 1]
        if not leaf_candidates:
            break
        leaf = min(leaf_candidates)
        neighbor = next(iter(tree.neighbors(leaf)))
        prufer.append(neighbor)
        tree.remove_node(leaf)
    return prufer

prufer_code = PruferCode(europe_map)
print("Код Прюфера для максимального остовного дерева:", *prufer_code, "\nДлина:", len(prufer_code))

