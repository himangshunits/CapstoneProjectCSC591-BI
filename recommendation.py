import ups_clustering as uc
import numpy as np
import pandas as pd
import reading as rd
import math

k = 5
t = 62
i = 257


MAX_SIZE_USER = len(rd.users) + 1
MAX_SIZE_ITEM = len(rd.movies) + 1

r_mean = rd.ratings.groupby(['UserID'])['Rating'].mean()
sim = np.load("user_ups.npy")
user_item = pd.read_csv("user_item.csv")

U_o = uc.o_cluster
U_p = uc.p_cluster
U_n = uc.n_cluster

U_sample = []

if t in U_o:
	U_sample = U_o + U_n
elif t in U_p:
	U_sample = U_p + U_n
else:
	U_sample = U_n

print len(U_o)
print len(U_n)
print len(U_p)
print len(U_sample)

sim_u = []
for u in U_sample:
	sim_u += [(sim[u][t], u)]

sim_u = sorted(sim_u, reverse = True)
U_nei = [x[1] for x in sim_u[:k+1]]

#calculate U_nei
#U_nei = [1,2,3,4,5]

#prediction
list_predictions = []
# recommendation for user t
for i in range(1, MAX_SIZE_ITEM):
	rti = user_item.ix[t][i]


	if not math.isnan(rti):
		prediction = r_mean[t]

		prediction_second_num =0.0
		prediction_second_denom =0.0


		for u in U_nei:
			rui = user_item.ix[u][i]
			if not math.isnan(rui):
				prediction_second_num += ((rui - r_mean[u]) * sim[t][u])
				prediction_second_denom += abs(sim[t][u])
			
		if prediction_second_denom != 0.0:
			prediction += ((prediction_second_num*1.0)/(prediction_second_denom*1.0))

		#print r_mean[t]
		#print prediction,"prediction"
		#list_predictions.append((i,prediction))

print list_predictions
