from flask import Flask, render_template

app = Flask(__name__)

# Имитация данных пользователя (в реальном приложении это будет из базы данных)
# Для теста можно менять значения
user = {
    "is_logged_in": True,
    # Измените на True, чтобы протестировать авторизованного пользователя
    "username": "User123"
}


@app.route('/')
def home():
    return render_template('main.html', user=user)


@app.route('/table')
def show_table():
    # Пример данных
    table_headers = ["ID", "Имя", "Возраст"]
    table_data = [
        [1, "Алексей", 25],
        [2, "Мария", 30],
        [3, "Иван", 22]
    ]

    return render_template('table.html',
                           user=user,
                           headers=table_headers,
                           data=table_data)


if __name__ == '__main__':
    app.run(debug=True)
