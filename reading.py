import pandas as pd
import numpy as np


movies = pd.read_csv('ml-100k/u.item', sep='|',header = 0)
#movies.to_csv('temp.csv',columns=['Genres'],index =False,header=False)

ratings = pd.read_csv('ml-100k/u.data', sep='\t')
users = pd.read_csv('ml-100k/u.user', sep='|')


user_item = pd.DataFrame(np.nan, index=range(0,len(users)+1), columns=range(0,len(movies)+1))

for k in ratings.index:
    u = ratings.ix[k].UserID
    i = ratings.ix[k].MovieID
    user_item.loc[u,i] = ratings.ix[k].Rating
    
user_item.to_csv('user_item.csv',index =False,header=True)

'''
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
'''