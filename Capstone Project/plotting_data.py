"""

@author: Sandy Auttelet

"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def plot_graph(graph,source,sink,n,path,title=None,labels=None):
    """
    Plots arbitrary circular graph wuth optimal path labels

    Parameters
    ----------
    graph : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html
    source : string
        origin point node label
    sink : string
        ending point node label
    n : int
        number of nodes
    path : list of strings
        node labels for optimal path
    title : string, optional
        Title of plot. The default is None

    Returns
    -------
    None. Prints plot for graph. Node labeled source colored pink (#FF19FF),
    sink node colored cyan (#B3FFFF), and other nodes in optimal path colored
    green (#49AF64). All nodes not in path colored red (#FE3F1C).

    """
    fig, ax = plt.subplots()
    fig.suptitle(title, fontsize='xx-large')
    pos = nx.circular_layout(graph)
    V = list(pos)

    node_size = 2000
    edgecolors = 'black'

    node_color = []
    for i in range(n):
        node_color.append('#FE3F1C')
        for j in range(len(path)):
            if chr(i+65) == source:
                node_color[i] = '#FF19FF'
                break;
            if chr(i+65) == sink:
                node_color[i] = '#B3FFFF'
                break;
            if chr(i+65) == path[j] and chr(i+65) != source and chr(i+65) != sink:
                node_color[i] = '#49AF64'
                break;
    


    nx.draw_networkx(graph, ax=ax, pos=pos, nodelist=V, edgelist=[],
                 node_color=node_color, edgecolors=edgecolors,
                 node_size=node_size)
    nx.draw_networkx_edges(graph, ax=ax, pos=pos, edgelist=graph.edges,
                       node_size=node_size)
    
    if labels != None:
        nx.draw_networkx_edge_labels(graph, ax=ax, pos=pos,font_size='xx-large')
    ax.axis('off')
    #plt.savefig('optimal_path.png', dpi=400)

