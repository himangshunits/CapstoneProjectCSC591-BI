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
    
    for rb in range(ra,6041):
        print rb
        temp1 = rd.ratings[rd.ratings.UserID==ra].MovieID
        temp2 = rd.ratings[rd.ratings.UserID==rb].MovieID
        
        common_movies = set(temp1) & set(temp2)
        
        num_pcc = 0.0
        denom_pcc =0.0
        
        d1_pcc = 0.0
        d1_cos = 0.0
        
        d2_pcc = 0.0
        d2_cos = 0.0
        
        num_cos = 0.0
        
        denom_cos = 0.0
        
        
        
        
        for i in common_movies:
            rai = rd.ratings[(rd.ratings.UserID==ra) & (rd.ratings.MovieID ==i)].Rating.values[0]
            rbi = rd.ratings[(rd.ratings.UserID==rb) & (rd.ratings.MovieID ==i) ].Rating.values[0]
            
            ra_bar = r_mean[ra]
            rb_bar = r_mean[ra]
            
            #print ra_bar
            
            
            #print (rai - r_mean[ra]).values[0] * (rbi - r_mean[rb]).values[0]
            num_pcc += (rai - ra_bar) * (rbi - rb_bar)
            
            d1_pcc += (rai - ra_bar) ** 2 
            d2_pcc += (rbi - rb_bar) ** 2
        
            num_cos += rai * rbi
            d1_cos += rai ** 2
            d2_cos += rbi ** 2
        
       
       
        
        
          
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