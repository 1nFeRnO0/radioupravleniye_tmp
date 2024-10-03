import socket

def start_server():
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))  # Сервер слушает на всех интерфейсах
    server_socket.listen(5)
    print("Сервер запущен и ожидает подключения...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключен клиент с адресом: {addr}")

        while True:
            # Получаем данные от клиента
            data = client_socket.recv(1024)
            if not data:
                break
            # Выводим нажатую клавишу в консоль
            print(f"Нажатая клавиша: {data.decode('utf-8')}")

        client_socket.close()

if __name__ == "__main__":
    start_server()
