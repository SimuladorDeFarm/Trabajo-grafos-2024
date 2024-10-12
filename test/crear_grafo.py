import networkx as nx
import matplotlib.pyplot as plt


def vertices():
    A = nx.Graph()
    B = nx.Graph()
    C = nx.Graph()
    #agregar un nodo
    A.add_node(1 )

    #agregar varios nodos
    B.add_nodes_from([2, 3])


    #agregar nodos con atributos
    C.add_nodes_from([(4, {"color": "red"}), (5, {"color": "green"}), (6, {"color": "yelow"})])

    #convinar nodos
    D = nx.path_graph(10)
    A.add_nodes_from(D) 
    A.add_node(D)


    #imprimir datos simplificado
    print(C)


    #imprimir los datos
    #print(C.nodes(data=True))
    #nx.draw(C)
    #G = nx.petersen_graph()
    # Dibujar el grafo
    nx.draw(B, with_labels=True, node_size=800, font_weight='bold')

    # Mostrar el grafo
    plt.show()


def edges():

    G = nx.Graph()

    #agregar uno a la vez y si no existe los crea
    #G.add_edge(1, 2)
    #e = (1,2)
    #G.add_edge(*e)  # unpack edge tuple

    #agregar por conjunto
    G.add_edges_from([(1,2),(2,3), (2,10), (3,7), (7,8),(8,9), (3,4), (4,5), (5,6)])

    #eliminar contenido del nodo
    #G.clear()

    print(G.number_of_nodes())
    print(G.number_of_edges())


    nx.draw(G, with_labels=True, node_size=500, font_weight='bold')

    # Mostrar el grafo
    plt.show()

edges()


