import networkx as nx
import matplotlib.pyplot as plt


#grafica un grafo con o sin peso; pesos = True or False
def graficar_grafos(G, pesos):

    #si es que tiene peso
    if pesos == True:
        #mostrar con pesos
        pos = nx.spring_layout(G) 
        nx.draw(G, with_labels=True, node_size=500, font_weight='bold')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        # Mostrar el grafo
        plt.show()

    #si es que no tiene peso    
    else:
        
        #imprime grafo sin pesos
        nx.draw(G, with_labels=True, node_size=500, font_weight='bold')

        # Mostrar el grafo
        plt.show()
