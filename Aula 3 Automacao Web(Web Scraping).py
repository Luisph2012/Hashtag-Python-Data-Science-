# Pegar Cotacao do Dolar, Euro, Ouro e atualizar o preco
# Passo 1: Pegar a cotacao do dolar
# Passo 2: Pegar a cotacao do Euro
# Passo 3: Pegar a cotacao do ouro
# Passo 4: Importar Base de Dados
# Passo 5: Atualizar Cotacao, Preco de Compra e Preco de Venda
# Passo 6: Exportar o relatorio atualizado

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from IPython.display import display

navegador = webdriver.Chrome("Arquivos/Aula 3/chromedriver.exe")
# Passo 1 Pegar Cotacao Dolar

# Entrar em um (selenium) site webdriver.get ()
navegador.get("https://www.google.com")

# Pesquisar Cotacao Dolar (.click () clicar... .send_keys(escrever).. get_attribute() pegar o valor.. ID, Class, e etc
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys(
    "cotacao dolar")
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys(
    Keys.ENTER)
# Pegar as Informacoes do dolar
cotacao_dolar = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Euro
navegador.get("https://www.google.com")
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys(
    'cotacao euro')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys(
    Keys.ENTER)
cotacao_euro = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Ouro

navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')

print('Cotacao: {} , {}, {}'.format(cotacao_dolar, cotacao_euro, cotacao_ouro))

# Import Base de Dados

import pandas as pd

table = pd.read_excel('Arquivos/Aula 3/Produtos.xlsx')
display(table)

#Passo 5 Atualizar cotacao

table["Moeda"] == 'Dólar'

table.loc[table["Moeda"] == 'Dólar', 'Cotação'] =  float(cotacao_dolar)
table.loc[table["Moeda"] == 'Euro' , 'Cotação'] =  float(cotacao_euro)
table.loc[table["Moeda"] == 'Ouro' , 'Cotação'] =  float(cotacao_ouro)


#Atualizar Preco de compra = Preco Original * Cotacao
#atualizar preco de venda = Preco de compra * Margem

table['Preço Base Reais'] = table['Preço Base Original'] * table['Cotação']
table['Preço Final'] = table['Preço Base Reais'] * table['Margem']

#Formatar

table['Preço Base Original'] = table['Preço Base Original'].map('R$ {:.2f}'.format)
table['Preço Base Reais'] = table['Preço Base Reais'].map('R$ {:.2f}'.format)
table['Preço Final'] = table['Preço Final'].map('R$ {:.2f}'.format)


#Exportar Tabela

table.to_excel('Arquivos/Aula 3/Produtos_Novo.xlsx', index=False)
navegador.quit()


