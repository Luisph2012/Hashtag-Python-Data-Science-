import pyautogui as autogui
import pyperclip
import time
import pandas as pd
import openpyxl

autogui.press('winleft')
autogui.write('edge')
autogui.press('Enter')

time.sleep(2)

autogui.hotkey('winleft', 'up')


pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing%27')
autogui.hotkey('ctrl','v')
autogui.press('Enter')
time.sleep(5)

autogui.click(x=336, y=249, clicks=4)
time.sleep(4)

autogui.click(x=353, y=255)
time.sleep(2)
autogui.click(x=1713, y=154)
time.sleep(3)

autogui.click(x=1448, y=521)

autogui.click(x=1447, y=567)
autogui.click(x=1447, y=567)

time.sleep(5)
datasheet =pd.read_excel('C:\\Users\phili\Downloads\Vendas - Dez.xlsx')

faturamento =datasheet['Valor Final'].sum()
total_itens =datasheet['Quantidade'].sum()


autogui.hotkey('ctrl','t')
autogui.click(x=458, y=54)
pyperclip.copy('www.gmail.com')
autogui.hotkey('ctrl','v')
autogui.press('Enter')
time.sleep(5)
autogui.click(x=76, y=177)
autogui.click(x=76, y=177)
pyperclip.copy('philipevilara@gmail.com')
autogui.hotkey('ctrl','v')
time.sleep(3)
autogui.press('tab')
pyperclip.copy('Relatório do Mês')
autogui.hotkey('ctrl','v')
autogui.press('tab')

texto ="""
Olá!
Bom Dia!
Relatório geral:

Faturamento:{:.2f}
Total de Itens Vendidos:{:.2f}

Agradecimentos 

Luis Philipe 
""".format(faturamento,total_itens)
pyperclip.copy(texto)
autogui.hotkey('ctrl','v')
autogui.hotkey('ctrl','enter')