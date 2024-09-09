#Напишите функцию, которая делает запрос к TheCatAPI для получения случайного изображения кошки. https://api.thecatapi.com/v1/images/search
#Напишите тест, который проверяет успешный запрос и возвращает правильный URL.
#Напишите тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает None.

import requests
def get_random_cat_image():
    """Запрашивает случайное изображение кошки из TheCatAPI и возвращает его URL."""
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный статус код
        data = response.json()
        return data[0]['url'] if data else None
    except requests.exceptions.RequestException:
        return None