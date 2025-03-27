from flask import Flask, render_template
from sqlalchemy import inspect
from data import (db_session, computer_cases, cooling_systems, memory_types,
                  motherboards, power_supplies, processors, ram_modules,
                  sockets, storage_devices, videocards)

app = Flask(__name__)
db_session.global_init("db/components.db")

# надо бд сделать и удалить
# Имитация данных пользователя (в реальном приложении это будет из базы данных)
# Для теста можно менять значения
user = {
    "is_logged_in": False,
    # Измените на True, чтобы протестировать авторизованного пользователя
    "username": "User123"
}


@app.route('/')
def home():
    return render_template('main.html', user=user)


@app.route('/choose_components/<components_type>')
def choose_components(components_type):
    return render_template('search_components.html',
                           user=user,)


components_types = {'computer_cases': computer_cases.ComputerCases,
                    'cooling_systems': cooling_systems.CoolingSystems,
                    'memory_types': memory_types.MemoryTypes,
                    'motherboards': motherboards.MotherBoards,
                    'power_supplies': power_supplies.PowerSupplies,
                    'processors': processors.Processors,
                    'ram_modules': ram_modules.RamModules,
                    'sockets': sockets.Sockets,
                    'storage_devices': storage_devices.StorageDevices,
                    'videocards': videocards.Videocards}


@app.route('/components/<components_type>')
def show_components_table(components_type):
    component_type = components_types[components_type]

    # все компоненты
    db_sess = db_session.create_session()
    components = db_sess.query(component_type).all()

    # название колонн
    inspector = inspect(component_type)
    columns = [column.name for column in inspector.mapper.columns]

    return render_template('components_table.html',
                           user=user,
                           keys=columns,
                           components=components)


@app.route('/builds')
def show_builds():
    return render_template('builds.html', user=user)


@app.route('/login')
def authorization():
    return render_template('authorization.html', user=user)


@app.route('/register')
def registration():
    return render_template('registration.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
