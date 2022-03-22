from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import sys


def cifrar(input_file, output_file, input_key):
    key = open(input_key, 'rb').read()
    serialization_key = serialization.load_pem_public_key(
        key,
        backend=default_backend()
    )
    input_data = open(input_file, 'rb').read()
    data_encryption = serialization_key.encrypt(input_data, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    print(data_encryption)
    output = open(output_file, 'wb')
    output.write(data_encryption)
    output.close()


def descifrar(input_file, output_file, input_key):
    key = open(input_key, 'rb').read()
    serialization_key = serialization.load_pem_private_key(
        key,
        backend=default_backend(),
        password=None
    )
    input_data = open(input_file, 'rb').read()
    message_decryption = serialization_key.decrypt(
      input_data,
      padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
      )
    )
    output = open(output_file, 'wb')
    output.write(message_decryption)
    output.close()


def operation(operation_rsa):
    if operation_rsa == 'cifrar':
        cifrar(input_file, output_file, input_key)
    elif operation_rsa == 'descifrar':
        descifrar(input_file, output_file, input_key)


if __name__ == '__main__':
    # Entradas
    if len(sys.argv) < 5:
        print('Error')
        exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_key = sys.argv[3]
    operation_rsa = sys.argv[4]
    operation(operation_rsa)
