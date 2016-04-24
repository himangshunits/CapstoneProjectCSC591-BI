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


import centroid_generation as cg
import sys
import numpy as np
import pandas as pd

################################################################################################
# CODE FOR FINDING CLUSTER BASED ON PCC SIMILARITY
################################################################################################

def pcc_clusters(oc, nc, pc):
	user_pcc = np.load("user_pcc.npy")	
	(row, col) = user_pcc.shape
	o_cluster = []
	n_cluster = []
	p_cluster = []
	for i in range(1, row):
		o_sim = user_pcc[oc, i]
		n_sim = user_pcc[nc, i]
		p_sim = user_pcc[pc, i]
		if o_sim > n_sim and o_sim > p_sim:
			o_cluster.append(i)
		elif p_sim > n_sim and p_sim > o_sim:
			p_cluster.append(i)
		else:
			n_cluster.append(i)
	return o_cluster, n_cluster, p_cluster


alpha = 4.0
beta = 2.0
[Uo, Un, Up] = cg.find_user_groups(alpha,beta)
print "User Groups have been found"
print "Creating Centroids..."
[optimist_centroid, neutral_centroid, pessimist_centroid] = cg.find_centroid(Uo, Un, Up)
print "THE THREE CENTROIDS ARE"
print optimist_centroid, neutral_centroid, pessimist_centroid
[o_cluster, n_cluster, p_cluster] = pcc_clusters(optimist_centroid, neutral_centroid, pessimist_centroid)
print o_cluster, n_cluster, p_cluster