import pandas as pd
url = 'https://raw.githubusercontent.com/Muralimekala/python/master/Resp2.csv'
df1 = pd.read_csv(url)
# Dataset is now stored in a Pandas DataFrame

url = 'https://raw.githubusercontent.com/Muralimekala/python/master/Salaries.csv'
sf = pd.read_csv(url)
#slaries CSV
sf.head()

para acessar o luigi -> localhost:8082