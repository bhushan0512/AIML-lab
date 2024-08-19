import pandas as pd

def series_to_list():
    data = list(map(float, input("Enter values separated by space: ").split()))
    series = pd.Series(data)
    series_list = series.tolist()
    print("List:", series_list)
    print("Type:", type(series_list))

series_to_list()
