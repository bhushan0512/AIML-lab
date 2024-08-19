import pandas as pd

def compare_series():
    data1 = list(map(float, input("Enter values for Series 1 separated by space: ").split()))
    data2 = list(map(float, input("Enter values for Series 2 separated by space: ").split()))
    series1 = pd.Series(data1)
    series2 = pd.Series(data2)
    
    print("Equality:\n", series1 == series2)
    print("Greater Than:\n", series1 > series2)
    print("Less Than:\n", series1 < series2)

compare_series()
