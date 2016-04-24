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

# This file implements the similarity matrix building functionalities of the following paper and stores the matrices as numpy arrays.
# 1. Zhang, J., Lin, Y., Lin, M., & Liu, J. (2016). An effective collaborative filtering algorithm based on user preference clustering. Applied Intelligence, 1-11.


import pandas as pd
import numpy as np
import reading as rd
import math

MAX_SIZE_USER = len(rd.users) + 1
#MAX_SIZE_USER = 10

MAX_SIZE_ITEM = len(rd.movies) + 1
#MAX_SIZE_ITEM = 10





def calculate_matrices_user():
    cosine = np.zeros(shape=(MAX_SIZE_USER,MAX_SIZE_USER))
    ups = np.zeros(shape=(MAX_SIZE_USER,MAX_SIZE_USER))
    pearson = np.zeros(shape=(MAX_SIZE_USER,MAX_SIZE_USER))


    r_mean = rd.ratings.groupby(['UserID'])['Rating'].mean()


    for ra in range(1,MAX_SIZE_USER):
        
        print ra
        
        temp1 = rd.ratings[rd.ratings.UserID==ra].loc[:,['MovieID','Rating']]
        ia = len(temp1)
        for rb in range(ra,MAX_SIZE_USER):
            temp2 = rd.ratings[rd.ratings.UserID==rb].loc[:,['MovieID','Rating']]            
            ib = len(temp2)
            temp3=pd.merge(temp1, temp2, how='inner', on=['MovieID'])              
            iintersect = len(temp3) * 1.0
            ups_exp =0.0
            ups_out=0.0
            rai = temp3.Rating_x
            rbi = temp3.Rating_y
            
           
            num_pcc = 0.0
            denom_pcc =0.0
            
            d1_pcc = 0.0
            d1_cos = 0.0
            
            d2_pcc = 0.0
            d2_cos = 0.0
            
            num_cos = 0.0
            
            denom_cos = 0.0            
             
            if iintersect == 0.0:
                ups_out = 0.0
                ups_exp = 0.0     
            else:
                ups_exp = math.exp(((sum(abs(rai - rbi)) * -1.0) / iintersect) * (abs(r_mean[ra] - r_mean[rb])))
                ups_out = (iintersect)/(ia+ib-iintersect)          

           
            num_pcc = sum ((rai - r_mean[ra]) * (rbi - r_mean[rb]))            
                
            d1_pcc = sum((rai - r_mean[ra]) ** 2 )
            d2_pcc = sum((rbi - r_mean[rb]) ** 2 )
            
            num_cos = sum(rai * rbi)
            d1_cos = sum(rai ** 2)
            d2_cos = sum(rbi ** 2)

            denom_pcc = math.sqrt(d1_pcc) * math.sqrt(d2_pcc)     
            denom_cos = math.sqrt(d1_cos) * math.sqrt(d2_cos)       
        
            if(denom_pcc==0.0):
                denom_pcc =1.0
        
            if(denom_cos==0.0):
                denom_cos =1.0


            pearson[ra][rb] = num_pcc/denom_pcc
            cosine[ra][rb] = num_cos/denom_cos
            
            pearson[rb][ra] = pearson[ra][rb]
            cosine[rb][ra] = cosine[ra][rb]
            
            ups[ra][rb]=ups_exp * ups_out
            ups[rb][ra]=ups[ra][rb]
            
    #np.save("user_pcc", pearson)
    #np.save("user_cos", cosine)
    #np.save("user_ups", ups)
    return pearson, cosine






def calculate_matrices_item():
    cosine = np.zeros(shape=(MAX_SIZE_ITEM,MAX_SIZE_ITEM))

    pearson = np.zeros(shape=(MAX_SIZE_ITEM,MAX_SIZE_ITEM))


    r_mean = rd.ratings.groupby(['MovieID'])['Rating'].mean()


    for ra in range(1,MAX_SIZE_ITEM):
        
        print ra
        #temp1 = rd.ratings[rd.ratings.UserID==ra].MovieID
        temp1 = rd.ratings[rd.ratings.MovieID==ra].loc[:,['UserID','Rating']]
        for rb in range(ra,MAX_SIZE_ITEM):
            #print rb            
            #temp2 = rd.ratings[rd.ratings.UserID==rb].MovieID
            temp2 = rd.ratings[rd.ratings.MovieID==rb].loc[:,['UserID','Rating']]            
            temp3=pd.merge(temp1, temp2, how='inner', on=['UserID'])              
            
            num_pcc = 0.0
            denom_pcc =0.0
            
            d1_pcc = 0.0
            d1_cos = 0.0
            
            d2_pcc = 0.0
            d2_cos = 0.0
            
            num_cos = 0.0
            
            denom_cos = 0.0            
            
            rai = temp3.Rating_x
            rbi = temp3.Rating_y
            
            num_pcc = sum ((rai - r_mean[ra]) * (rbi - r_mean[rb]))            
                
            d1_pcc = sum((rai - r_mean[ra]) ** 2 )
            d2_pcc = sum((rbi - r_mean[rb]) ** 2 )
            
            num_cos = sum(rai * rbi)
            d1_cos = sum(rai ** 2)
            d2_cos = sum(rbi ** 2)

            denom_pcc = math.sqrt(d1_pcc) * math.sqrt(d2_pcc)     
            denom_cos = math.sqrt(d1_cos) * math.sqrt(d2_cos)       
        
            if(denom_pcc==0.0):
                denom_pcc =1.0
        
            if(denom_cos==0.0):
                denom_cos =1.0


            pearson[ra][rb] = num_pcc/denom_pcc
            cosine[ra][rb] = num_cos/denom_cos
            
            pearson[rb][ra] = pearson[ra][rb]
            cosine[rb][ra] = cosine[ra][rb]
    
    np.save("item_pcc", pearson)
    np.save("item_cos", cosine)
     
    return pearson, cosine


calculate_matrices_user()
#calculate_matrices_item()

