import pymysql as mySQL
import pickle
from filtro import (Filtro,FiltroPrimaryKey,ActorFiltro,FiltroColumna,
    AddressFiltro,CategoryFiltro,CityFiltro,CountyFiltro,CustomerFiltro,FilmFiltro,Film_Actor_Filtro,Film_Category,
    Film_Text, Inventory, Language)


def Conectar():
    arch = open("claves.dll","rb")
    usu = pickle.load(arch)
    arch.close()
    usuario = usu[0:4]
    clave = usu[5:9] 
    conectar = mySQL.connect(user=usuario, password=clave, host="localhost", db="information_schema")
    return conectar
    
def ConectarSakila():
    arch = open("claves.dll","rb")
    usu = pickle.load(arch)
    arch.close()
    usuario = usu[0:4]
    clave = usu[5:9] 
    conectar = mySQL.connect(user=usuario, password=clave, host="localhost", db="sakila")
    return conectar
    
def CrearShema(titulo):
    with open(titulo+".sql","a") as arch:
        arch.write("DROP SCHEMA IF EXISTS '"+titulo+"';\n")
        arch.write("CREATE SCHEMA IF NOT EXISTS '"+titulo+"';\n")
        arch.write("USE '"+titulo+"';\n\n")
        arch.close()
    
def CrearTablas(titulo):
    conexion = Conectar()
    cursor = conexion.cursor()
    cursor.execute("select TABLE_NAME from TABLES where TABLE_SCHEMA = 'sakila' and TABLE_TYPE = 'BASE TABLE';")
    for ren in cursor.fetchall():
        EscribirTablas(ren,cursor,titulo)
        InsertInto(ren,cursor,titulo)
        comilla = str(ren).replace("',)",";")
        inicio = comilla.replace("('","")
        with open(titulo+".sql","a") as arch:
            arch.write("select * from "+inicio+"\n")
            arch.write("\n")
            
        
     
    conexion.close()
    print("Copia de datos creada... (Encontrar como:  "+titulo+".sql)")
    
    
def EscribirTablas(ren, cursor,titulo):
    with open(titulo+".sql","a") as arch:
        for tabla in ren:
            arch.write("CREATE TABLE "+tabla+"(\n")
            primaryKey = PrimaryKey(tabla,cursor)
            cursor.execute("select COLUMN_NAME, data_type, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE from columns where TABLE_SCHEMA = 'sakila' and table_name = '"+tabla+"';")
            for atributo in cursor.fetchall():
                atrib = Filtro(atributo)
                arch.write(atrib+", \n")
            arch.write(primaryKey+" \n")
            arch.write(") ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;\n\n")
            
        arch.close()
        
def PrimaryKey(tabla,cursor):
    lista = []
    cursor.execute("select COLUMN_NAME from columns where TABLE_SCHEMA ='sakila' and COLUMN_KEY = 'PRI' and TABLE_NAME ='"+tabla+"';")
    for pri in cursor.fetchall():
        lista.append(pri)
    resultado = "PRIMARY"+str(lista)+""
    primaryKey = FiltroPrimaryKey(resultado)
    return primaryKey
        

def InsertInto(ren,cursor,titulo):
    conectarSakila= ConectarSakila()
    cursorSakila = conectarSakila.cursor()
    #lista = ()
    columna = ""
    with open(titulo+".sql","a") as arch:
        for tabla in ren:
            cursor.execute("select COLUMN_NAME from columns where TABLE_SCHEMA = 'sakila' and table_name = '"+tabla+"';")
            for atributo in cursor.fetchall():
                columna += str(atributo)
            datos=FiltroColumna(columna)
            arch.write("INSERT INTO "+str(tabla)+" "+str(datos)+" values \n")
            cursorSakila.execute("select * from "+tabla+";")
            if tabla == "actor":
                for datos in cursorSakila.fetchall():
                    insert = ActorFiltro(datos)
                    arch.write(str(insert)+"\n")
            elif tabla == "actor_info":
                for datos in cursorSakila.fetchall():
                    #insertAddress = AddressFiltro(datos)
                    arch.write(str(datos)+"\n")
            elif tabla == "address":
                for datos in cursorSakila.fetchall():
                    insertAddress = AddressFiltro(datos)
                    arch.write(str(insertAddress)+"\n")
            elif tabla == "category":
                for datos in cursorSakila.fetchall():
                    insertCategory = CategoryFiltro(datos)
                    arch.write(str(insertCategory)+"\n")
            elif tabla == "city":
                for datos in cursorSakila.fetchall():
                    insertCity = CityFiltro(datos)
                    arch.write(str(insertCity)+"\n")
            elif tabla == "country":
                for datos in cursorSakila.fetchall():
                    insertCounty = CountyFiltro(datos)
                    arch.write(str(insertCounty)+"\n")
            elif tabla == "customer":
                for datos in cursorSakila.fetchall():
                    insertCustomer = CustomerFiltro(datos)
                    arch.write(str(insertCustomer)+"\n")
            elif tabla == "customer_list":
                for datos in cursorSakila.fetchall():
                    insertCustomer = CustomerFiltro(datos)
                    arch.write(str(insertCustomer)+"\n")
            elif tabla == "film":
                for datos in cursorSakila.fetchall():
                    insertFilm = FilmFiltro(datos)
                    arch.write(str(insertFilm)+"\n")
            elif tabla == "film_actor":
                for datos in cursorSakila.fetchall():
                    insertFilm_actor = Film_Actor_Filtro(datos)
                    arch.write(str(insertFilm_actor)+"\n")
            elif tabla == "film_category":
                for datos in cursorSakila.fetchall():
                    insertFilm_category = Film_Category(datos)
                    arch.write(str(insertFilm_category)+"\n")
            elif tabla == "film_text":
                for datos in cursorSakila.fetchall():
                    insertFilm_category = Film_Text(datos)
                    arch.write(str(insertFilm_category)+"\n")
            elif tabla == "inventory":
                for datos in cursorSakila.fetchall():
                    insertInventory = Inventory(datos)
                    arch.write(str(insertInventory)+"\n")
            elif tabla == "language":
                for datos in cursorSakila.fetchall():
                    insertLanguaje = Language(datos)
                    arch.write(str(insertLanguaje)+"\n")
            elif tabla == "payment":
                for datos in cursorSakila.fetchall():
                    #insertLanguaje = Language(datos)
                    arch.write(str(datos)+"\n")
            elif tabla == "rental":
                for datos in cursorSakila.fetchall():
                    #insertLanguaje = Language(datos)
                    arch.write(str(datos)+"\n")
            elif tabla == "staff":
                for datos in cursorSakila.fetchall():
                    #insertLanguaje = Language(datos)
                    arch.write(str(datos)+"\n")
            elif tabla == "store":
                for datos in cursorSakila.fetchall():
                    #insertLanguaje = Language(datos)
                    arch.write(str(datos)+"\n")
            arch.write("\n")

    
    
    
    
    
    



    

    
#def FiltroInserInto(resultado):

        
    #+= Agrega datos en una misma varible
    # self es como this en java
    # Lenguaje de forma estructurada vs lenguaje de objetos
    
    
        

        
        

    