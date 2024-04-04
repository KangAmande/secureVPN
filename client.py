import socket
import hashlib
from cryptography.fernet import Fernet

# This is a test secret key.
# TODO Improve the authentication and encryption in this file.
SECRET_KEY = Fernet.generate_key()
fernet = Fernet(SECRET_KEY)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(("127.0.0.1",1194))
        print(f"Connected to server at 127.0.0.1:1194")

        # Send the secret key as an authentication token
        client_socket.send(SECRET_KEY)

        # Encrypt the message
        message = fernet.encrypt(b"Hello from client!")
        client_socket.send(message)

        response = client_socket.recv(1024)

        # Decrypt the response
        decrypted_response = fernet.decrypt(response)
        print(f"Received from server: {decrypted_response.decode('utf-8')}")
    except Exception as e:
        print(f"Error connecting to server: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()

