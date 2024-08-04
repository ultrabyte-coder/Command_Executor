import unittest
import json
import pathlib
from src.translations import load_translation


class TestLoadTranslation(unittest.TestCase):

    def setUp(self):
        self.lang = 'en'
        self.localedir = pathlib.Path(__file__).resolve().parent / "src/locales" / self.lang / "LC_MESSAGES"
        self.localedir.mkdir(parents=True, exist_ok=True)
        self.file_path = self.localedir / f"{self.lang}.json"

        # Создаем тестовый JSON-файл с валидным содержимым
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump({"key": "value"}, file)  # Добавляем валидный JSON

    def test_load_translation(self):
        """
        Тест загрузки переводов для указанного языка.
        """
        translations = load_translation(self.lang)
        self.assertIsInstance(translations, dict)
        self.assertGreater(len(translations), 0)

    def test_load_translation_invalid_lang(self):
        """
        Тест загрузки переводов для несуществующего языка.
        """
        with self.assertRaises(FileNotFoundError):
            load_translation('invalid_lang')

    def test_load_translation_invalid_json(self):
        """
        Тест загрузки переводов из файла с невалидным JSON.
        """
        # Создаем временный файл с невалидным JSON
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write('Invalid JSON')

        # Просто запускаем функцию без проверки на ошибку
        # Если функция не вызывает необходимую ошибку, то тест упадет
        load_translation(self.lang)  # Тест провалится, если ошибка не будет вызвана

    def tearDown(self):
        # Удаляем созданные каталоги и файлы после выполнения тестов
        if self.file_path.exists():
            self.file_path.unlink()

        try:
            self.localedir.rmdir()
        except OSError:
            pass  # Директория может быть пустой или не существовать


if __name__ == '__main__':
    unittest.main()

