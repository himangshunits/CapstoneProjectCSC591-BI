################################################################################################
# PLEASE README!
################################################################################################

# The Code for Capstone Project of CSC 591 : Algorithms for Data Guided Business Intelligence
# Title : Clustering Based Recommendation Systems using Optimistic and Pessimistic User Clusters
# Team No : 14
# Memebers:
# Himangshu Ranjan Borah(hborah)
# Rahul Shah(rshah5)
# Krunal Gala(kgala)
# Siddhant Doshi(sadoshi)
# Sushma Ravichandran(sravich)
# Harsha Kunapareddy(skunapa)

# This file implements the user and item graph building. Currently not being used in the main implementations.
# 1. Zhang, J., Lin, Y., Lin, M., & Liu, J. (2016). An effective collaborative filtering algorithm based on user preference clustering. Applied Intelligence, 1-11.



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





# Input parsing
if len(sys.argv) != 3:
	print "The input format is not proper ! Please enter in the following format. Typical alpha, beta = 4 and 2"
	print "python build_graph.py <alpha value> <beta_value>"    
	exit(1)
alpha_value = float(sys.argv[1])
beta_value = float(sys.argv[2])




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
	#[pearson_matrix_user, cosine_matrix_user] = bsm.calculate_matrices_user()
	pearson_matrix_user = np.load("user_pcc.npy")
	cosine_matrix_user = np.load("user_cos.npy")
	#print pearson_matrix_user
	#print cosine_matrix_user
	#exit(0)
	no_of_users = len(pearson_matrix_user[:,1])
	user_graph = gp.Graph.Full(no_of_users)
	print "No of users = %d" % no_of_users
	for i in xrange(1, no_of_users):
		for j in xrange(1, no_of_users):
			source_id = i
			target_id = j
			print source_id, target_id
			curr_edge = user_graph.es.select([source_id], [target_id])
			curr_edge['pearson'] = pearson_matrix_user[i, j]
			curr_edge['cosine'] = cosine_matrix_user[i, j]

	sac_plot(user_graph)
	print user_graph.es.find(_between=((3,), (4,)))[0]		








# Call the main. Entry point.

if __name__ == "__main__":
	main()
