import pandas as pd

def perform_operations():
    data1 = list(map(float, input("Enter values for Series 1 separated by space: ").split()))
    data2 = list(map(float, input("Enter values for Series 2 separated by space: ").split()))
    series1 = pd.Series(data1)
    series2 = pd.Series(data2)
    
    print("Addition:\n", series1 + series2)
    print("Subtraction:\n", series1 - series2)
    print("Multiplication:\n", series1 * series2)
    print("Division:\n", series1 / series2)

perform_operations()
