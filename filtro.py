def Filtro(atributo):
    not_Null = str (atributo).replace("NO","NOT NULL")
    yes_Null = not_Null.replace("YES","NULL")
    parentesis = yes_Null.replace("(","")
    parentesis2 = parentesis.replace(")","")
    comillas = parentesis2.replace("''","")
    comillas1 = comillas.replace("'","")
    comillas2 = comillas1.replace(" '","")
    comas = comillas2.replace(","," ")
    none = comas.replace("None","")
    #Varchars
    varchar10= none.replace("varchar  10","VARCHAR(10)")
    varchar20 = varchar10.replace("varchar  20","VARCHAR(20)")
    varchar50 = varchar20.replace("varchar  50","VARCHAR(50)")
    varchar45 = varchar50.replace("varchar  45","VARCHAR(45)")
    varchar25 = varchar45.replace("varchar  25","VARCHAR(25)")
    varchar91 = varchar25.replace("varchar  91","VARCHAR(91)")
    varchar128 = varchar91.replace("varchar  128","VARCHAR(128)")
    varchar6 = varchar128.replace("varchar  6","VARCHAR(6)")
    varchar16 = varchar6.replace("varchar  16","VARCHAR(16)")
    varchar95 = varchar16.replace("varchar  95","VARCHAR(95)")
    varchar40 = varchar95.replace("varchar  40","VARCHAR(40)")
    #Otros
    smallint = varchar40.replace("smallint","SMALLING")
    text = smallint.replace("text  65535","TEXT(65535)")
    timestamp = text.replace("timestamp","TIMESTAMP")
    tinyint = timestamp.replace("tinyint","TINYINT")
    datetime = tinyint.replace("datetime","DATETIME")
    year = datetime.replace("year","YEAR")
    inte = year.replace("int","INT")
    geometry = inte.replace("geometry","GEOMETRY")
    decimal27 = geometry.replace("decimal27","DECIMAL(27)")
    decimal4 = decimal27.replace("decimal4","DECIMAL(4)")
    decimal5 = decimal4.replace("decimal5","DECIMAL(5)")
    enum = decimal5.replace("enum  5","ENUM(5)")
    setopcion = enum.replace("set  54 ","SET(54)")
    decimal = setopcion.replace("decimal","DECIMAL")
    bloob = decimal.replace("blob  65535","BLOB(65535)")
    charopcion = bloob.replace("char  20","CHAR(20)")
    return charopcion
    
def FiltroPrimaryKey(resultado):
    parentesis1 = str(resultado).replace("('","")
    parentesis2 = parentesis1.replace("',)","")
    corcheteInicio = parentesis2.replace("PRIMARY[","PRIMARY (")
    corcheteFin = corcheteInicio.replace("]",")")
    return corcheteFin
    
def FiltroColumna(columna):
    comilla = str(columna).replace("'",'"')
    parentesis = comilla.replace(")(","")
    coma = parentesis.replace(",)",")")
    return coma
    
def ActorFiltro(datos):
    comillas = str(datos).replace("'",'"')
    date = comillas.replace("datetime.datetime(2006, 2, 15, 4, 34, 33)","2016-02-15 04:34:33")
    coma = date.replace(")","),")
    quitarComa = coma.replace('(200, "THORA", "TEMPLE", 2016-02-15 4:34:33),','(200, "THORA", "TEMPLE", 2016-02-15 4:34:33);') 
    return quitarComa
    
def AddressFiltro(datos):
    comillas = str(datos).replace("'",'"')
    data1 = comillas.replace("datetime.datetime(2014, 9, 25, 22, 30, ","2014-9-25 22:30:")
    data2 = data1.replace("datetime.datetime(2014, 9, 25, 22, 31, ","2014-9-25 22:31:")
    data3 = data2.replace("datetime.datetime(2014, 9, 25, 22, 32, ","2014-9-25 22:32:")
    data4 = data3.replace("datetime.datetime(2014, 9, 25, 22, 33, ","2014-9-25 22:33:")
    data5 = data4.replace("datetime.datetime(2014, 9, 25, 22, 34, ","2014-9-25 22:34:")
    data6 = data5.replace("datetime.datetime(2014, 9, 25, 22, 30) ","2014-9-25 22:30")
    data7 = data6.replace("datetime.datetime(2014, 9, 25, 22, 31) ","2014-9-25 22:31")
    data8 = data7.replace("datetime.datetime(2014, 9, 25, 22, 32) ","2014-9-25 22:32")
    data9 = data8.replace("datetime.datetime(2014, 9, 25, 22, 33) ","2014-9-25 22:33")
    data10 = data9.replace("datetime.datetime(2014, 9, 25, 22, 34) ","2014-9-25 22:34")
    parentesis = data10.replace("))","),")
    quitarComa = parentesis.replace('(605, "1325 Fukuyama Street", "", "Heilongjiang", 537, "27107", "288241215394", b"\x00\x00\x00\x00\x01\x01\x00\x00\x00\x17T\npp\x01`@\x1e\x1cG\x07\x7f}G@", 2014-9-25 22:30:44),','(605, "1325 Fukuyama Street", "", "Heilongjiang", 537, "27107", "288241215394", b"\x00\x00\x00\x00\x01\x01\x00\x00\x00\x17T\npp\x01`@\x1e\x1cG\x07\x7f}G@", 2014-9-25 22:30:44);')
    return quitarComa
    
def CategoryFiltro(datos):
    comillas = str(datos).replace("'",'"')
    date = comillas.replace("datetime.datetime(2006, 2, 15, 4, 46, 27)","2006-2-15 04:46:27")
    coma = date.replace(")","),")
    quitarComa = coma.replace('(16, "Travel", 2006-2-15 4:46:27),','(16, "Travel", 2006-2-15 04:46:27);')
    return quitarComa
    
def CityFiltro(datos):
    comillas = str(datos).replace("'",'"')
    date = comillas.replace("datetime.datetime(2006, 2, 15, 4, 45, 25)","2006-2-15 04:45:25")
    coma = date.replace(")","),")
    quitarComa = coma.replace('(600, "Ziguinchor", 83, 2006-2-15 4:45:25),','(600, "Ziguinchor", 83, 2006-2-15 4:45:25);')
    return quitarComa
    
def CountyFiltro(datos):
    comillas = str(datos).replace("'",'"')
    date = comillas.replace("datetime.datetime(2006, 2, 15, 4, 44)","2006-2-15 04:44")
    coma = date.replace(")","),")
    quitarComa = coma.replace('(109, "Zambia", 2006-2-15 4:44),','(109, "Zambia", 2006-2-15 04:44);')
    return quitarComa
    
def CustomerFiltro(datos):
    comillas = str(datos).replace("'",'"')
    date1 = comillas.replace("datetime.datetime(2006, 2, 14, 22, 4, 36)","2006-2-14 22:04:36")
    date2 = date1.replace("datetime.datetime(2006, 2, 15, 4, 57, 20)","2006-2-15 04:57:20")
    coma = date2.replace(")","),")
    quitarComa = coma.replace('(599, 2, "AUSTIN", "CINTRON", "AUSTIN.CINTRON@sakilacustomer.org", 605, 1, datetime.datetime(2006, 2, 14, 22, 4, 37),, 2006-2-15 4:57:20),','(599, 2, "AUSTIN", "CINTRON", "AUSTIN.CINTRON@sakilacustomer.org", 605, 1, datetime.datetime(2006, 2, 14, 22, 4, 37),, 2006-2-15 04:57:20);')
    return quitarComa
    
def FilmFiltro(datos):
    comillas = str(datos).replace("'",'"')
    date1 = comillas.replace("datetime.datetime(2006, 2, 15, 5, 3, 42)","2006-2-15 05:03:42")
    coma = date1.replace(")","),")
    quitarComa = coma.replace('(1000, "ZORRO ARK", "A Intrepid Panorama of a Mad Scientist And a Boy who must Redeem a Boy in A Monastery", 2006, 1, None, 3, Decimal("4.99"),, 50, Decimal("18.99"),, "NC-17", "Trailers,Commentaries,Behind the Scenes", 2006-2-15 05:03:42),','(1000, "ZORRO ARK", "A Intrepid Panorama of a Mad Scientist And a Boy who must Redeem a Boy in A Monastery", 2006, 1, None, 3, Decimal("4.99"),, 50, Decimal("18.99"),, "NC-17", "Trailers,Commentaries,Behind the Scenes", 2006-2-15 05:03:42);')
    return quitarComa
    
def Film_Actor_Filtro(datos):
    comillas = str(datos).replace("'",'"')
    date1 = comillas.replace("datetime.datetime(2006, 2, 15, 5, 5, 3)","2006-02-15 05:05:03")
    coma = date1.replace(")","),")
    quitarComa = coma.replace('(200, 993, 2006-02-15 05:05:03),','(200, 993, 2006-02-15 05:05:03);')
    return quitarComa
    
def Film_Category(datos):
    comillas = str(datos).replace("'",'"')
    date1 = comillas.replace("datetime.datetime(2006, 2, 15, 5, 7, 9)","2006-02-15 05:07:09")
    coma = date1.replace(")","),")
    quitarComa = coma.replace('(1000, 5, 2006-02-15 05:07:09),','(1000, 5, 2006-02-15 05:07:09);')
    return quitarComa

def Film_Text(datos):
    comillas = str(datos).replace("'",'"')
    coma = comillas.replace(")","),")
    quitarComa = coma.replace('(1000, "ZORRO ARK", "A Intrepid Panorama of a Mad Scientist And a Boy who must Redeem a Boy in A Monastery"),','(1000, "ZORRO ARK", "A Intrepid Panorama of a Mad Scientist And a Boy who must Redeem a Boy in A Monastery");')
    return quitarComa

def Inventory(datos):
    date1 = str(datos).replace("datetime.datetime(2006, 2, 15, 5, 9, 17)","2006-02-15 05:09:17")
    coma = date1.replace(")","),")
    quitarComa = coma.replace('(4581, 1000, 2, 2006-02-15 05:09:17),','(4581, 1000, 2, 2006-02-15 05:09:17);')
    return quitarComa
    
def Language(datos):
    comillas = str(datos).replace("'",'"')
    date1 = comillas.replace("datetime.datetime(2006, 2, 15, 5, 2, 19)","2006-02-15 05:02:19")
    coma = date1.replace(")","),")
    quitarComa = coma.replace('(6, "German", 2006-02-15 05:02:19),','(6, "German", 2006-02-15 05:02:19);')
    return quitarComa
    
    
    
    
    
    
    
    