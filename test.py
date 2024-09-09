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


# Тесты
def test_get_random_cat_image_success():
    """Тест для проверки успешного запроса."""
    url = get_random_cat_image()
    assert url is not None, "Ошибка: URL изображения кошки не должен быть None."
    assert url.startswith("http"), "Ошибка: URL должен начинаться с 'http'."


def test_get_random_cat_image_failure():
    """Тест для проверки неуспешного запроса (например, статус код 404)."""
    # Для этого теста мы можем использовать mock библиотеку, чтобы имитировать ответ API.
    from unittest.mock import patch

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {}

        url = get_random_cat_image()
        assert url is None, "Ошибка: при неуспешном запросе URL должен быть None."


# Запуск тестов
if __name__ == "__main__":
    test_get_random_cat_image_success()
    test_get_random_cat_image_failure()
    print("Все тесты пройдены!")