import tkinter as tk
from app import CommandExecutorApp

if __name__ == "__main__":
    # Создание основного окна приложения и запуск главного цикла
    root = tk.Tk()
    app = CommandExecutorApp(root)
    root.mainloop()