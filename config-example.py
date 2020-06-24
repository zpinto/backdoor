import os
# rename this file to config.py and add desired values


class CONFIG:
    dirname = os.path.dirname(__file__)
    host = "127.0.0.1"
    port = 3001
    pwd = "secret"
    key_file = os.path.join(dirname, "secret.key")
