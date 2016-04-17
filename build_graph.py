import pandas as pd
import numpy as np
import subprocess
import reading as rd
import math

#print rd.movies

cosine = np.zeros(shape=(6041,6041))

pearson = np.zeros(shape=(6041,6041))


r_mean = rd.ratings.groupby(['UserID'])['Rating'].mean()


for ra in range(1,6041):
    
    print ra
    #temp1 = rd.ratings[rd.ratings.UserID==ra].MovieID
    temp1 = rd.ratings[rd.ratings.UserID==ra].loc[:,['MovieID','Rating']]
    for rb in range(ra,6041):
        print rb
        
        #temp2 = rd.ratings[rd.ratings.UserID==rb].MovieID
        temp2 = rd.ratings[rd.ratings.UserID==rb].loc[:,['MovieID','Rating']]
        
        temp3=pd.merge(temp1, temp2, how='inner', on=['MovieID'])
        
        
        
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
 
print cosine