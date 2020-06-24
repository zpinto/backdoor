from cryptography.fernet import Fernet
from config import CONFIG

if __name__ == "__main__":
    key = Fernet.generate_key()
    key_file = open(CONFIG.key_file, 'wb')
    key_file.write(key)
    key_file.close()
