# Automação de Cadastro de Produtos

## Descrição

Este projeto utiliza a biblioteca `pyautogui` para automatizar o preenchimento de um formulário de cadastro de produtos em uma aplicação web. Os dados dos produtos são lidos a partir de um arquivo CSV, permitindo que o processo de inserção seja feito de maneira rápida e eficiente.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o script de automação.
- **PyAutoGUI**: Biblioteca para automação de interfaces gráficas, permitindo o controle do mouse e teclado.
- **Pandas**: Biblioteca para manipulação de dados, usada para ler o arquivo CSV com os produtos.

## Pré-requisitos

Antes de executar o projeto, você deve ter instalado:

- Python 3.x
- Bibliotecas necessárias:
  ```bash
  pip install pyautogui pandas
  ```

## Funcionalidades

- **Abertura do Navegador**: O script abre automaticamente o navegador Edge.
- **Login Automático**: Realiza o login em uma plataforma específica.
- **Leitura de Dados**: Lê os dados de um arquivo CSV (`produtos.csv`) contendo informações dos produtos.
- **Preenchimento de Formulário**: Preenche automaticamente o formulário de cadastro com os dados lidos do CSV.
- **Navegação**: Utiliza teclas de atalho e cliques para navegar entre os campos do formulário.

## Como Usar

1. **Configurar o Arquivo CSV**: Crie um arquivo chamado `produtos.csv` no mesmo diretório do script, com as seguintes colunas:
   - `codigo`
   - `marca`
   - `tipo`
   - `categoria`
   - `preco_unitario`
   - `custo`
   - `obs`

2. **Configurar o Script**: Abra o arquivo do script e ajuste os seguintes parâmetros, se necessário:
   - **E-mail e Senha**: Insira suas credenciais na seção de login.

3. **Executar o Script**: 
   - Execute o script Python:
   ```bash
   python seu_script.py
   ```

4. **Interagir com a Interface**: Após executar, o script realizará o login e começará a preencher os dados automaticamente. É importante não interferir durante a execução.

## Exemplo de Código

Aqui está um trecho do código que realiza o login e o preenchimento dos dados:

```python
import pyautogui
import time
import pandas

pyautogui.PAUSE = 1.5

# Abrir o navegador e acessar a página de login
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)
pyautogui.click(x=400, y=364)  # Ajuste as coordenadas conforme necessário
pyautogui.write('seu_email@exemplo.com')
pyautogui.press('tab')
pyautogui.write('sua_senha')
pyautogui.click(x=666, y=525)

# Ler o arquivo CSV
tabela = pandas.read_csv('produtos.csv')

# Preencher o formulário
for linha in tabela.index:
    # Preencher cada campo com os dados do CSV
    pyautogui.click(x=443, y=256)  # Clique para começar o preenchimento
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    # Continue preenchendo os outros campos...
```

## Considerações

- **Segurança**: Mantenha suas credenciais seguras e evite compartilhar seu script com informações sensíveis.
- **Coordenadas do Mouse**: As coordenadas usadas nas funções `click` podem variar dependendo da sua resolução de tela e da interface da aplicação. Ajuste-as conforme necessário.
- **Teste Inicial**: É recomendado realizar um teste em um ambiente de desenvolvimento antes de utilizar em produção.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: jennisaantiago@outlook.com

---

Esperamos que este projeto facilite o seu trabalho de cadastro de produtos!
