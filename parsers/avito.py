import requests
from bs4 import BeautifulSoup
import time


def parse_avito():
    # URL страницы с видеокартами в Москве
    """
    https://www.avito.ru/<город>/tovary_dlya_kompyutera/komplektuyuschie
    /<тип комплектующего>-ASgBAgICAkTGB~pm7gmmZw?cd=1&
    q=<Название комплектующего>
    """
    url = "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie-ASgBAgICAUTGB~pm?q=rtx+2060"

    # Заголовки для имитации браузера
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Отправляем GET-запрос
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки

        # Парсим HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все объявления (класс может измениться, нужно проверить актуальность)
        items = soup.find_all('div', {'data-marker': 'item'})

        # Список для хранения данных
        video_cards = []

        for item in items:
            try:
                # Извлекаем название
                title = item.find('h3', {'itemprop': 'name'})
                title_text = title.text.strip() if title else "Название не указано"

                # Извлекаем цену
                price = item.find('p', {'data-marker': 'item-price'})
                price_text = price.text.strip() if price else "Цена не указана"

                # Извлекаем ссылку
                link = item.find('a', {'itemprop': 'url'})
                link_url = 'https://www.avito.ru' + link[
                    'href'] if link else "Ссылка отсутствует"

                # Добавляем данные в список
                video_cards.append({
                    'title': title_text,
                    'price': price_text,
                    'link': link_url
                })

            except Exception as e:
                print(f"Ошибка при парсинге объявления: {e}")
                continue

        # Выводим результаты*.
        for card in video_cards:
            print(f"Название: {card['title']}")
            print(f"Цена: {card['price']}")
            print(f"Ссылка: {card['link']}")
            print("-" * 50)

        print(f"Всего найдено объявлений: {len(video_cards)}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к сайту: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    # Задержка перед запросом (чтобы не нагружать сервер)
    time.sleep(1)
    parse_avito()