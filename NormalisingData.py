import numpy as np

def normalize(data):
    col_max = np.max(data, axis = 0)
    col_min = np.min(data, axis = 0)
    return np.divide(data - col_min, col_max - col_min)

x_norm = normalize(x)
