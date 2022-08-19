from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)

# Conexion MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'nombre_base_de_datos'

conexion = MySQL(app)

@app.before_request
def before_request():
    print("Antes de la repeticion")
    
@app.after_request
def after_request(response):
    print("Despues de la repeticion")
    return response

#Esta es una forma de crear un enlace a traves del decorador '@'
@app.route('/')
def index():
    #return "<h1>ajaja mundo- sub</h1>"
    cursos = ['PHP', 'Python', 'Java', 'kotlin', 'Dart', 'javascript']
    data={
        'titulo':'Index',
        'bienvenida':'Saludo',
        'cursos':cursos,
        'nro_Cursos':len(cursos),
    }
    return render_template('index.html', data=data)

#url dinamica
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo':'Contacto',
        'nombre':nombre,
        'edad':edad,
    }
    return render_template('contacto.html', data=data)
    
def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))

    return "ok"

@app.route('/cursos')
def listar_cursos():
    data={}
    try:
        cursor=conexion.connecition.cursor()
        sql='SELECT codigo, nombre, creditos FROM curso ORDER BY nombre ASC'
        cursor.execute(sql)
        cursos=cursor.fetchall()
        dat['cursos'] = cursos
        data['mensake']='Exito'
    except Exeption as ex:
        data['mensaje']='Error...'
    
    return jsonify(data)

def paginaNoEncontrada(error):
    #return render_template('404.html'), 404
    
    #Esta linea hara que la pagina de error se redirija al index
    return redirect(url_for('index'))
    
if __name__=='__main__':
    #Esta es otra forma de crear un enlace a traves de una regla de url
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, paginaNoEncontrada)
    app.run(debug=True, port=5000)