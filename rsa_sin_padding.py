import gmpy2
import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def rsa_encrypt(m, publickey):
    numbers = publickey.public_numbers()
    return gmpy2.powmod(m, numbers.e, numbers.n)


def rsa_decrypt(c, privatekey):
    numbers = privatekey.private_numbers()
    return gmpy2.powmod(c, numbers.d, numbers.public_numbers.n)


def bytes_to_int(b):
    return int.from_bytes(b, byteorder='big')


def int_to_bytes(i):
    i = int(i)
    return i.to_bytes((i.bit_length()+7)//8, byteorder='big')


def message_to_int(message):
    return bytes_to_int(message)


def cifrar(input_file, output_file, input_key):
    key = open(input_key, 'rb').read()
    serialization_key = serialization.load_pem_public_key(
        key,
        backend=default_backend()
    )
    input_data = open(input_file, 'rb').read()
    bytes_encryption = rsa_encrypt(message_to_int(input_data), serialization_key)
    # * cifrar el mensaje
    message_encryption = int_to_bytes(bytes_encryption)
    output = open(output_file, 'wb')
    # * guardar el texto cifrado
    output.write(message_encryption)
    output.close()
    print(message_encryption)

def descifrar(input_file, output_file, input_key):
    key = open(input_key, 'rb').read()
    serialization_key = serialization.load_pem_private_key(
        key,
        backend=default_backend(),
        password=None
    )
    input_data = open(input_file, 'rb').read()
    message_encryption = bytes_to_int(input_data)
    message_decoded_bytes = rsa_decrypt(message_encryption, serialization_key)
    print(message_decoded_bytes)
    message_decoded = int_to_bytes(message_decoded_bytes)
    # * guardar el texto descifrado
    output = open(output_file, 'wb')
    output.write(message_decoded)
    output.close()


def operation(operation_rsa):
    if operation_rsa == 'cifrar':
        cifrar(input_file, output_file, input_key)
    elif operation_rsa == 'descifrar':
        descifrar(input_file, output_file, input_key)


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Error')
        exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_key = sys.argv[3]
    operation_rsa = sys.argv[4]
    operation(operation_rsa)

"""
*
python3 generate_keys_rsa.py private_key.pem public_key.pem
^
python3 RSA.py michi.txt michi.cif public_key.pem cifrar
^
python3 RSA.py michi.cif michi.des private_key.pem descifrar
"""