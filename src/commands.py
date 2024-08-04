# Список команд для выполнения
commands = [
    "apt update",
    "apt upgrade -y",
    "apt clean",
    "apt autoclean",
    "apt autoremove -y",
    "journalctl --vacuum-time=3d",
    "journalctl --vacuum-size=100M",
    "systemd-tmpfiles --clean"
]