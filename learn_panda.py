import pandas as pd

def pula():
    print()


df = pd.read_csv("Gapminder.csv", error_bad_lines=False, sep=';')
print(df.head()) #Visualizando as 5 primeiras linhas

df = df.rename(columns={"country": "Pais",  "continent": "continente", "year": "Ano", "lifeExp": "Expectativa de vida", "pop": "Pop Total", "gdpPercap": "PIB"})# renomeando as colunas
pula()
print(df.head(10))
pula()
print(df.shape)#Total de linhas e colunas
pula()
print(df.columns)#mostrar os nomes das colunas
pula()
print(df.dtypes)# mostra os tipos de cada coluna
pula()
print(df.tail())# mostra as ultimas linhas
pula()
print(df.describe())# retoina informações estatisticas
pula()
print(df['continente'].unique()) #retorna os volores dos continentes
Oceania = df.loc[df["continente"] == 'Oceania'] # serve para fazer filtros no banco de dados
pula()
print(Oceania.head())
pula()
print(df.groupby("continente")["Pais"].nunique())#tras uma contagem de qnt tem para cada continente
pula()
print(df.groupby("Ano")["Expectativa de vida"].mean())
pula()
print(df["PIB"].mean())#tras a media 
pula()

df.info()# traz os tipos de dado, os volumes de dados com informações nula e o tamanho do volume d dados