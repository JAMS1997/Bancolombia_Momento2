from flask import Flask, render_template,request,redirect,url_for
#Establecer conexion con la base de datos
from flask_mysqldb import MySQL

from config import config
##Crear la aplicacion
app=Flask(__name__)

##Base de datos
db = MySQL(app)

##Configuracion de rutas
@app.route('/')
def index():
    return  redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login(): ##definir nombre de una vista
    if request.method=="POST":
        print(request.form['username'])
        print(request.form['password'])
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


if __name__ =='__main__':
    app.config.from_object(config['development'])
    app.run()