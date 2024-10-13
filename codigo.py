import pyautogui
import time
import pandas #importar a base de dados

# pyautogui.write > escrever um texto
# pyautogui.click > clicar com o mouse
# pyautogui.press > apertar uma tecla
# pyautogui.hotkey > apertar um atalho do teclado (Ctrl, c)

pyautogui.PAUSE = 1.5

# abrir o navegador
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

# fazer login
pyautogui.press('enter')

# quero dar uma pausa de 3 segundos
time.sleep(3)
pyautogui.click(x=400, y=364)
pyautogui.write('jennisaantiago@outlook.com')

# passar para o proximo campo
pyautogui.press('tab')
pyautogui.write('minha senha aqui')

# apertar no botão de login
pyautogui.click(x=666, y=525)

time.sleep(2)

tabela = pandas.read_csv('produtos.csv')
print(tabela)

# executar o cadastro da tabela
for linha in tabela.index:
    pyautogui.click(x=443, y=256)
    # código
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # preco
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    # custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # observação
    # nan = Not a Number = vazio
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)
