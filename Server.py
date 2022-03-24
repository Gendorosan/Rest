from flask import Flask, jsonify, request
import sqlite3
import traceback
import sys

app = Flask(__name__)


@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"INSERT INTO Users (id, current_balance, joining_date, age, city, last_activity, "
                       f"tariff) VALUES ({data['id']}, {data['current_balance']}, {data['joining_date']},"
                       f" {data['age']}, {data['city']}, {data['last_activity']}, {data['tariff']}) ")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось вставить данные в таблицу Users")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/delete_user', methods=['POST'])
def delete_user():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"delete from Users where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось удалить пользователя")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_user', methods=['POST'])
def update_user():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update Users set current_balance = {data['current_balance']},"
                       f" joining_date = {data['joining_date']}, age = {data['age']},"
                       f" city = {data['city']}, last_activity = {data['last_activity']},"
                       f" tariff = {data['tariff']} where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные пользователя")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return_answer = {'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))}
        return jsonify(return_answer)


@app.route('/update_user_current_balance', methods=['POST'])
def update_user_current_balance():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update Users set current_balance = {data['current_balance']} where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные пользователя")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_user_last_activity', methods=['POST'])
def update_user_last_activity():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update Users set tariff = {data['tariff']} where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные пользователя")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_user_city', methods=['POST'])
def update_user_city():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update Users set city = {data['city']} where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные пользователя")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_user_tariff', methods=['POST'])
def update_user_tariff():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update Users set last_activity = {data['last_activity']} where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные пользователя")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("SELECT* FROM Users")
        return_answer = {}
        for row in cursor:
            return_answer.update([(row[0], {'name': row[1], 'current_balance': row[2], 'joining_date': row[3],
                                            'age': row[4], 'city': row[5], 'last_activity': row[6], 'tariff': row[7]})])
        sqlite_connection.close()
        cursor.close()
        return jsonify(return_answer)

    except sqlite3.Error as error:
        print("Не удалось получить данные из таблицы tariff")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/add_tariff', methods=['POST'])
def add_tariff():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"INSERT INTO tariff (id, name, start_date, end_date, minute_volume, sms_volume, "
                       f"traffic_volume) VALUES ({data['id']}, {data['name']}, {data['start_date']},"
                       f" {data['end_date']}, data{['minute_volume']}, {data['sms_volume']}) ")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось вставить данные в таблицу tariff")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/delete_tariff', methods=['POST'])
def delete_tariff():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"delete from tariff where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось удалить тариф")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_tariff', methods=['POST'])
def update_tariff():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update tariff set name = {data['name']},"
                       f" start_date = {data['start_date']}, end_date = {data['end_date']},"
                       f" minute_volume = {data['minute_volume']}, sms_volume = {data['sms_volume']},"
                       f" traffic_volume = {data['traffic_volume']} where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные тарифа")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_tariff_end_date', methods=['POST'])
def update_tariff_end_date():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update tariff set end_date = {data['end_date']} where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные тарифа")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_tariff_minute_volume', methods=['POST'])
def update_tariff_minute_volume():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update tariff set minute_volume = {data['minute_volume']} where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные тарифа")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_tariff_sms_volume', methods=['POST'])
def update_tariff_sms_volume():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()

        cursor.execute(f"Update tariff set sms_volume = {data['sms_volume']} where id = {data['id']}")

        sqlite_connection.commit()
        cursor.close()
        return_answer = {'answer': 'success'}
        sqlite_connection.close()
        return jsonify(return_answer)

    except sqlite3.Error as error:
        print("Не удалось обновить данные тарифа")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_tariff_traffic_volume', methods=['POST'])
def update_tariff_traffic_volume():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()

        cursor.execute(f"Update tariff set traffic_volume = {data['traffic_volume']} where id = {data['id']}")

        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные тарифа")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/get_tariffs', methods=['GET'])
def get_tariffs():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        cursor = sqlite_connection.cursor()
        return_answer = {}
        for row in cursor:
            return_answer.update([(row[0], {'name': row[1], 'start_date': row[2], 'end_date': row[3],
                                            'minute_volume': row[4], 'sms_volume': row[5], 'traffic_volume': row[6]})])
        sqlite_connection.close()
        cursor.close()
        return jsonify(return_answer)

    except sqlite3.Error as error:
        print("Не удалось получить данные из таблицы tariff")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/add_event', methods=['POST'])
def add_event():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor = sqlite_connection.cursor()
        cursor.execute(f"INSERT INTO event (id, time_stamp, user_id, type_of_service, volume)"
                       f" VALUES ({data['id']}, {data['time_stamp']}, {data['user_id']},"
                       f" {data['type_of_service']}, data{['volume']}) ")

        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось вставить данные в таблицу event")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/delete_event', methods=['POST'])
def delete_event():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"delete from event where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось удалить событие")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_event', methods=['POST'])
def update_event():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update event set time_stamp = {data['time_stamp']},"
                       f" user_id = {data['user_id']}, type_of_service = {data['type_of_service']},"
                       f" volume = {data['volume']} where id = {data['id']}")

        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные события")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_event_time_stamp', methods=['POST'])
def update_event_time_stamp():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update event set time_stamp = {data['time_stamp']}where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные события")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_event_user_id', methods=['POST'])
def update_event_user_id():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update event set user_id = {data['user_id']}where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные события")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_event_type_of_service', methods=['POST'])
def update_event_type_of_service():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update event set type_of_service = {data['type_of_service']}where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные события")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/update_event_volume', methods=['POST'])
def update_event_volume():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        data = request.get_json()
        cursor.execute(f"Update event set volume = {data['volume']}where id = {data['id']}")
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return jsonify({'answer': 'success'})

    except sqlite3.Error as error:
        print("Не удалось обновить данные события")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


@app.route('/get_events', methods=['GET'])
def get_events():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("SELECT* FROM event")
        return_answer = {}
        sqlite_connection.close()
        for row in cursor:
            return_answer.update([(row[0], {'time_stamp': row[1], 'user_id': row[2], 'type_of_service': row[3],
                                            'volume': row[4]})])
        cursor.close()
        return jsonify(return_answer)

    except sqlite3.Error as error:
        print("Не удалось получить данные из таблицы event")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        return jsonify({'answer': str(traceback.format_exception(exc_type, exc_value, exc_tb))})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
