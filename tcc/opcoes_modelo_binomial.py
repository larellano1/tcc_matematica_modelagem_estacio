##Importar numpy, matplotlib, yfinance e pandas
import numpy as np
import yfinance as yf

##Definir função para calcular o preço de uma opção de compra
def preco_call(S, K, r, sigma, T, n):
    dt = T/n
    u = np.exp(sigma*np.sqrt(dt))
    d = 1/u
    p = (np.exp(r*dt)-d)/(u-d)
    C = np.zeros(n+1)
    for i in range(n+1):
        C[i] = max(S*(u**i)*(d**(n-i))-K, 0)
    for t in range(n-1, -1, -1):
        for i in range(t+1):
            C[i] = np.exp(-r*dt)*(p*C[i+1]+(1-p)*C[i])
    return C[0]



######### Utilização da Função #########


##Carregar dados do ativo PETR4.SA usando o yfinance
ativo = yf.Ticker("PETR4.SA")
dados = ativo.history(period="max")

##Calcular o logaritmo dos preços de fechamento
dados["log_retorno"] = np.log(dados["Close"]/dados["Close"].shift(1))

##Calcular a média e o desvio padrão dos logaritmos dos preços de fechamento
media = dados["log_retorno"].mean()
desvio_padrao = dados["log_retorno"].std()

##Calcular o desvio padrão anualizado
desvio_padrao_anualizado = desvio_padrao*np.sqrt(252)

##Obter ultimo preço de fechamento
ultimo_preco = dados["Close"][-1]

##Utilizar ultimo preco de fechamento, taxa livre de risco, desvio padrão anualizado 
##e tempo de vencimento para calcular o preço de uma opção de compra
preco_opcao = preco_call(S=ultimo_preco, K=30, r=0.01375, sigma=desvio_padrao_anualizado, T=1, n=300)
print(f'Ultimo Preço: {ultimo_preco} - Preço Opção: {preco_opcao}')

##Import matplotlib.pyplot
import matplotlib.pyplot as plt

##Use seaborn style
plt.style.use("seaborn")

##Plotar o gráfico de preços de fechamento
plt.plot(dados["Close"])
plt.title("Preço de Fechamento do Ativo PETR4.SA")
plt.xlabel("Data")
plt.ylabel("Preço de Fechamento")
plt.show()

##Plotar histograma de logaritmos dos preços de fechamento
plt.hist(dados["log_retorno"], bins=100)
plt.title("Histograma de Logaritmos dos Preços de Fechamento do Ativo PETR4.SA")
plt.xlabel("Logaritmo dos Preços de Fechamento")
plt.ylabel("Frequência")
plt.show()
