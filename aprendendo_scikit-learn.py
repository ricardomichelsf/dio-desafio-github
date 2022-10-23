from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# gerando uma massa de dados:
x, y =make_regression(n_samples=200, n_features=1, noise=30)

#mostra grafico
plt.scatter(x, y)
plt.show()
# Criação do modelo
modelo = LinearRegression()

