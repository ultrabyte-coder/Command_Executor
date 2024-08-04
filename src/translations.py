import json
import pathlib


def load_translation(lang):
    """
    Загружает переводы из JSON-файла для указанного языка.

    :param lang: Язык, для которого загружаются переводы (например, 'en' или 'ru').
    :return: Словарь с переводами.
    """
    localedir = pathlib.Path(__file__).resolve().parent / "locales" / lang / "LC_MESSAGES"
    with open(localedir / f"{lang}.json", 'r', encoding='utf-8') as file:
        return json.load(file)