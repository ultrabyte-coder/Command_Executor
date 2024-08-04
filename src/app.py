import tkinter as tk
from tkinter import messagebox, scrolledtext
from translations import load_translation
import subprocess
from commands import commands


class CommandExecutorApp:
    def __init__(self, root):
        """
        Инициализация графического интерфейса приложения.

        :param root: Основное окно приложения.
        """
        self.root = root
        self.root.title("Command Executor")
        self.translations = load_translation('en')

        self.output_report = {}

        # Переменные для хранения состояния чекбоксов
        self.check_vars = [tk.IntVar() for _ in commands]

        # Создание чекбоксов для каждой команды
        for i, command in enumerate(commands):
            checkbox = tk.Checkbutton(root, text=self.translations[command], variable=self.check_vars[i])
            checkbox.pack(anchor='w')

        # Кнопка для выполнения выбранных команд
        execute_button = tk.Button(root, text=self.translations["Execute Selected Commands"], command=self.execute_commands)
        execute_button.pack(pady=10)

        # Область для вывода отчета
        self.report_area = scrolledtext.ScrolledText(root, width=80, height=20)
        self.report_area.pack()

        # Меню для выбора языка
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        self.lang_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=self.translations["Language"], menu=self.lang_menu)

        # Опции меню для выбора языка
        self.lang_menu.add_command(label=self.translations["English"], command=lambda: self.change_language('en'))
        self.lang_menu.add_command(label=self.translations["Russian"], command=lambda: self.change_language('ru'))

    def execute_commands(self):
        """
        Выполняет выбранные команды в терминале и обновляет отчет о выполнении.
        """
        self.output_report.clear()
        self.report_area.delete('1.0', tk.END)

        # Получение списка выбранных команд
        selected_commands = [command for i, command in enumerate(commands) if self.check_vars[i].get() == 1]

        if not selected_commands:
            messagebox.showinfo(self.translations["Info"], self.translations["No commands selected."])
            return

        # Формирование команды для исполнения
        full_command = " && ".join([f"sudo {cmd}" for cmd in selected_commands])

        terminal_command = f"konsole -e bash -c '{full_command}; exec bash'"

        try:
            print(f"Executing commands in terminal: {full_command}")
            subprocess.run(terminal_command, shell=True)
            self.output_report = {cmd: self.translations["Command sent for execution."] for cmd in selected_commands}
        except Exception as e:
            self.output_report = {cmd: f'Error starting terminal: {e}' for cmd in selected_commands}

        self.show_report()

    def show_report(self):
        """
        Отображает отчет о выполнении команд в области текста.
        """
        self.report_area.insert(tk.END, f"--- {self.translations['Execution Report']} ---\n")
        for command, status in self.output_report.items():
            self.report_area.insert(tk.END, f"{command}: {status}\n")
        self.report_area.insert(tk.END, "\n")

    def change_language(self, lang):
        """
        Изменяет язык интерфейса приложения.

        :param lang: Новый язык интерфейса ('en' или 'ru').
        """
        try:
            self.translations = load_translation(lang)
            self.root.title(self.translations["Command Executor"])
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Checkbutton):
                    widget.config(text=self.translations[commands[self.root.winfo_children().index(widget)]])
                elif isinstance(widget, tk.Button):
                    widget.config(text=self.translations["Execute Selected Commands"])
                elif isinstance(widget, tk.Menu):
                    for item in widget.winfo_children():
                        if isinstance(item, tk.Menu):
                            for sub_item in item.winfo_children():
                                sub_item.config(label=self.translations["Language"])
                                for sub_sub_item in sub_item.winfo_children():
                                    sub_sub_item.config(label=self.translations["English"] if lang == 'en' else self.translations["Russian"])
        except Exception as e:
            messagebox.showerror(self.translations["Error"], f"Ошибка загрузки перевода: {e}")












