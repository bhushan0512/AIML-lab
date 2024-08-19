import numpy as np
import pandas as pd

def numpy_to_series():
    data = np.array(list(map(float, input("Enter 5 values separated by space: ").split())))
    series = pd.Series(data)
    print(series)

numpy_to_series()
