from flask import Flask, request

app = Flask(__name__)

senha_correta = "777"

@app.route("/")
def inicio():
    return '''
        <h2>Login</h2>
        <form method="POST" action="/login">
            <input type="password" name="senha" placeholder="Digite a senha">
            <button type="submit">Entrar</button>
        </form>
    '''

@app.route("/login", methods=["POST"])
def login():
    senha = request.form.get("senha")

    if senha == senha_correta:
        return "Login realizado com sucesso!"

    return "Senha incorreta!"

if __name__ == "__main__":
    app.run()