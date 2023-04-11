import pymysql as mySQL
import pickle
from filtro import Filtro


def Conectar():
    arch = open("claves.dll","rb")
    usu = pickle.load(arch)
    arch.close()
    usuario = usu[0:4]
    clave = usu[5:9] 
    conectar = mySQL.connect(user=usuario, password=clave, host="localhost", db="sakila")
    return conectar
    
def CrearTablas(titulo):
    conexion = Conectar()
    cursor = conexion.cursor()
    cursor.execute("Show tables;")
    for ren in cursor.fetchall():
        EscribirTablas(ren,cursor,titulo)
    conexion.close()
    print("Copia de datos creada... (Encontrar como:  "+titulo+".sql)")
    
    
def EscribirTablas(ren, cursor,titulo):
    with open(titulo+".sql","a") as arch:
        for tabla in ren:
            arch.write("DROP TABLE IF NOT EXITS "+tabla+";\n")
            arch.write("CREATE TABLE "+tabla+"(\n")
            cursor.execute("Describe "+tabla+";")
            for atributo in cursor.fetchall():
                atrib = Filtro(atributo)
                arch.write(atrib+", \n")
            arch.write(") ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;\n\n")
            
        arch.close()
    
def CrearShema(titulo):
    with open(titulo+".sql","a") as arch:
        arch.write("DROP DATABASE IF EXISTS '"+titulo+"';\n")
        arch.write("CREATE DATABASE IF NOT EXISTS '"+titulo+"';\n")
        arch.write("USE '"+titulo+"';\n")
        arch.close()

def Filtro(atributo):
    not_Null = str (atributo).replace("NO","NOT NULL")
    yes_Null = not_Null.replace("YES","NULL")
    primaryKey = yes_Null.replace("PRI","PRIMARY KEY")
    parentesis = primaryKey.replace("(","")
    parentesis2 = parentesis.replace(")","")
    comillas = parentesis2.replace("''","")
    comillas1 = comillas.replace("'","")
    comillas2 = comillas1.replace(" '","")
    comas = comillas2.replace(","," ")
    none = comas.replace("None","")
    #Varchars
    varchar10= none.replace("varchar10","VARCHAR(10)")
    varchar20 = varchar10.replace("varchar20","VARCHAR(20)")
    varchar50 = varchar20.replace("varchar50","VARCHAR(50)")
    varchar45 = varchar50.replace("varchar45","VARCHAR(45)")
    varchar25 = varchar45.replace("varchar25","VARCHAR(25)")
    varchar91 = varchar25.replace("varchar91","VARCHAR(91)")
    varchar128 = varchar91.replace("varchar128","VARCHAR(128)")
    varchar6 = varchar128.replace("varchar6","VARCHAR(6)")
    varchar16 = varchar6.replace("varchar16","VARCHAR(16)")
    varchar95 = varchar16.replace("varchar95","VARCHAR(95)")
    #Otros
    smallint = varchar95.replace("smallint","SMALLING")
    text = smallint.replace("text","TEXT")
    timestamp = text.replace("timestamp","TIMESTAMP")
    tinyint = timestamp.replace("tinyint","TINYINT")
    datetime = tinyint.replace("datetime","DATETIME")
    year = datetime.replace("year","YEAR")
    inte = year.replace("int","INT")
    geometry = inte.replace("geometry","GEOMETRY")
    decimal27 = geometry.replace("decimal27","DECIMAL(27)")
    decimal4 = decimal27.replace("decimal4","DECIMAL(4)")
    decimal5 = decimal4.replace("decimal5","DECIMAL(5)")
    
    return decimal5
        

        
        

    