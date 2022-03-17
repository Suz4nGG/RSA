from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import sys


def generate_private_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend())
    return private_key


def generate_public_key(private_key):
    return private_key.public_key()


def private_key_to_bytes(private_key):
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    return private_key_bytes


def public_key_to_bytes(public_key):
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return public_key_bytes

def output_keys(output_private_key, output_public_key):
    # * Llave privada
    private_key = generate_private_key()
    # * Llave pública
    public_key = generate_public_key(private_key)
    output = open(output_private_key, 'wb')
    output.write(private_key_to_bytes(private_key))
    output.close()
    output = open(output_public_key, 'wb')
    output.write(public_key_to_bytes(public_key))
    output.close()

if __name__ == '__main__':
    output_private_key = sys.argv[1]
    output_public_key = sys.argv[2]
    output_keys(output_private_key, output_public_key)
