import numpy as np

def calculate(arr):
    if len(arr) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.reshape(arr, (3,3))
    
    mean = [list(np.mean(arr, 0)), list(np.mean(arr, 1)), np.mean(arr)]
    variance = [list(np.var(arr, 0)), list(np.var(arr, 1)), np.var(arr)]
    st_dev = [list(np.std(arr, 0)), list(np.std(arr, 1)), np.std(arr)]
    _max = [list(np.max(arr, 0)), list(np.max(arr, 1)), np.max(arr)]
    _min = [list(np.min(arr, 0)), list(np.min(arr, 1)), np.min(arr)]
    _sum = [list(np.sum(arr, 0)), list(np.sum(arr, 1)), np.sum(arr)]
    
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': st_dev,
        'max': _max,
        'min': _min,
        'sum': _sum
    }
    
    return calculations