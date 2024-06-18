"""

@author: Sandy Auttelet

"""

import graph_2D as g2
import plotting_data as pd
import numpy as np
import networkx as nx
import tests as ts
import os
import csv
import saving_gui as GUI #Comment out this import if you do not want to execute GUI

#Check current directory's path
#os.getcwd()

data = np.genfromtxt('input_data.txt', dtype=None, delimiter=",", encoding=None)

file1_name,file2_name,source,sink,weight,tol,order_cost,file1_text,file2_text,file1_type,file2_type = GUI.load_data()

#else:
"""
Default User Input
===============================================================================
"""
data1 = np.loadtxt(file1_name, delimiter=",")
data2 = np.loadtxt(file2_name, delimiter=",")

# source = 'A'
# sink = 'G'

# weight = 7000

# #Maximum tolerance for [distance, delay]
# tol = [100.0, 0.06]

# #Additional parameters for printing and financial risk assessment
# order_cost = 100
# file1_text = 'distance'
# file2_text = 'delay'
# file1_type = 'csv'
# file2_type = 'csv'

#==============================================================================




"""
Building Graphs
===============================================================================
"""
graph1 = g2.create_graph(data1)
graph2 = g2.create_graph(data2)
n = len(data1)
m = len(data2)

sim = ts.test_data_similarity(graph1,graph2)

graph_weighted = g2.weighted_sum_edge_graph_2d(graph1, graph2, weight,n,sim=sim)[0]
k = len(graph_weighted.nodes)

#==============================================================================





"""
Optimal Paths
===============================================================================
"""
path_g1 = nx.shortest_path(graph1, source=source, target=sink, weight='weight')
path_g2 = nx.shortest_path(graph2, source=source, target=sink, weight='weight')
path_weighted = nx.shortest_path(graph_weighted, source=source, target=sink, weight='weight')

#==============================================================================





"""
Checking Tolerance
===============================================================================
"""

path_with_weight = g2.find_optimal_param(graph1,graph2,source,sink,n,sim)
print(path_with_weight)

paths = g2.run_shortest_parallel(graph1, graph2,graph_weighted, source)

all_paths = []
for i in range(len(path_with_weight)):
    all_paths.append(path_with_weight[i][0])


# #The code below was used to find intermediate paths and the ratio slice.
# paths_with_weights = []
# for i in range(len(graph1.nodes)):
#     path_with_weight = g2.find_optimal_param(graph1,graph2,'A',chr(i+65),n,sim)
#     paths_with_weights.append(path_with_weight)


#==============================================================================





"""
Finding Flows
===============================================================================
"""
#1D Flow
flow1_opt = g2.get_path_flow(graph1, path_g1)
flow1_g2 = g2.get_path_flow(graph1, path_g2)
flow2_opt = g2.get_path_flow(graph2, path_g2)
flow2_g1 = g2.get_path_flow(graph2, path_g1)


#2D Flow
flow1_w = g2.get_path_flow(graph1, path_weighted)
flow2_w = g2.get_path_flow(graph2, path_weighted)

#Irrelivant value numerically due to delay importance parameter
flow_weighted = g2.get_path_flow(graph_weighted, path_weighted)

#==============================================================================




"""
===============================================================================
===============================================================================
Print Report
===============================================================================
===============================================================================
"""

print(f'Optimal {file1_text} path:', path_g1)
print(f'{file1_text} of optimal {file1_text} path:', flow1_opt)
print(f'{file2_text} of optimal {file1_text} path:', flow2_g1, "\n")

print(f'Optimal {file2_text} path:', path_g2)
print(f'{file1_text} of optimal {file2_text} path:', flow1_g2)
print(f'{file2_text} of optimal {file2_text} path:', flow2_opt, "\n")

print("Optimal weighted path:", path_weighted)
print(f'{file1_text} of weighted path:', flow1_w)
print(f'{file2_text} of weighted path:', flow2_w, "\n")


print(f'All paths from {source} to {sink}\n', all_paths, "\n")

optimal_paths = g2.optimal_path(path_with_weight, graph1, graph2, tol[0], tol[1],order_cost)
print(f'All optimal paths from {source} to {sink} with input parameters assessed:\n', optimal_paths,"\n")

print(f'All optimal weighted paths from {source} to all other cities with {file1_text} and {file2_text} respectively:\n', paths)

"""
Plotting Graphs
===============================================================================
"""
pd.plot_graph(graph1,source,sink,n,path_g1, title=f'{file1_text} graph path')
pd.plot_graph(graph2,source,sink,m,path_g2, title=f'{file2_text} graph path')
pd.plot_graph(graph_weighted,source,sink,k,path_weighted, title='weighted graph path')

#==============================================================================
