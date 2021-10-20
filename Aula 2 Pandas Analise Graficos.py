import pandas as pd
import numpy
from IPython.display import display
import plotly.express as px

tabela = pd.read_csv(r'E:\Programmer\Estudos\Extra\Python\Aulas Intensivao\Aula 2\telecom_users.csv')
tabela = tabela.drop('Unnamed: 0', axis=1)

# axis = 0 para linha,1 para coluna
# How = all tira as infos que tem todos os valores Vazios, How = Any tira as infos que tem pelo menos 1 valor vazio


tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

tabela = tabela.dropna(how='all', axis=1)

tabela = tabela.dropna(how='any', axis=0)

print(tabela.info())

print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True))
# printa as informações da coluna (normalize) = em decimal


# analise mais completa
print(tabela['Churn'].value_counts(normalize=True).map("{:.1%}".format))  # em porcentagem
tabela2 = tabela['Churn']  # mostrar uma tabela só com a informação do churn

grafico = px.histogram(tabela, x=tabela2)  # Cor

for coluna in tabela.columns:  # color = '' tabela em marca dagua
    grafico = px.histogram(tabela, x=coluna, color='Churn', color_discrete_sequence=['black', 'red'])
    # fica um grafico em backgroud

    grafico.show()  #mostra o gráfico
