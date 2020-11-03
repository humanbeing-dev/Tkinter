from mysql import connector


def connection():
    config = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "auth_plugin": "mysql_native_password"
    }
    try:
        c = connector.connect(**config)
        return c
    except:
        print("Connection Error")
        exit(1)
