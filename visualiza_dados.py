import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
"""
#Upload do arquivo no google colab
from google.colab import files
arq = files.upload()
"""
# Criando nosso DataFrame
df = pd.read_excel('AdventureWorks.xlsx')

# Visualizando as 5 primeiras linhas
df.head()

# Quantidade de linhas e colunas
df.shape

# Verificando os tipos de dados
df.dtypes

#Qual a Receita total?
df['Valor Venda'].sum()

# Qual o custo Total?
df['Custo'] = df['Custo Unitário'].mul(df['Quantidade'])# Criando a coluna de custo

df.head(1)

# Qual o custo total?
round(df['Custo'].sum(), 2)

# Agora que temos a receita e custo e o toal, podemos achar o Lucro total
#Vamos criar uma coluna de Lucro que será Receita - Custo
df['lucro'] = df['Valor Venda'] - df['Custo']

df.head(1)

#Total Lucro
round(df['lucro'].sum(), 2)

#Criando uma coluna com totla de dias para enviar o produto
df['Tempo_envio'] = df['Data Envio'] - df['Data Venda']

df.head(1)

# AGORA, QUEREMOS SABER A MÉDIA DO TEMPO DE ENVIO PARA CADA MARCA, E PARA ISSO PRECISAMOS TRANSFORMAR A COLUNA TEMPO_ENVIO EM NUMERICA
# Extraindo apenas os dias
df['Tempo_envio'] = (df['Data Envio'] - df['Data Venda']).dt.days
df.head(1)

# Verificando o tipo da coluna Tempo_envio
df['Tempo_envio'].dtypes

#Média do tempo de envio por hora
df.groupby('Marca')['Tempo_envio'].mean()

# Missing Values

# Verificando se temos dados faltantes
df.isnull().sum()

# E,se a gente quiser saber o Lucro por Ano e Por Marca?

# Vamos agrupar por ano e marca
df.groupby([df['Data Venda'].dt.year, "Marca"])['lucro'].sum()

# Configura o formato dos numeros float
pd.options.display.float_format ='{:20,.2f}'.format

#Resetando o index
lucro_ano = df.groupby([df['Data Venda'].dt.year, 'Marca'])['lucro'].sum().reset_index()
lucro_ano

#Qual o total de produtos vendidos?
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)

#Gráfico total de produtos vendidos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.barh(title='Total Produtos vendidos')
plt.xlabel('Total')
plt.ylabel('Produto');

df.groupby(df['Data Venda'].dt.year)['lucro'].sum().plot.bar(title='Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Receita');

df.groupby(df['Data Venda'].dt.year)['lucro'].sum()

#Selecionando apenas as vendas de 2009
df_2009 = df[df['Data Venda'].dt.year == 2009]
df_2009.head()

df_2009.groupby(df_2009['Data Venda'].dt.month)['lucro'].sum().plot(title='Lucro x Mês')
plt.xlabel('Marca')
plt.ylabel('Lucro');

df_2009.groupby('Marca')['lucro'].sum().plot.bar(title='Lucro x Marca')
plt.xlabel('Marca')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal');

df_2009.groupby('Classe')['lucro'].sum().plot.bar(title='Lucro x Marca')
plt.xlabel('Classe')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal');

df['Tempo_envio'].describe()

#Grafico de Boxplot
plt.boxplot(df['Tempo_envio']);

# Histogrma
plt.hist(df['Tempo_envio']);

#Tempo minimo de envio
df['Tempo_envio'].min()

#Tempo maximo de envio
df['Tempo_envio'].max()

#Identificando o Outlier
df[df['Tempo_envio'] == 20]

# Salvando em csv
df.to_csv('df_vendas_novo.csv', index=False)


#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