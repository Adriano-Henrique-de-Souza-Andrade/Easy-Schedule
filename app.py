from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'aws.connect.psdb.cloud'
app.config['MYSQL_USER'] = 'zqghdq1xlwsdlkyrj1nq'
app.config['MYSQL_PASSWORD'] = 'pscale_pw_fnTtNLxbWnrV79oZZLNUmWX1neJvCXRW7pN9PCOEpP9'
app.config['MYSQL_DB'] = 'mps_agenda'
 
mysql = MySQL(app)

# Rota para o formulário de cadastro
@app.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    if request.method == "POST":
        # Obter dados do formulário
        nome = request.form["nome_input"]
        email = request.form["email_input"]
        senha = request.form["senha_input"]

        # Consulta para obter o valor máximo atual de usuario_id
        cursor = db.cursor()
        cursor.execute("SELECT MAX(usuario_id) FROM agenda_users")
        result = cursor.fetchone()
        usuario_id = result[0] + 1 if result[0] else 1

        # Inserir novo registro na tabela agenda_users
        sql = """
            INSERT INTO agenda_users (usuario_id, usuario_nome, usuario_email, usuario_status, usuario_senha)
            VALUES (%s, %s, %s, 'ativo', %s)
        """
        values = (usuario_id, nome, email, senha)
        cursor.execute(sql, values)
        db.commit()

        # Exibir mensagem de sucesso
        flash("Cadastro realizado com sucesso!")

    return render_template("cadastro.html")

if __name__ == '__main__':
    app.run()