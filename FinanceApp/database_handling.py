import mysql.connector


def db_connect():
    config = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "auth_plugin": "mysql_native_password"
    }
    c = mysql.connector.connect(**config)
    try:
        c = mysql.connector.connect(**config)
        return c
    except:
        print("Connection Error")
        exit(1)


def show_databases():
    cn = db_connect()
    my_cursor = cn.cursor()
    my_cursor.execute("SHOW DATABASES")
    return [db[0].decode("utf-8") for db in my_cursor]


def create_database(db_name):
    cn = db_connect()
    my_cursor = cn.cursor()
    my_cursor.execute(f"CREATE DATABASE {db_name}")


def show_tables(db_name):
    cn = db_connect()
    my_cursor = cn.cursor()
    my_cursor.execute(f"USE {db_name}")
    my_cursor.execute(f"SHOW TABLES;")
    return [db[0].decode("utf-8") for db in my_cursor]


def create_table(tbl_name, db_name):
    """Function to create a table within a chosen database"""
    cn = db_connect()
    my_cursor = cn.cursor()
    my_cursor.execute(f"USE {db_name}")
    my_cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tbl_name} (
        exp_id INT AUTO_INCREMENT PRIMARY KEY,
        exp_day DATE,
        exp_cat_1 VARCHAR(100),
        exp_cat_2 VARCHAR(100),
        exp_val INTEGER(10)
    );""")


# print(dbs_show())
# print(create_table('expenditures', "our_finances"))
# print(show_tables("our_finances"))
# db_create("our_finances")
# create_table('expenditures', "our_finances")
# print(show_tables('our_finances'))