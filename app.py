from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'cicada-3301-secret'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
