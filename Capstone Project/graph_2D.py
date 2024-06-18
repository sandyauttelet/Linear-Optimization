"""

@author: Sandy Auttelet

"""

import numpy as np
import networkx as nx

#For rounding if needed:
def find_mantissa(num):
    """
    Finds optimal rounded values for report printing.

    Parameters
    ----------
    num : float
        number you are trying to round.

    Returns
    -------
    rounded_num : float
        rounded number to three decimal places.

    """
    scale = int(round(np.log10(num),0))-7 #the 7 here defines order of accuracy in reporting
    mantissa = int(round(num/10**scale,0))
    rounded_num = mantissa*10**scale
    rounded_num = round(rounded_num,3)
    return rounded_num

def create_graph(data):
    """
    Builds a networkx graph object from a matrix of edge weights.

    Parameters
    ----------
    data : list of list of floats
        edge weights for graph

    Returns
    -------
    G : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html

    """
    G = nx.Graph(weight=0)
    n = len(data)
    for i in range(n):
        G.add_node(chr(i+65))
    for i in range(n):
        for j in range(n):
            if data[i][j] != 0:
                G.add_edge(chr(i+65),chr(j+65), weight=data[i][j])
    return G

def weighted_sum_edge_graph_2d(graph1, graph2, weights_p,n,sim=True):
    """
    Builds a networkx graph object with edge weights calculated from weighted sum of two input graphs.

    Parameters
    ----------
    graph1 : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html
    graph2 : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html
    weights_p : float
        adjustable parameter for weighted sum calculating manipulating importance of graph2 data compared to graph1
    n : int
        number of nodes in each graph
    sim : bool, optional
        Used to determine if input graphs have same structure for weighted sum calulation. The default is True.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if sim == False:
        print("Your two data sets are not the same size with the same connections and thus a weighted graph cannot be computed.")
        return None
    G = nx.Graph(weight=0)
    ratios = []
    for i in range(n):
        G.add_node(chr(i+65))
    for i in range(n):
        for j in range(n):
            if graph1.get_edge_data(chr(i+65),chr(j+65)) != None and graph2.get_edge_data(chr(i+65),chr(j+65)) != None:
                edge1_weight = graph1.get_edge_data(chr(i+65),chr(j+65),"weight")
                edge2_weight = graph2.get_edge_data(chr(i+65),chr(j+65),"weight")
                ratios.append(edge1_weight['weight']/edge2_weight['weight'])
                weighted_sum = edge1_weight['weight']+weights_p*edge2_weight['weight']
                G.add_edge(chr(i+65),chr(j+65), weight=weighted_sum)
    return G, max(ratios)
    

def get_path_flow(graph, path):
    """
    Determines the sum of the weight on each edge from a specified travel path.

    Parameters
    ----------
    graph : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html
    path : list of strings
        Strings denote nodes from graph, list of a specific path taken.

    Returns
    -------
    flow : float
        Sum of weights on edges traveled from input path.

    """
    flow = 0
    for i in range(1,len(path)):
        edge_weight = graph.get_edge_data(path[i-1],path[i],"weight")
        if graph.get_edge_data(path[i-1],path[i]) != None:
            flow += edge_weight['weight']
    return round(flow,6)

def run_shortest_parallel(graph1, graph2, graph_weighted, source):
    """
    Returns all optimal paths for a source node to all other nodes in the graph.

    Parameters
    ----------
    graph1 : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html
    graph2 : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html
    graph_weighted : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html, generated from weighted sum.
    source : string
        node label for starting point in paths.

    Returns
    -------
    path_info : list of list of strings and two floats
        first part of list is optimal path with each node traveled to, second element
        is distance traveled in path, and third is probability of delay.

    """
    paths = dijkstra(graph_weighted)
    path_info = []
    for i in range(len(paths[source])):
        flow1_paths = get_path_flow(graph1, paths[source][chr(i+65)])
        flow2_paths = get_path_flow(graph2, paths[source][chr(i+65)])
        path_info.append([paths[source][chr(i+65)], flow1_paths, flow2_paths])
    return path_info

def dijkstra(graph):
    path = dict(nx.all_pairs_dijkstra_path(graph))
    return path
    
def find_optimal_param(graph1,graph2,source,sink,n,sim):
    """
    Determines what value of input weight parameter switches path aand saves those numbers with associated path.

    Parameters
    ----------
    graph1 : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html
    graph2 : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html
    source : String
        Starting point
    sink : String
        Ending point
    n : int
        number of nodes in graphs
    sim : bool
        ensures graphs have the same structure so weighted sum can be computed.

    Returns
    -------
    path_shifts : list of list of strings and one float
        list of path, strings denoting nodes traveled to, for shortest path with a weight parameter in each list.

    """
    graph0, ratio = weighted_sum_edge_graph_2d(graph1, graph2, 0,n,sim=sim)
    weights = np.linspace(0,int(ratio+100),10000)
    path_0 = nx.shortest_path(graph0, source=source, target=sink, weight='weight')
    path_shifts = [[path_0,0]]
    k = 1
    for i in range(len(weights)):
        path_w = path_0
        graph_weighted = weighted_sum_edge_graph_2d(graph1, graph2, weights[i],n,sim=sim)[0]
        path_0 = nx.shortest_path(graph_weighted, source=source, target=sink, weight='weight')
        if path_w != path_0:
            k+=1
            path_shifts.append([path_0,weights[i]])
    return path_shifts

def financial_risk(d,p,q,tol1,tol2,i, w=0.55,f=7.0,g=3.999,v=63.0):
    """
    Determines if route is financially viable based on risk assessment calculations.

    Parameters
    ----------
    d : flaot
        distance traveled
    p : float
        probability of delay
    q : float
        price of order
    m : float
        max time able to drive
    tol2 : float
        max risk willing to take
    w : float, optional
        wage of driver per mile. The default is 0.55.
    f : float, optional
        fuel efficiency of Freigthliner Cascadia truck. The default is 7.0.
    g : float, optional
        average cost of fuel per gallon. The default is 3.999.
    v : float, optional
        average speed in miles per hour. The default is 63.0.

    Returns
    -------
    bool
        returns true if cost of service is less than price of order.

    """
    c = w*d+(g*d/f)
    t = d/v
    r = q*p
    V = r+c
    if r > tol2:
        print(f'Current risk is larger than max risk input for path {i+1}.\n')
        return False
    if t > tol1:
        print(f'Current expected time of delivery is larger than max time input for path {i+1}.\n')
        return False
    if V > q:
        print(f'Current cost of service is larger than cost of order for path {i+1}.\n')
        return False
    if q < c:
        print(f'Current weighting parameter is not optimal for shortest distance for path {i+1}.\n')
        return False
    else:
        return True
    
def optimal_path(paths, graph1, graph2, tol1, tol2,cost):
    """
    Determines if a path is optimal based on input parameters and financial risk assessment.

    Parameters
    ----------
    paths : list of lists
        All possible paths from source to sink
    graph1 : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html
    graph2 : networkx graph object
        https://networkx.org/documentation/stable/tutorial.html
    tol1 : float
        Max time able to travel
    tol2 : float
        max risk willing to accept
    cost : flaot
        price charged to customer for order delivery

    Returns
    -------
    optimal_paths : list of lists
        all possible paths that are considered optimal based on input parameters

    """
    optimal_paths = []
    for i in range(len(paths)):
        flow1 = get_path_flow(graph1, paths[i][0])
        flow2 = get_path_flow(graph2, paths[i][0])
        risk = financial_risk(flow1,flow2,cost,tol1,tol2, i)
        if risk == True:
            optimal_paths.append(paths[i][0])
    if len(optimal_paths) < 1:
        print("No optimal path was found based on input parameters.")
        print("Consider adjusting input parameters and recalculating the optimal path.\n")
    return optimal_paths
