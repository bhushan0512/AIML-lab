import pandas as pd

def create_series():
    data = list(map(float, input("Enter values separated by space: ").split()))
    series = pd.Series(data)
    print(series)

create_series()
