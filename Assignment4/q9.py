import pandas as pd

def dict_to_series():
    empno = int(input("Enter employee number: "))
    ename = input("Enter employee name: ")
    basic = float(input("Enter basic salary: "))
    data = {'empno': empno, 'ename': ename, 'basic': basic}
    series = pd.Series(data)
    print(series)

dict_to_series()
