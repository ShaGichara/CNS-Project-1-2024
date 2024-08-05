from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    encrypted_data = [cipher_suite.encrypt(str(d).encode()).decode() for d in data]
    return encrypted_data
    
