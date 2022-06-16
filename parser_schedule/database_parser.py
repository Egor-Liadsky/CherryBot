import json
from datetime import datetime

import psycopg2
import setting


class DatabaseParser:
    def __init__(self):
        self.__connect = psycopg2.connect(
            dbname=setting.DATABASE['database'],
            user=setting.DATABASE['user'],
            password=setting.DATABASE['password'],
            host=setting.DATABASE['host']
        )

        self.__cursor = self.__connect.cursor()

    def append_json_data(self, group: str, json_data: json, is_group: bool):
        self.__cursor.execute("INSERT INTO schedule VALUES (%s, %s, %s)", (f'{group}', f'{json_data}', is_group))
        self.__connect.commit()


def __enter__(self):
    self.__connect.commit()
    self.__cursor.close()
    self.__connect.close()


def __exit__(self, exc_type, exc_val, exc_tb):
    self.__connect.commit()
    self.__cursor.close()
    self.__connect.close()
