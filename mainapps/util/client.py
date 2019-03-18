import socket


# 1. 创建socket
client = socket.socket()


# 2. 连接服务器
client.connect(('localhost', 8050))
print('--连接服务器成功---')

# 3. 接收服务器的数据
msg = client.recv(1024)
print(msg.decode())

while True:
    msg = input('> ')  # 当前键盘输入的消息

    # 向服务端发送消息
    client.send(msg.encode())

    msg = client.recv(1024) # 接收消息
    if b'0' == msg:
        break


client.close()
print('---退出连接--')
