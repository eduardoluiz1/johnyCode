# bibliotecas = pacotes de códigos
# pip install pyautogui

import pyautogui
import time

# pyautogui.click - clica
# pyautogui.write - escreve um texto
# pyautogui.press - aperta uma tecla
# pyautogui.hotkey - aperta um atalho (hotkey)
# Colocaremos o comando PAUSE do pyautogui para ter um tempo entre os comandos e uma segurança na execução.
pyautogui.PAUSE = 0.09 # por enquanto o menor tempo
# Criaremos uma variável "link" para armazenar a informação do link. variável é dar um nome para um valor que iremos utilizar no código
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# abriria o navegador
pyautogui.press("win") #textos precisam estar entre aspas, o restante não precisa 
pyautogui.write("edge")
time.sleep(0.3)
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey("ctrl", "l")
# no meu caso, para usar o chrome preciso clicar no usuário que está utilizando (William o Talita) para acessar
pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior para o site carregar. usaremos o "time.sleep" para um tempo antes de colocar o login
time.sleep(3) # por padrão ele contabiliza 3 segundos

# Passo 2: Fazer login
#clicar no campo de email1    
# pyautogui.click(x=603, y=458)
pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") #passar para o próximo campo
pyautogui.write("minha senha") # digitar a senha
pyautogui.press("tab") # passar para o botão
pyautogui.press("enter")
# fazer uma pausa maior para o site carregar    

time.sleep(4)

# Passo 3: Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl (pandas = trabalha com base de dados, openpyxl = permite o pandas em trabalhar com base de dados em excel)
import pandas # salvar as informações da pasta "produto" dentro de uma variável

tabela = pandas.read_csv("produtos.csv") # ler as informações da base de dados e armazenar na variável tabela
print(tabela)

# para cada(for) linha(nome que você escolhe) dentro(in) da minha tabela eu quero executar todas a linhas abaixo(.index:)
# .index quer dizer que o programa irá percorrer cada linha da minha tabela começando pela zero. se fosse coluna seria coluns
# o nome "linha" depois do for é uma variável que você escolhe conforme informação que irá precisar
# o espaço que fica em cada linha é chamado na programação de indentação. é uma margem que significa oq será repetido várias vezes no for
# selecionar todas as linhas que o for irá repetir e pressione a tecla tab. caso não selecione alguma entre outras, pode dar erro
# no python ele não conta o cabeçalho como uma linha, somente onde tem conteúdo, assim que enxerga a base de dados.
for linha in tabela.index: # se ficar vermelho o nome do programa (codigo.py) faltou selecionar as informações que o "for" irá repetir
    # Passo 4: Cadastrar 1 produto
    # cadastrar código
    pyautogui.click(x=599, y=313) # clicar no campo do código
    # codigo = str(tabela.loc[linha, "codigo"]) # localizar entre conchetes. para localizar cria uma variável onde irá percorrer linha e coluna
    codigo = str(tabela.loc[linha, "codigo"])
    time.sleep(1)
    pyautogui.write(codigo) # escrever o primeiro código
    pyautogui.press("tab") # passar para o próximo campo de cadastro
    # cadastrar marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab") # passar para o próximo campo
    # cadastrar tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab") # passar para o próximo campo
    # cadastrar catagoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab") # passar para o próximo campo
    # cadastrar preco_unitario
     # o nome da coluna que vai localizar precisa ser exatamente o mesmo da tabela
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab") # passar para o próximo campo
    # cadastrar custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab") # passar para o próximo campo
    # cadastrar obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": # se obs for diferente (!=) de nan, cadastra, caso não seja, passa para o próximo
        pyautogui.write(obs)
    pyautogui.press("tab") # passar para o botão enviar
    pyautogui.press("enter") # clicar em enviar e cadastrar o produto
    #time.sleep(0.5)

    # voltar para o inicio da tela
    pyautogui.scroll(5000) # colocar um valor do scroll muito alto para não precisar ficar testando. valor + é para cima e - para baixo

# Passo 5: Repetir o passo 4 até acabar a lista de produtos

# texto na programação chamamos de string. e como na programação so faz a leitura de texto, é necessário transformar números em texto
# exemplo: "1" = str(1)
# não é necessário fazer em tudo, mas por precaução vamos colocar string (str) em todas a informações da busca
# NaN = Not a number = Valor Vazio

