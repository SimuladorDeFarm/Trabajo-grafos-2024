import networkx as nx
import matplotlib.pyplot as plt

def mostrar(G):
    
    #mostrar
    pos = nx.spring_layout(G) 
    nx.draw(G, with_labels=True, node_size=500, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Mostrar el grafo
    plt.show()


def prueba_grafo():


    G = nx.Graph()

    #agregar uno a la vez y si no existe los crea
    #G.add_edge(1, 2)
    #e = (1,2)
    #G.add_edge(*e)  # unpack edge tuple

    #agregar por conjunto
    G.add_edges_from([(1,2, {'weight': 2}),
    (1,8, {'weight': 5}),
    (2,3, {'weight': 3}),
    (2,9, {'weight': 1}),
    (3,4, {'weight': 5}),
    (4,9, {'weight': 3}),
    (4,5, {'weight': 3}),
    (5,6, {'weight': 1}),
    (6,9, {'weight': 2}),
    (6,7, {'weight': 3}),
    (7,8, {'weight': 4}),
    (8,9, {'weight': 4})])

    return G