import requests
import sqlite3
from bs4 import BeautifulSoup

con = sqlite3.connect('components.db')
con.execute("""
            CREATE TABLE powersupplies
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                name VARCHAR, 
                form_factor TEXT NOT NULL,
                TDP VARCHAR
            );
            """)

cur = con.cursor()

url = 'https://pcstonks.ru/tables/psu'  # сюда ссылку на сайт
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Найдем таблицу с рейтингом процессоров
    table = soup.find('table')

    # Извлекаем заголовки таблицы
    headers = [header.text for header in table.find_all('th')]
    print("Заголовки таблицы:", headers)

    # Извлекаем строки таблицы
    count = 0
    for row in table.find_all('tr')[1:]:  # Пропускаем заголовок
        cols = row.find_all('td')
        data = [col.text.strip() for col in cols]
        count += 1
        cur.execute(f"""INSERT INTO powersupplies (id, name, 
                            form_factor, TDP) VALUES ('{count}', 
                            '{data[0]}', '{data[1]}', '{data[2]}')
                                                """)
        con.commit()
else:
    print(f'Ошибка при загрузке страницы: {response.status_code}')
