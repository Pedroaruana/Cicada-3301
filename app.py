from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'cicada-3301-secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/instrucoes')
def instrucoes():
    return render_template('instrucoes.html')

@app.route('/fase/1')
def fase1():
    return render_template('fase1.html')

@app.route('/fase/x7k2m9q3p5r8t4v6wz')
def fase2():
    return render_template('fase2.html')

@app.route('/fase/p3n8w')
def fase3():
    return render_template('fase3.html')

@app.route('/fase/sombra')
def fase4():
    return render_template('fase4.html')

@app.route('/fase/nexus')
def fase5():
    return render_template('fase5.html')

@app.route('/fim')
def fim():
    return render_template('fim.html')

@app.route('/boas-vindas')
def boas_vindas():
    return render_template('boas-vindas.html')

@app.route('/fazer-parte')
def fazer_parte():
    return render_template('fazer-parte.html')

@app.route('/certificado', methods=['POST'])
def certificado():
    nome = request.form.get('nome', '')
    pais = request.form.get('pais', '')
    estado = request.form.get('estado', '')
    cidade = request.form.get('cidade', '')
    data = datetime.now().strftime('%d/%m/%Y')
    return render_template('certificado.html',
                           nome=nome, pais=pais, estado=estado,
                           cidade=cidade, data=data)

@app.route('/confidencial')
def confidencial():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return render_template('confidencial.html', ip=ip)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
