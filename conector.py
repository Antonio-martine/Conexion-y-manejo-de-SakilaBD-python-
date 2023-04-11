import pymysql as mySQL
import pickle

def Conectar(clave, usuario):
    arch = open("claves.dll","rb")
    usu = pickle.load(arch)
    arch.close()
    usuario = usu[0:4]
    clave = usu[5:9] 
    conectar = mySQL.connect(user=usuario, password=clave, host="localhost", db="sakila")
    return conectar


def ConsultaTabla():
conexion = Conectar()
cursor = conexion.cursor()
cursor.execute("Select * from actor")
for ren in cursor.fetchall():
    print(ren)
conexion.close()

#cur.execute( "SELECT nombre, apellido FROM usuarios" )
#for nombre, apellido in cur.fetchall() :
   #print nombre, apellido