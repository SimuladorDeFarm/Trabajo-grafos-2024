import networkx as nx
import matplotlib.pyplot as plt


def graficar_grafos(G, pesos):


    if pesos == True:
        #mostrar con pesos
        pos = nx.spring_layout(G) 
        nx.draw(G, with_labels=True, node_size=500, font_weight='bold')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        # Mostrar el grafo
        plt.show()

        
    else:
        
        nx.draw(G, with_labels=True, node_size=500, font_weight='bold')

        # Mostrar el grafo
        plt.show()
