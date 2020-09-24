from mysql.connector import connect, errorcode, Error


def ConnectMySql():
    try:
        mydb = connect(
            host="localhost", user="root", password="system", database="pizzabot",
        )
        return mydb
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("check your user name or password once again")
            return False
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return False
        else:
            print(err)
            return False
