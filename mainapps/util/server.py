import socket

def start(port):
    # 1. 创建socket
    server_socket = socket.socket()

    # 2. 绑定端口
    server_socket.bind(('', port))

    # 3. 开始监听
    server_socket.listen()
    print('---启动服务----')

    # 4. 等待客户端的连接
    client, address = server_socket.accept()  # 阻塞到有客户端连接为止

    # 5. 向客户端发送数据
    client.send(f'{address}连接成功!'.encode())

    while True:
        # 6. 接收客户端发来的数据
        msg = client.recv(1024)
        if b'0' == msg:
            break

        print(msg.decode())
        client.send('ok'.encode())

    client.send(b'0')
    server_socket.close()
    print('---退出服务----')


if __name__ == '__main__':
    start(8050)