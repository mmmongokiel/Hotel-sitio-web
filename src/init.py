from flask import Flask, render_template

app=Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('pages/404.html')

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/habitaciones')
def habitaciones():
    return render_template('pages/habitaciones.html')

@app.route('/nosotros')
def nosotros():
    return render_template('pages/nosotros.html')

if __name__ == '__main__':
    app.run(debug=True)
