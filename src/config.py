class config:
    SECRET_KEY = 'SOYUNSECRETO' #Esta llave nos va a servir para el envio de mensajes a traves de la funcion flash propia de flask 'usuario no valido'

#Esta clase esta heredando la clase config
class DevelopmentConfig(config):
    DEBUG=True
#Conexion a la base de datos Mysql
    MYSQL_HOST ='localhost'
    MYSQL_USER='root'
    MYSLQ_PASSWORD=''
    MYSQL_DB='flask_login'

config = {
    'development':DevelopmentConfig
}