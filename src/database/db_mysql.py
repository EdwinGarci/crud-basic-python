from decouple import config

import pymysql

def get_connection():
    try:
        return pymysql.connect(
            host=config('MYSQL_DB_HOST'),
            user=config('MYSQL_DB_USER'),
            password=config('MYSQL_DB_PASSWORD'),
            db=config('MYSQL_DB_NAME'),
        )
    except Exception as ex:
        print(ex)