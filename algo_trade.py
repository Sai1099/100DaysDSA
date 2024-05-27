import pandas as pd
import numpy as np
import math 
import requests


stocks = pd.read_csv('sp_500_stocks.csv')
from secrets import IEX_CLOUD_API_TOKEN


symbol = 'AAPL'
url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
print(url)
data = requests.get(url)
print(data.status_code)


import pandas as pd