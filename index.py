from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Servicio')
def servicio():
    return render_template('servicio.html')

@app.route('/Nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/BestRouter')
def bestRouter():
    return render_template('bestRouter.html')

if __name__ == '__main__':
    app.run(debug=True)
