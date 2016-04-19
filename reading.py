import pandas as pd
import numpy as np


movies = pd.read_csv('ml-1m_dataset/movies.dat', sep='::',header = 0)
movies.to_csv('temp.csv',columns=['Genres'],index =False,header=False)

ratings = pd.read_csv('ml-1m_dataset/ratings.dat', sep='::')
users = pd.read_csv('ml-1m_dataset/users.dat', sep='::')


f = open('temp.csv','r')

li=[]
l2=[]
for line in f:
    temp = line.strip().split('|')  

    l2.append(temp)
    for t in temp:
        li.append(t)
        

li = sorted(set(li))


f.close()

l3=[]

for gen in l2:
    vec = ""
    for w in li:
        if w in gen:
            vec += "1"
        else:
            vec += "0"
    l3.append(vec)



movies['Vector'] = np.asarray(l3)
#print movies

#movies.to_csv('final.csv',index =False,header=False)
