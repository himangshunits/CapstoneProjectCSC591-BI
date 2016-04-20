import build_similarity_matrices as bsm
import pandas as pd
import numpy as np
import reading as rd
import math


def clustering(alpha, beta):
	r_mean = rd.ratings.groupby(['UserID'])['Rating'].mean()
	r_mean.sort()
	r_mean.index

	for i in range(r_mean.size):
		if r_mean.iloc[i] > beta:
			pessimist = i
			break
	for i in range(r_mean.size):
		if r_mean.iloc[i] > alpha:
			optimist = i
			break
	print optimist, pessimist
	print r_mean.index[:pessimist]
	print r_mean.index[pessimist:optimist]
	print r_mean.index[optimist:-1]



clustering(4,2)
