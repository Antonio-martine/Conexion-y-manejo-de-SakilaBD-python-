import pickle
#ddl = libreria de enlaces dinamico
#ensamblador -> lenguaje de programacion
arch = open("claves.dll","wb")
msg = "root,root"
pickle.dump(msg,arch)
arch.close()