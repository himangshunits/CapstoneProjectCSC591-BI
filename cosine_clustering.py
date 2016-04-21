import centroid_generation as cg
import sys
import numpy as np
import pandas as pd

################################################################################################
# CODE FOR FINDING CLUSTER BASED ON COSINE SIMILARITY
################################################################################################

def cos_clusters(oc, nc, pc):
	user_cos = np.load("user_cos.npy")	
	(row, col) = user_cos.shape
	o_cluster = []
	n_cluster = []
	p_cluster = []
	for i in range(1, row):
		o_sim = user_cos[oc, i]
		n_sim = user_cos[nc, i]
		p_sim = user_cos[pc, i]
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
[o_cluster, n_cluster, p_cluster] = cos_clusters(optimist_centroid, neutral_centroid, pessimist_centroid)
print o_cluster, n_cluster, p_cluster