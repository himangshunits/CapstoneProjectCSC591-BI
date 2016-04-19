import sys
import collections
import time
import csv
import math
import copy
import numpy as np
import pandas as pd
import igraph as gp
from itertools import izip
from sklearn.metrics.pairwise import cosine_similarity
import colour
import build_similarity_matrices as bsm





################################################################################################
# CODE FOR VISUALIZATION OR THE CLUSTERS
################################################################################################


# Function to plot an igraph object.
def sac_plot(sac_graph):
	layout = sac_graph.layout("kk")
	gp.plot(sac_graph, layout=layout)


# Fucntion to plot an I graph object with different clusters having different colors according to a membership list.
def sac_plot_cluster(sac_graph, membership_list, filename):
	red = colour.Color("red")
	blue = colour.Color("blue")
	my_rainbow = list(red.range_to(blue, membership_list.max() + 1))
	color_list = [i.get_hex_l() for i in my_rainbow]
	layout = sac_graph.layout("kk")
	gp.plot(sac_graph, filename, layout=layout, vertex_color=[color_list[x] for x in membership_list])

# Same as above function, but from a cluster_dict. Saves the plot to filename.
def plot_clusters_from_dict(clusters_dict, sac_graph_original, filename):
	membership_list = [0] * len(sac_graph_original.vs)
	membership_list = pd.Series(membership_list)
	for key in clusters_dict.iterkeys():
		indices = list(clusters_dict[key])
		cluster_id = key
		for index in indices:
			membership_list[index] = cluster_id
	sac_plot_cluster(sac_graph_original, membership_list, filename)		





################################################################################################
# CODE FOR BUILDING THE MAIN GRAPH
################################################################################################


def main():	
	build_graph_from_matrices()



def build_graph_from_matrices():
	[pearson_matrix_user, cosine_matrix_user] = bsm.calculate_matrices_user()
	#print pearson_matrix_user
	no_of_users = len(pearson_matrix_user)
	user_graph = gp.Graph.Full








# Call the main. Entry point.

if __name__ == "__main__":
	main()
