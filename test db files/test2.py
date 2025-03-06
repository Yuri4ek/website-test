import requests
import sqlite3
from bs4 import BeautifulSoup

count = 1
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
            try:
                if (data[2] == 'desktop' or data[2] == 'workstation') and \
                        int(data[5]) > 2015 and float(data[3]) > 1:
                    print(
                        f'[{count}, {data[1]}, {data[3]}, {data[5]},'
                        f' {data[6]}],')

                    count += 1
            except:
                pass
    else:
        print(f'Ошибка при загрузке страницы: {response.status_code}')
