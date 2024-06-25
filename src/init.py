from flask import Flask, render_template

app=Flask(__name__)

# Manejador de error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('pages/404.html')

# Rutas del sitio web
@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/habitaciones')
def habitaciones():
    return render_template('pages/habitaciones.html')

@app.route('/nosotros')
def nosotros():
    return render_template('pages/nosotros.html')

# Rutas del apartado administrador
@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/habitaciones')
def admin_habitaciones():
    return render_template('admin/habitaciones.html')

# Corriendo la aplicación
if __name__ == '__main__':
    app.run(debug=True)
