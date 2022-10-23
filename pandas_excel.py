import pandas as pd
import matplotlib.pyplot as plt

# leitura de arquivos
df1 = pd.read_excel('Aracaju.xlsx')
df2 = pd.read_excel('Fortaleza.xlsx')
df3 = pd.read_excel('Natal.xlsx')
df4 = pd.read_excel('Recife.xlsx')
df5 = pd.read_excel('Salvador.xlsx')

#print(df1.head())
#Juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])
"""
# retorna as 5 primeiras linhas
#print(df.head())

# retorna as 5 ultimas linhas
#print(df.tail())

# exibe 5 linhas aleatorias
#print(df.sample(5))

# Verificando o tipo de cada coluna
print(df.dtypes)

#Alterando o tipo de dado da coluna LojaID
df['LojaID'] = df['LojaID'].astype('object')
print(df.dtypes)

# Consultando linhas com valores faltantes
print(df.isnull().sum())

#Substituindo os valores nulos pela media
df['Vendas'].fillna(df['Vendas'].mean(), inplace=True)
print(df.isnull().sum())

#Substituindo os valores nulos por 0
df['Vendas'].fillna(0, inplace=True)

# Apagando as linhas com valores nulos
df.dropna(inplace=True)

# Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(inplace=True)

#Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how='all', inplace=True)

#CRIANDO NOVAS COLUNAS

#Crinado colunas de receita
df['Receita'] = df['Vendas'].mul(df('Qtde'))

#Para achar a quantidade
df['Receita/Vendas'] = df['Receita'] / df['Vendas']

#Retornando a maior receita
df['Receita'].max()

#Retornando a menos receita
df['Receita'].min()

#nlargest retorna as maiores receitas
df.nlargest(3, 'Receita')

#nsamlargest retorna as menores receitas
df.nsmallest(3, 'Receita')

#Agrupamento por cidade
df.groupby('Cidade')['Receita'].sum()

#Ordenando o conjunto de dados 
df.sort_values('Receita',ascending=False).head(10)# ascending=False traz do maior para o menor

#Trabalhando com Datas

#Transformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype('int64')

#Transformando coluna de data em data
df['Data'] = pd.to_datetime(df['Data'])

df.dtypes # mostra o tipo de dado

# Agrupando por ano
df.groupby(df['Data'].dt.year)['Receita'].sum()

#Criando uma nova coluna ano
df['Ano_Venda'] = df['Data'].dt.year

df.sample(5)

#Extraindo o mês e o dia
df['mes_venda'], df['dia_venda'] = (df['Data'].dt.mouth, df['Data'].dt.day)

df.sample(5)

#Retornando a data mais antiga
df['Data'].min()

#Calculando a diferencade dias
df['diferenca_dias'] = df['Data'] - df['Data'].min()

df.sample(5)

#Criando a coluna de trimestre
df['trimestre_venda'] = df['Data'].dt.quarter

#Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df['Data']).dt.year == 2019] & (df['Data'].dt.mouth == 3)
print(vendas_marco_19)

#Visualização de dados
#df['LojaID'].value_counts(ascending=False) #faz uma contagem mostrando qm vendeu mais

# Grafico de barras
df['LojaID'].value_counts(ascending=False).plot.bar()

#Grafico de barras horizontais
#df['LojaID'].value_counts().plot.barh()

# Graficos de barras horizontais
df['LojaID'].value_counts(ascending=True).plot.barh()

# Grafico de Pizza
df.groupby(df['Data'].dt.year)['Receita'].sum().plot.pie()

#Total vendas por cidade
df['Cidade'].value_counts()

#Adicionando um titulo e alterando o nome dos eixos
import matplotlib.pyplot as plt
df['Cidade'].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total vendas");

#Alterando a cor
df['Cidade'].value_counts().plot.bar(title="Total vendas por Cidade", color='red')
plt.xlabel("Cidade")
plt.ylabel("Total vendas");

#Alterando o estilo
plt.style.use("ggplot")
df.groupby(df['mes_vendas'])['Qtde'].sum().plot(title= "Totla Produtos vendidos x mês")
plt.xlabel('Mês')
plt.ylabel("Total produtos vendidos");
plt.legend()

# Tras o mês e a quantiidade de produtos vendidos naquele mês
df.groupby(df['mes_vendas'])['Qtde'].sum()

#Selecionando apenas as vendas de 2019
df_2019 = df[df['Ano_Vendas'] == 2019]

# Total produtos vendidos por mês
df_2019.groupby(df_2019['mes_vendas'])['Qtde'].sum().plot(marker = 'y')
plt.xlabel('Mês')
plt.ylabel('Total Produtod vendidos')
plt.legend(); #o : serve para não aparecer a fraseda lib mattplot

#Hisograma
plt.hist(df['Qtde'], color='orangered');

# grafico de dispersão
plt.scatter(x=df_2019['dia_venda'], y = df_2019["Receita"]);

# Salvando em png
df_2019.groupby(df_2019['mes_vendas'])['Qtde'].sum().plot(marker = 'v')
plt.title('Quantidade de produtos vendidos x mês')
plt.xlabel('Mês')
plt.ylabel('Total Produtos vendidos')
plt.legend();
plt.savefig('grafico QTDE x MES.png')
"""

