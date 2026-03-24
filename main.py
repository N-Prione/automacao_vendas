import pyautogui
import pandas
import time

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome', interval=0.1)
pyautogui.press('enter')

link = 'https://forms.gle/1xLikaYvZShyqDdZA'
pyautogui.write(link, interval=0.1)
pyautogui.press('enter')
time.sleep(3)

dados = pandas.read_csv('vendas.csv')

for linha in dados.index:
    pyautogui.click(x=707, y=383)

    nome = dados.loc[linha, 'nome']
    pyautogui.write(str(nome))
    pyautogui.press('tab')

    cidade = dados.loc[linha, 'cidade']
    pyautogui.write(str(cidade))
    pyautogui.press('tab')

    contato = dados.loc[linha, 'contato']
    pyautogui.write(str(contato))
    pyautogui.press('tab')

    email = dados.loc[linha, 'email']
    pyautogui.write(str(email))
    pyautogui.press('tab')

    linha_impl = dados.loc[linha, 'linha']
    pyautogui.write(str(linha_impl))
    pyautogui.press('tab')
  
    marca = dados.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    peca = dados.loc[linha, 'peca']
    pyautogui.write(str(peca))
    pyautogui.press('tab')

    qtd = dados.loc[linha, 'quantidade']
    pyautogui.write(str(qtd))
    pyautogui.press('tab')

    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=709, y=275)
    time.sleep(2)