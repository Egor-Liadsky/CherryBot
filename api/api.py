import json

from flask import Flask
import database_api
import setting

app = Flask(__name__)

database_api = database_api.DatabaseAPI()


# Берёт все группы и всех преподавателей
@app.route('/api', methods=['GET'])
def get_all():
    list = database_api.select_all()
    return str(list)

# Берёт определённую группу/преподавателя
@app.route('/api/<group>', methods=['GET'])
def get_group(group):
    list = database_api.take_group(group)
    return str(json.loads(list))

# Берёт все название/имена групп, преподавателей
@app.route('/api/list', methods=['GET'])
def list():
    list = database_api.take_list()
    return str(json.loads(list))


@app.errorhandler(404)
def not_found(error):
    """Ошибка при не нахождении страницы"""
    return '404'


@app.errorhandler(400)
def not_found(error):
    """Ошибка при неверном запросе"""
    return '400'


@app.errorhandler(500)
def not_found(error):
    """Ошибка при неверном запросе"""
    return '404'


if __name__ == '__main__':
    app.run(host=setting.DATABASE['host'], port=8080)
