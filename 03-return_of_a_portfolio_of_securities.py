import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers = ['AAPL', 'AMZN', 'TSLA', 'JPM', 'JNJ']

# Create an empty dataframe
mydata = pd.DataFrame()

# Get the historical data for each stock and add it to the dataframe
for t in tickers:
    mydata[t] = yf.download(t, start='2023-01-01', end='2023-05-11')['Adj Close']

# Print the dataframe information
print(mydata.info())
print(mydata.head())
print(mydata.tail())

# Calculate the daily returns
returns = mydata.pct_change()

# Define the weights for the portfolio
weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

# Calculate the annualized average return for each stock and the portfolio
annual_returns = returns.mean() * 89
portfolio_return = np.dot(annual_returns, weights)

# Print the annualized average return for the portfolio
print(f"Portfolio return: {portfolio_return:.2%}")

# Print the annualized average return for each stock
(mydata / mydata.iloc[0] * 100).plot(figsize=(15,6))
plt.show()
