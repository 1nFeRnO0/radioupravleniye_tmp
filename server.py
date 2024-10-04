import socket

def start_server():
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))  # Сервер слушает на всех интерфейсах
    server_socket.listen(5)
    print("Сервер запущен и ожидает подключения...")

    movement_dict = {'w': ['w','w'],
                    's': ['s', 's'],
                    'a': ['s', 'w'],
                    'd': ['w','s']}

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключен клиент с адресом: {addr}")

        while True:
            # Получаем данные от клиента
            data = client_socket.recv(1024)
            data_decode = data.decode('utf-8')
            if not data:
                break
            # Передаем нажатую клавишу для распределения по гусеницам
            movement(movement_dict, data_decode)
            
            # Выводим нажатую клавишу в консоль
            # print(f"Нажатая клавиша: {data.decode('utf-8')}")

        client_socket.close()

def movement(mov_dict, data):
    if data in mov_dict:
        print('Движение левой гусеницы: ', mov_dict[data][0])
        print('Движение правой гусеницы: ', mov_dict[data][1])

if __name__ == "__main__":
    start_server()
