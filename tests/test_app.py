import sys
import os
import tkinter
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk, END
from src.commands import commands
from src.app import CommandExecutorApp


class TestCommandExecutorApp(unittest.TestCase):
    """
    Класс для тестирования приложения CommandExecutorApp.
    """

    def setUp(self):
        """
        Инициализация тестового окружения.

        Создает главное окно Tkinter и экземпляр приложения CommandExecutorApp.
        """
        self.root = Tk()
        self.app = CommandExecutorApp(self.root)

    def test_init(self):
        """
        Тест инициализации приложения.

        Проверяет заголовок главного окна, количество чекбоксов и видимость области отчета.
        """
        self.assertEqual(self.app.root.title(), "Command Executor")
        self.assertEqual(len(self.app.check_vars), len(commands))
        self.assertEqual(self.app.report_area.winfo_ismapped(), 0)

    def test_execute_commands(self):
        """
        Тест выполнения команд.

        Проверяет поведение приложения при отсутствии выбранных команд и при выборе всех команд.
        """
        self.app.execute_commands()
        self.assertEqual(self.app.report_area.get('1.0', END), "\n")

        for var in self.app.check_vars:
            var.set(1)
        self.app.execute_commands()
        self.assertIn("--- Execution Report ---", self.app.report_area.get('1.0', END))

    @patch('subprocess.run')
    def test_execute_commands_with_terminal(self, mock_run):
        """
        Тест выполнения команд в терминале.

        Проверяет вызов метода subprocess.run при выполнении команд.
        """
        mock_run.return_value = MagicMock()
        for var in self.app.check_vars:
            var.set(1)
        self.app.execute_commands()
        mock_run.assert_called_once()

    def test_show_report(self):
        """
        Тест отображения отчета.

        Проверяет содержимое отчета после его отображения.
        """
        self.app.output_report = {cmd: "Command sent for execution." for cmd in commands}
        self.app.show_report()
        report = self.app.report_area.get('1.0', END)
        for cmd in commands:
            self.assertIn(f"{cmd}: Command sent for execution.", report)

    def test_change_language(self):
        """
        Тест смены языка интерфейса.

        Проверяет заголовок главного окна и текст кнопок после смены языка на русский.
        """
        self.app.change_language('ru')
        self.assertEqual(self.app.root.title(), "Исполнитель команд")
        for widget in self.app.root.winfo_children():
            if isinstance(widget, str):
                self.assertEqual(widget, self.app.translations[commands[self.app.root.winfo_children().index(widget)]])
            elif isinstance(widget, tkinter.Button):
                self.assertEqual(widget.cget('text'), self.app.translations["Execute Selected Commands"])


if __name__ == '__main__':
    unittest.main()
