from flask import Flask, render_template

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

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
