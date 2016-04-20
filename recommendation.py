import ups_clustering as uc
import numpy as np
import pandas as pd


k = 10

U_o = uc.o_cluster
U_p = uc.p_cluster
U_n = uc.n_cluster

print U_o, U_n , U_p



user_id = 1

U_sample = []

print "Hello"

print len(U_o)
print len(U_p)
print len(U_n)

if user_id in U_o:
	U_sample = U_o + U_n
elif user_id in U_p:
	U_sample = U_p + U_n
else:
	U_sample = U_n

print len(U_sample)
print U_sample