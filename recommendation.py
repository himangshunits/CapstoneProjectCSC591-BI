import ups_clustering as uc
import numpy as np
import pandas as pd
import reading as rd

k = 10
t = 1
i = 10

r_mean = rd.ratings.groupby(['UserID'])['Rating'].mean()
sim = uc.user_ups

U_o = uc.o_cluster
U_p = uc.p_cluster
U_n = uc.n_cluster

#print U_o, U_n , U_p
print "Hello"


U_sample = []


if user_id in U_o:
	U_sample = U_o + U_n
elif user_id in U_p:
	U_sample = U_p + U_n
else:
	U_sample = U_n


print len(U_o)
print len(U_n)
print len(U_p)
print len(U_sample)


'''
#calculate U_nei
U_nei = [1,2,3,4,5]

user_item = pd.read_csv("user_item.csv")
prediction = r_mean[t]

prediction_second_num =0.0
prediction_second_denom =0.0

for u in U_nei:
	rui = user_item.ix[u][i]
	if !Math.isnan(rui):
		prediction_second_num += ((rui - r_mean[u]) * sim[t][u])
		prediction_second_denom += abs(sim[t][u])

if prediction_second_denom != 0.0
	prediction += ((prediction_second_num*1.0)/(prediction_second_denom*1.0))
'''
