from flask import Flask, render_template, request 
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'amanda1',
        password= 'eliti',
        database = 'testebd'
    )
@app.route('/singup', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def singup():
    if request.method == 'POST':
        nome=request.form['nome']
        email=request.form['email']
        senha=request.form['senha']
        conexao=get_db_connection()
        cursor=conexao.cursor()
        cursor.execute(
            'INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)',
            (nome, email, senha)
        )
        conexao.commit()
        cursor.close()
        conexao.close()
        return "Cadastro concluido!"
    return render_template('singup.html')

if __name__ == '__main__':
    app.run (debug=True)