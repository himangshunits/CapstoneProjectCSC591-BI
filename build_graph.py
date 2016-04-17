import pandas as pd
import numpy as np

ratings = pd.read_csv('ml-1m_dataset/ratings.dat', sep='::')
movies = pd.read_csv('ml-1m_dataset/movies.dat', sep='::')
users = pd.read_csv('ml-1m_dataset/users.dat', sep='::')

cosine = np.zeros(shape=(6040,6040))

pearson = np.zeros(shape=(6040,6040))

print ratings
print ''
print movies
print ''
print users
