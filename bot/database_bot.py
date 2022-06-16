import psycopg2
import setting


class DatabaseBot:
    def __init__(self):
        self.__connect = psycopg2.connect(
            dbname=setting.DATABASE['database'],
            user=setting.DATABASE['user'],
            password=setting.DATABASE['password'],
            host=setting.DATABASE['host']
        )

        self.__cursor = self.__connect.cursor()