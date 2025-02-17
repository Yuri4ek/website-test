import requests
import sqlite3
from bs4 import BeautifulSoup

con = sqlite3.connect('components.db')
con.execute("""
            CREATE TABLE videocards
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                name VARCHAR, 
                type VARCHAR, 
                efficiency REAL, 
                architecture VARCHAR, 
                releaseYear INT, 
                TDP VARCHAR
            );
            """)

cur = con.cursor()
for i in range(1, 9):
    url = f'https://technical.city/en/video/rating?&pg={i}'  # сюда ссылку на
    # сайт
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
            print(data)
            try:
                cur.execute(f"""INSERT INTO videocards (id, name, type, 
                efficiency, architecture, releaseYear, TDP) VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}')
                                    """)
                con.commit()
            except:
                pass
    else:
        print(f'Ошибка при загрузке страницы: {response.status_code}')
