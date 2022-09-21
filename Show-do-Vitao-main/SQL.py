def LoginSQL(login, senha,novo):
    from unittest import skip
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        auth_plugin = "mysql_native_auth")

    cursor = mydb.cursor()

    try:
        cursor.execute("CREATE DATABASE Login")
    except:
        skip

    cursor.execute("USE Login")

    try:
        cursor.execute("CREATE TABLE login (nome varchar(20) primary key, senha varchar(30), pontos integer)")
    except:
        skip
    
    if novo == True:
        try:
            cursor.execute(f"INSERT INTO login VALUES ('{login}','{senha}', 0);")
            mydb.commit()
            verificador = True
        except:
            verificador = False
    else:
        try:
            cursor.execute(f"SELECT nome, senha FROM login WHERE nome = '{login}' AND senha = '{senha}'")
            for x in cursor:
                loginSQL = x[0]
                senhaSQL = x[1]
            if login == loginSQL and senha == senhaSQL:
                verificador = True
            else:
                verificador = False
        except:
            verificador = False

    if verificador == True or verificador == False:
        return verificador

def PlacarSQL():
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        auth_plugin = "mysql_native_auth")

    lista_nomes = []
    lista_pontos = []
    cursor = mydb.cursor()
    cursor.execute("USE Login")
    cursor.execute(f"SELECT nome, pontos FROM login ORDER BY pontos DESC LIMIT 5")
    for x in cursor:
        lista_nomes.append(x[0])
        lista_pontos.append(x[1])
    return lista_nomes, lista_pontos

def PontosSQL(login):
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        auth_plugin = "mysql_native_auth")

    cursor = mydb.cursor()
    cursor.execute("USE Login")
    cursor.execute(f"SELECT pontos FROM login WHERE nome = '{login}'")
    for x in cursor:
        pontos = x
    return pontos

def SomarPontosSQL(login, nova_pontuacao):
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        auth_plugin = "mysql_native_auth")

    cursor = mydb.cursor()
    cursor.execute("USE Login")
    cursor.execute(f"UPDATE Login SET pontos = pontos + {nova_pontuacao} WHERE nome = '{login}'")
    mydb.commit()
