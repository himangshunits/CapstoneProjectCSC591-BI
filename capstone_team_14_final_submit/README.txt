################################################################################################
# PLEASE README!
################################################################################################

# The Code for Capstone Project of CSC 591 : Algorithms for Data Guided Business Intelligence
# Title : Clustering Based Recommendation Systems using Optimistic and Pessimistic User Clusters
# Reference Publications:
# 1. Zhang, J., Lin, Y., Lin, M., & Liu, J. (2016). An effective collaborative filtering algorithm based on user preference clustering. Applied Intelligence, 1-11.
# 2. Sarwar, Badrul et al. "I tembased
# collaborative filtering recommendation algorithms. " P roceedings of the 10th
# international conference on World Wide Web 1 Apr. 2001: 285295.
# 3. Aytekin, Tevfik, and Mahmut Özge Karakaya. "C lusteringbased
# diversity improvement in topN
# recommendation. " Journal of Intelligent Information Systems 42.1 (2014): 118.
# 4. Pham, Manh Cuong et al. "A Clustering Approach for Collaborative Filtering Recommendation Using Social
# Network Analysis. " J. UCS 17.4 (2011): 583604.
# 5. Braak, Paul te, Noraswaliza Abdullah, and Yue Xu. "I mproving the performance of collaborative filtering
# recommender systems through user profile clustering." P roceedings of the 2009 IEEE/WIC/ACM International
# Joint Conference on Web Intelligence and Intelligent Agent TechnologyVolume
# 03 15 Sep. 2009: 147150.
# 
#
#
# Team No : 14
# Memebers:
# Himangshu Ranjan Borah(hborah)
# Rahul Shah(rshah5)
# Krunal Gala(kgala)
# Siddhant Doshi(sadoshi)
# Sushma Ravichandran(sravich)
# Harsha Kunapareddy(skunapa)

# The following libraries has to be installed which are available as pip packages : numpy, pandas, igraph

# Description of the Code Files:
# build_graph.py : used to build graphs from user item matrix, currently not being used in the main flow.
# build_similarity_matrices.py : Used to compute various similiraty matrices between users.(stores the matrices in numpy arrayas in files *.npy)
# create_user_item.py : to build the user item matrix, stores in csv file called user_item.csv
# *_clustering.py : Implements various clustering methods corresponding to different similarity measures.
# centroid_generation.py : Used to fidn the centroids as described in the reference paper.
# recommendation_*.py : Used to evaluate the models on the known ratings.
# recommendation_topk.py : ;reccomends top k movies to the user which he has not seen.


# Code Running instructions 
# The matrices and the user item matrix are already generated as described above.
# If you want to generate the matrices, just run the codes build_similarity_matrices.py, create_user_item.py
# To build the models and evaluate, set the K values in the scripts named recommendation_*.py and run.
# If you want recomendation for top k movies using the algorithm describes, run the recommendation_topk.py