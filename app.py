from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/quem_somos')
def quem_somos():
    return render_template('quem_somos.html')

@app.route('/gato_salem')
def gato_salem():
    return render_template('gato_salem.html')

@app.route('/gato_espoleta')
def gato_espoleta():
    return render_template('gato_espoleta.html')

@app.route('/gato_pipoca')
def gato_pipoca():
    return render_template('gato_pipoca.html')

@app.route('/gato_lola')
def gato_lola():
    return render_template('gato_lola.html')

@app.route('/gato_aurora')
def gato_aurora():
    return render_template('gato_aurora.html')

@app.route('/gemini')
def gemini():
    return render_template('gemini.html')

app.run()