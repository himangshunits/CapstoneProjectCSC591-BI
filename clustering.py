import pandas as pd
import numpy as np
import math


################################################################################################
# FUNCTION FOR FINDING OPTIMSTIC, PESSIMISTIC AND NEUTRAL USER GROUPS
################################################################################################

def find_user_groups(alpha, beta):
	ratings = pd.read_csv('ml-100k/u.data', sep='\t')
	r_mean = ratings.groupby(['UserID'])['Rating'].mean()
	r_mean.sort_values(inplace = True)
	r_mean.index

	for i in range(r_mean.size):
		if r_mean.iloc[i] > beta:
			pessimist = i
			break
	for i in range(r_mean.size):
		if r_mean.iloc[i] > alpha:
			optimist = i
			break
	Up = list(r_mean.index[:pessimist])
	Un = list(r_mean.index[pessimist:optimist])
	Uo = list(r_mean.index[optimist:-1])
	return Up, Un, Uo


################################################################################################
# FUNCTION FOR FINDING CENTROIDS OF OPTIMSTIC, PESSIMISTIC AND NEUTRAL USER GROUPS CLUSTERS
################################################################################################

def find_centroid(Uo, Un, Up):
	user_item = pd.read_csv("user_item.csv")
	no_of_rows = len(user_item)
	optimist_centroid = 0
	pessimist_centroid = 0
	neutral_centroid = 0

	max_items = 0

	row = len(Uo)
	for i in range (0, row):
		temp = user_item.loc[Uo[i],:]
		temp = temp.dropna()
		if len(temp) > max_items:
			max_items = len(temp)
			optimist_centroid = Uo[i]
			
	max_items = 0
	row = len(Un)
	for i in range (0, row):
		temp = user_item.loc[Un[i],:]
		temp = temp.dropna()
		if len(temp) > max_items:
			max_items = len(temp)
			neutral_centroid = Un[i]


	max_items = 0
	row = len(Up)
	for i in range (0, row):
		temp = user_item.loc[Up[i],:]
		temp = temp.dropna()
		if len(temp) > max_items:
			max_items = len(temp)
			pessimist_centroid = Up[i]


	return optimist_centroid, neutral_centroid, pessimist_centroid


if __name__ == "__main__":
	[Uo, Un, Up] = find_user_groups(4,2)
	print "User Groups have been found"
	print "Creating Centroids..."
	[optimist_centroid, neutral_centroid, pessimist_centroid] = find_centroid(Uo, Un, Up)
	print "THE THREE CENTROIDS ARE"
	print optimist_centroid, neutral_centroid, pessimist_centroid

	