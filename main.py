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
    return render_template('test.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
