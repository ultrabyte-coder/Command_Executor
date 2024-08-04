import tkinter as tk  # Импортируем библиотеку Tkinter для создания графического интерфейса
from .app import CommandExecutorApp  # Импортируем класс приложения
from .translations import load_translation  # Импортируем функцию загрузки переводов
from .commands import commands  # Импортируем список команд

__version__ = "1.0.0"
__author__ = "ultranumb-coder"

# Создание основного окна приложения и запуск главного цикла
root = tk.Tk()  # Инициализируем главное окно Tkinter
app = CommandExecutorApp(root)  # Создаем экземпляр нашего приложения
root.mainloop()  # Запускаем главный цикл обработки событий

# Определяем публичный интерфейс пакета
__all__ = ["CommandExecutorApp", "load_translation", "commands"]

"""
Как запустить приложение:
1. Клонируйте репозиторий с GitHub:

   git clone https://github.com/ultranumb-coder/Command_Executor.git

2. Перейдите в директорию проекта:

   cd Command_Executor

3. Убедитесь, что у вас установлены все необходимые зависимости для вашего проекта.
4. Импортируйте пакет в вашем Python-скрипте или интерактивной оболочке:

   import Command_Executor  # Импортируйте ваш проект.

5. При выполнении этой команды приложение запустится автоматически.
6. Закройте приложение, используя стандартные средства (например, кнопку закрытия окна).
"""
