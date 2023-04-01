from flask import Flask, request, render_template, flash
from database import engine

app = Flask(__name__)
app.secret_key = "mysecretkey"

# Rota para o formulário de cadastro
@app.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    if request.method == "POST":
        # Obter dados do formulário
        nome = request.form["nome_input"]
        email = request.form["email_input"]
        senha = request.form["senha_input"]

        with engine.connect() as conn:
            # Consulta para obter o valor máximo atual de usuario_id
            result = conn.execute(text("SELECT MAX(usuario_id) FROM agenda_users"))
            usuario_id = result.fetchone()[0] + 1

            # Inserir novo registro na tabela agenda_users
            sql = """
                INSERT INTO agenda_users (usuario_id, usuario_nome, usuario_email, usuario_status, usuario_senha)
                VALUES (:usuario_id, :nome, :email, 'ativo', :senha)
            """
            values = {"usuario_id": usuario_id, "nome": nome, "email": email, "senha": senha}
            conn.execute(text(sql), values)

        # Exibir mensagem de sucesso
        flash("Cadastro realizado com sucesso!")

    return render_template("cadastro.html")
