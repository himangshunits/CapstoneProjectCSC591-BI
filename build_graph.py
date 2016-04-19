import sys
import collections
import time
import csv
import math
import copy
import numpy as np
import pandas as pd
import igraph as gp
from itertools import izip
from sklearn.metrics.pairwise import cosine_similarity
import colour
import build_similarity_matrices as bsm


def build_graph_from_matrices():
	