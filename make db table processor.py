import requests
import sqlite3
from bs4 import BeautifulSoup

con = sqlite3.connect('components.db')
con.execute("""
            CREATE TABLE processors
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
                name VARCHAR, 
                socket VARCHAR, 
                performance REAL, 
                cores_threads VARCHAR, 
                year INT, 
                TDP VARCHAR
            );
            """)

cur = con.cursor()
count = 1
for i in range(1, 19):
    url = f'https://technical.city/en/cpu/rating?&pg={i}'  # сюда ссылку на сайт
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Найдем таблицу с рейтингом процессоров
        table = soup.find('table')

        # Извлекаем заголовки таблицы
        '''headers = [header.text for header in table.find_all('th')]
        print("Заголовки таблицы:", headers)'''

        # Извлекаем строки таблицы
        for row in table.find_all('tr')[1:]:  # Пропускаем заголовок
            cols = row.find_all('td')
            data = [col.text.strip() for col in cols]
            try:
                if data[2] == 'desktop' and int(data[6]) > 2009:
                    cur.execute(f"""INSERT INTO processors (id, name, socket, 
                    performance, cores_threads, year, TDP) VALUES (
                    '{count}', '{data[1]}', '{data[3]}', '{data[4]}', 
                    '{data[5]}', '{data[6]}', '{data[7]}')
                                        """)
                    con.commit()
                    count += 1
            except:
                pass
    else:
        print(f'Ошибка при загрузке страницы: {response.status_code}')
