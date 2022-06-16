import json
import psycopg2
import setting


class DatabaseAPI:
    def __init__(self):
        self.__connect = psycopg2.connect(
            dbname=setting.DATABASE['database'],
            user=setting.DATABASE['user'],
            password=setting.DATABASE['password'],
            host=setting.DATABASE['host']
        )

        self.__cursor = self.__connect.cursor()

    def take_group(self, group):
        self.__cursor.execute(f"SELECT * FROM schedule WHERE group_name='{group}'")
        result = self.__cursor.fetchone()
        return json.dumps({"name": result[0], "schedule": result[1], "is_group": result[2]})


    def take_list(self):
        self.__cursor.execute('SELECT group_name FROM schedule WHERE is_group=true')
        group = list(map(lambda x:x[0], self.__cursor.fetchall()))
        self.__cursor.execute('SELECT group_name FROM schedule WHERE is_group=false')
        prepods = list(map(lambda x:x[0], self.__cursor.fetchall()))
        return json.dumps({'group': group, 'teacher': prepods})


    def select_all(self):
        self.__cursor.execute("SELECT * FROM schedule")
        result = self.__cursor.fetchone()
        print(result)
        result = list(map(lambda x: {'name': result[0], 'schedule': result[1], 'is_group': result[2]}, result))
        return json.dumps({"name": 'all', 'schedule': result})

    def __enter__(self):
        self.__connect.commit()
        self.__cursor.close()
        self.__connect.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connect.commit()
        self.__cursor.close()
        self.__connect.close()
