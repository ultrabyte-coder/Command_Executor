# Developer Aleksandr Kolesnikov

#### RU

# Command Executor

**Command Executor** — это приложение на Python, использующее библиотеку Tkinter для выполнения команд очистки системы в Linux с возможностью выбора языка интерфейса. 
Данное приложение подходит в основном для пользователей, использующих SSD-диски, так как очистка с помощью команд более безопасна для таких дисков по сравнению с утилитами.

**Важно:** Все команды выполняются с правами суперпользователя (`sudo`). Хотя список выполняемых команд специально подобран так, чтобы исключить риски повредить систему, 
тем не менее, автор не несет ответственности за любые проблемы или последствия, возникающие в результате выполнения команд.

## Описание

Это приложение позволяет пользователям выбирать команды для выполнения и отправлять их в терминал. 
Поддерживаются языки: английский и русский. Приложение выводит отчет о выполненных командах в области текста.

## Установка

1. Убедитесь, что у вас установлен Python 3.11.
2. Скачайте или клонируйте репозиторий:

   ```bash
   git clone https://github.com/ultranumb-coder/Command_Executor
   cd Command_Executor
   
### Настройка терминала

1. Прежде чем запускать приложение, убедитесь, что вы указали правильный терминал. 
Вы можете узнать, какой терминал используется в вашей системе, выполнив следующую команду в терминале:

   ```bash
   echo $TERM

2. Затем откройте файл кода приложения и найдите строку, где определяется переменная terminal_command. 
3. Измените её на соответствующий вашему терминалу формат. Например, для терминала Konsole используйте:

terminal_command = f"konsole -e bash -c '{full_command}; exec bash'"

Для других терминалов замените konsole на название вашего терминала. Примеры:

- Для GNOME Terminal:
  - terminal_command = f"gnome-terminal -- bash -c '{full_command}; exec bash'"

- Для XFCE Terminal:
  - terminal_command = f"xfce4-terminal -e 'bash -c \"{full_command}; exec bash\"'"

## Использование

1. Запустите приложение:

python main.py

2. Выберите желаемые команды из списка доступных.
3. Нажмите кнопку "Execute Selected Commands" для выполнения выбранных команд.
4. Отчет о выполнении появится в текстовой области ниже.

## Команды

Приложение поддерживает следующие команды очистки системы:

- apt update: Обновляет список пакетов в системе, загружая информацию о новых версиях программного обеспечения и зависимостях.
- apt upgrade -y: Устанавливает обновления для всех установленных пакетов. Опция -y автоматически подтверждает установку без запроса на подтверждение.
- apt clean: Удаляет все загруженные файлы пакетов из кеша, освобождая место на диске.
- apt autoclean: Удаляет старые версии загруженных пакетов, которые больше не могут быть загружены, освобождая место на диске.
- apt autoremove -y: Удаляет пакеты, которые были установлены автоматически и больше не требуются другими пакетами. Опция -y автоматически подтверждает удаление.
- journalctl --vacuum-time=3d: Удаляет журналы системы старше 3 дней. Это помогает сократить объем занимаемого места.
- journalctl --vacuum-size=100M: Удаляет журналы системы до тех пор, пока общий размер журналов не станет меньше 100 МБ.
- systemd-tmpfiles --clean: Очищает временные файлы в системах, использующих systemd, согласно настройкам, указанным в конфигурационных файлах.

## Переводы

Для изменения языка интерфейса выберите нужный язык из меню "Language" в верхней части окна.

## Зависимости

- tkinter
- subprocess

## Лицензия 

Этот проект является личной собственностью и предоставляется в безвозмездное пользование.

## Контакты:

Если у вас есть вопросы или предложения, вы можете связаться со мной по электронной почте: developer_python@list.ru

#### ====================================================================================================================

# Developer Aleksandr Kolesnikov

#### EN 

# Command Executor

**Command Executor** is a Python application that uses the Tkinter library to execute system cleanup commands in Linux, with the option to choose the interface language. This application is primarily suitable for users with SSD drives, as command-based cleanup is safer for such drives compared to utilities.

**Important:** All commands are executed with superuser privileges (`sudo`). Although the list of commands is specifically curated to minimize risks to the system, the author is not responsible for any issues or consequences arising from executing these commands.

## Description

This application allows users to select commands for execution and send them to the terminal. Supported languages are English and Russian. The application outputs a report of executed commands in the text area.

## Installation

1. Ensure that you have Python 3.11 installed.
2. Download or clone the repository:

   ```bash
   git clone https://github.com/ultranumb-coder/Command_Executor
   cd Command_Executor
   
### Terminal Setup

1. Before running the application, make sure you specify the correct terminal. 
You can find out which terminal is being used on your system by executing the following command in the terminal:

    ```bash
    echo $TERM
   
2. Then open the application's code file and find the line where the terminal_command variable is defined.
3. Change it to the format corresponding to your terminal. For example, for Konsole terminal use:

terminal_command = f"konsole -e bash -c '{full_command}; exec bash'"

For other terminals, replace konsole with the name of your terminal. Examples:

- For GNOME Terminal:
    - terminal_command = f"gnome-terminal -- bash -c '{full_command}; exec bash'"

- Для XFCE Terminal:
  - terminal_command = f"xfce4-terminal -e 'bash -c \"{full_command}; exec bash\"'"

## Usage
1. Run the application:

python main.py

1. Select the desired commands from the available list.
2. Click the "Execute Selected Commands" button to run the selected commands.
3. A report of the execution will appear in the text area below.

## Commands

The application supports the following system cleanup commands:

- apt update: Updates the package list on the system by downloading information about new versions of software and dependencies.
- apt upgrade -y: Installs updates for all installed packages. The -y option automatically confirms the installation without prompting for confirmation.
- apt clean: Removes all downloaded package files from the cache, freeing up disk space.
- apt autoclean: Removes old versions of downloaded packages that can no longer be retrieved, freeing up disk space.
- apt autoremove -y: Removes packages that were installed automatically and are no longer needed by other packages. The -y option automatically confirms the removal.
- journalctl --vacuum-time=3d: Deletes system logs older than 3 days. This helps reduce the amount of occupied space.
- journalctl --vacuum-size=100M: Deletes system logs until the total size of the logs is less than 100 MB.
- systemd-tmpfiles --clean: Cleans temporary files in systems using systemd according to the settings specified in configuration files.

## Translations

To change the interface language, select the desired language from the "Language" menu at the top of the window.

## Dependencies

- tkinter
- subprocess

## License

This project is personal property and is provided for free use.

## Contact:

If you have any questions or suggestions, you can contact me via email: developer_python@list.ru