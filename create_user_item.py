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


import pandas as pd
import reading as rd
import numpy as np

MAX_SIZE_USER = len(rd.users) + 1
MAX_SIZE_ITEM = len(rd.movies) + 1

user_item = pd.DataFrame(np.nan, index=range(0,MAX_SIZE_USER), columns=range(0,MAX_SIZE_ITEM))

for k in rd.ratings.index:
    u = rd.ratings.ix[k].UserID
    i = rd.ratings.ix[k].MovieID
    user_item.loc[u,i] = rd.ratings.ix[k].Rating
    
user_item.to_csv('user_item.csv',index =False,header=True)

user_item = pd.read_csv('user_item.csv')