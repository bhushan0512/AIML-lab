import pandas as pd
import matplotlib.pyplot as plt

def plot_financial_data():
    data = pd.read_csv('financial_data.csv')
    plt.plot(data['Date'], data['Open'], label='Open')
    plt.plot(data['Date'], data['Close'], label='Close')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Financial Data of Alphabet Inc.')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_financial_data()
