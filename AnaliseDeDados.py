import pandas as pd
import os
import plotly.express as px


# Percorrer todos os arquivos da pasta base de dados(pasta Vendas)

lista_arquivo = os.listdir("C://Users/Público/Downloads/Vendas")


frame = []
# Importar as bases de dados de vendas

for arquivo in lista_arquivo:
 if "Vendas" in arquivo:
  tabela = pd.read_csv(f"C://Users/Público/Downloads/Vendas/{arquivo}")
  frame.append(tabela)
tabela_total = pd.concat(frame)

# Compilar base de dados

tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)


# Calcular Produtos(Faturamento):

tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)


#Calcular Loja que mais vendeu

tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas= tabela_lojas[["Faturamento"]]
print(tabela_lojas)

#Criar Gráficos

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento")
grafico.show()












