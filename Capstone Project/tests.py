"""

@author: Sandy Auttelet

"""


import graph_2D as g2
import networkx as nx
import plotting_data as pd


test_distance_data = [[0.,  2.9, 3.2, 4.2, 0.,  0.,  0. ],\
 [2.9, 0.,  0.,  2.3, 0.,  4.1, 0. ],\
 [3.2, 0.,  0.,  2.1, 3.2, 0.,  0. ],\
 [4.2, 2.3, 2.1, 0.,  3.7, 2.4, 4.2],\
 [0.,  0.,  3.2, 3.7, 0.,  0.,  2.9],\
 [0.,  4.1, 0.,  2.4, 0.,  0.,  3. ],\
 [0.,  0.,  0.,  4.2, 2.9, 3.,  0. ]]

test_delay_data = [[0., 0.021, 0.042, 0.033, 0., 0., 0.],\
 [0.021, 0., 0., 0.03, 0., 0.011, 0.],\
 [0.042, 0., 0., 0.042, 0.013, 0., 0.],\
 [0.033, 0.03, 0.042, 0., 0.019, 0.008, 0.057],\
 [0., 0., 0.013, 0.019, 0., 0., 0.01],\
 [0., 0.011, 0., 0.008, 0., 0., 0.028],\
 [0., 0., 0., 0.057, 0.01, 0.028, 0.]]

    
def test_data_similarity(graph1,graph2):
    """
    Tests if two graphs have the same structure.

    Parameters
    ----------
    graph1 : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html
    graph2 : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html

    Returns
    -------
    v : bool
        True if two graphs have same structure else false with printed warnings.

    """
    v = True
    nodes2 = list(graph2.nodes())
    nodes1 = list(graph1.nodes())
    if len(nodes1) != len(nodes2):
        v = False
        print("The two graphs do not have the same number of nodes and thus a weighted graph cannot be created.")
        return v
    edges2 = list(graph2.edges())
    edges1 = list(graph1.edges())
    for i in range(len(nodes1)):
        if nodes1[i] != nodes2[i]:
            print("Warning: The two graphs do not have the same ordered node labels.")
            if edges1[i] != edges2[i]:
                print("Warning: The two graphs do not have the same ordered edge labels.")
        if len(edges1) != len(edges2):
            v = False
            print("The two graphs do not have the same number of edges and thus a weighted graph cannot be created.")
            if edges1[i] != edges2[i]:
                print("Warning: The two graphs do not have the same ordered edge labels")
            return v
        if edges1[i] != edges2[i]:
            print("Warning: The two graphs do not have the same ordered edge labels.")
    
def test_dist_image():
    """
    Generates image for specific test data to ensure accurate plotting.

    Returns
    -------
    None.

    """
    test_graph = g2.create_graph(test_distance_data)
    short_path = ['A', 'D', 'G']
    pd.plot_graph(test_graph,'A','G',7,short_path, title='Distance Graph Path')
    
def test_delay_image():
    """
    Generates image for specific test data to ensure accurate plotting.

    Returns
    -------
    None.

    """
    test_graph = g2.create_graph(test_delay_data)
    short_path = ['A', 'B', 'F', 'G']
    pd.plot_graph(test_graph,'A','G',7,short_path, title='Delay Graph Path')
    
def test_weighted_image():
    """
    Generates image for specific test data to ensure accurate plotting.

    Returns
    -------
    None.

    """
    test_graph1 = g2.create_graph(test_distance_data)
    test_graph2 = g2.create_graph(test_delay_data)
    test_weighted_graph = g2.weighted_sum_edge_graph_2d(test_graph1, test_graph2, [1.0,1.0],7)
    short_path = ['A', 'B', 'F', 'G']
    pd.plot_graph(test_weighted_graph,'A','G',7,short_path, title='Weighted Graph Path')    
    
# test_dist_image()
# test_delay_image()
# test_weighted_image()

def test_graph_creation_dist():
    """
    Tests if distance graph built as expected from test data.

    Returns
    -------
    None. Prints warning for graph_2d() in g2

    """
    test_graph = g2.create_graph(test_distance_data)
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'D'), ('B', 'F'), ('C', 'D'), ('C', 'E'), ('D', 'E'), ('D', 'F'), ('D', 'G'), ('E', 'G'), ('F', 'G')]
    i = 0
    for node in test_graph.nodes():
        if node != nodes[i]:
            print("Warning: graph_2d() in g2 did not create the nodes of your distance graph as expected.")
        i += 1
    i = 0
    for edge in test_graph.edges():
        if edge != edges[i]:
            print("Warning: graph_2d() in g2 did not create the edges of your distance graph as expected.")
        i += 1
test_graph_creation_dist()

def test_graph_creation_delay():
    """
    Tests if delay graph built as expected from test data.

    Returns
    -------
    None. Prints warning for graph_2d() in g2

    """
    test_graph = g2.create_graph(test_delay_data)
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'D'), ('B', 'F'), ('C', 'D'), ('C', 'E'), ('D', 'E'), ('D', 'F'), ('D', 'G'), ('E', 'G'), ('F', 'G')]
    i = 0
    for node in test_graph.nodes():
        if node != nodes[i]:
            print("Warning: graph_2d() in g2 did not create the nodes of your delay graph as expected.")
        i += 1
    i = 0
    for edge in test_graph.edges():
        if edge != edges[i]:
            print("Warning: graph_2d() in g2 did not create the edges of your delay graph as expected.")
        i += 1

test_graph_creation_delay()

def test_weighted_graph_creation():
    """
    Tests if weighted graph built as expected from test data.

    Returns
    -------
    None. Prints warning for weighted_sum_edge_graph_2d() in g2

    """
    test_graph1 = g2.create_graph(test_distance_data)
    test_graph2 = g2.create_graph(test_delay_data)
    test_weighted_graph = g2.weighted_sum_edge_graph_2d(test_graph1, test_graph2, [1.0,1.0],7)
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    if len(nodes) != len(test_weighted_graph.nodes):
        print("Warning: weighted_sum_edge_graph_2d() in g2 did not create the nodes of your weighted graph as expected.")
    edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'D'), ('B', 'F'), ('C', 'D'), ('C', 'E'), ('D', 'E'), ('D', 'F'), ('D', 'G'), ('E', 'G'), ('F', 'G')]
    if len(edges) != len(test_weighted_graph.edges):
        print("Length Warning: weighted_sum_edge_graph_2d() in g2 did not create the edges of your weighted graph as expected.")
    print(test_weighted_graph.edges)
    i = 0
    for node in test_weighted_graph.nodes():
        if node != nodes[i]:
            print("Warning: weighted_sum_edge_graph_2d() in g2 did not create the nodes of your weighted graph as expected.")
        i += 1
    i = 0
    for edge in test_weighted_graph.edges():
        if edge != edges[i]:
            print("Warning: weighted_sum_edge_graph_2d() in g2 did not create the edges of your weighted graph as expected.")
        i += 1
        
# test_weighted_graph_creation()

def test_shortest_distance_path():
    """
    Tests networkx shortest path for distance data is computed properly with printed warnings if fails.

    Returns
    -------
    None.

    """
    test_graph_dist = g2.create_graph(test_distance_data)
    test_path_dist = nx.shortest_path(test_graph_dist, source='A', target='G', weight='weight')
    short_path = ['A', 'D', 'G']
    i = 0
    for node in test_path_dist:
        if len(short_path) != len(test_path_dist):
            print("Warning: nx.shortest_path() did not compute as expected. Likely weight assignment error.")
            break;
        if node != short_path[i]:
            print("Warning: nx.shortest_path() did not compute as expected. Likely edge label assignment error.")
        i += 1
        
test_shortest_distance_path()

def test_shortest_delay_path():
    """
    Tests networkx shortest path for delay data is computed properly with printed warnings if fails.

    Returns
    -------
    None.

    """
    test_graph_delay = g2.create_graph(test_delay_data)
    test_path_delay = nx.shortest_path(test_graph_delay, source='A', target='G', weight='weight')
    short_path = ['A', 'B', 'F', 'G']
    i = 0
    for node in test_path_delay:
        if len(short_path) != len(test_path_delay):
            print("You have not found the accurate shortest path.")
            break;
        if node != short_path[i]:
            print("You have not found the accurate shortest path.")
        i += 1

test_shortest_delay_path()

def test_shortest_weighted_path():
    """
    Tests if networkx shortest path for weighted data is computed properly with printed warnings if fails.

    Returns
    -------
    None.

    """
    print("Need to write this test.")

def test_flow_dist():
    """
    Tests g2.get_path_flow() if accurate flow for a specific path is computed correctly for distance data.

    Returns
    -------
    None.

    """
    short_path = ['A', 'D', 'G']
    test_graph_dist = g2.create_graph(test_distance_data)
    test_flow_dist = g2.get_path_flow(test_graph_dist, short_path)
    real_flow = 8.4
    if test_flow_dist != real_flow:
        print("You have not found the accurate shortest path flow.")
 
test_flow_dist()

def test_flow_delay():
    """
    Tests g2.get_path_flow() if accurate flow for a specific path is computed correctly for delay data.

    Returns
    -------
    None.

    """
    short_path = ['A', 'B', 'F', 'G']
    test_graph_delay = g2.create_graph(test_delay_data)
    test_flow_delay = g2.get_path_flow(test_graph_delay, short_path)
    real_flow = 0.06
    if test_flow_delay != real_flow:
        print("You have not found the accurate shortest path flow.")
 
test_flow_delay()

    
def test_shortest_parallel_path():
    print("Need to write this test.")
    
def test_optimal_path():
    print("Need to write this test.")
    
def test_find_optimal_param():
    print("Need to write this test.")
    
def test_financial_risk():
    print("Need to write this test.")
