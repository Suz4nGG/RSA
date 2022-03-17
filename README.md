# RSA
- Crear un script que genera la llave pública y privada en las rutas
elegidas por el usuario (a partir de dos parámetros) y guarda el resultado en formato PEM.

- Crear un script que recibe como parámetro la ruta de una
llave pública o privada (según sea el caso) en formato PEM, la ruta de
un archivo de texto plano o cifrado (por ahora sólo archivos de
texto) y la operación a realizar (cifrar o descifrar)

* Usar la versión completa de RSA con padding
Ejecución: 
python3 generate_keys_rsa.py private_key.pem public_key.pem
Ejecución: 
python3 RSA.py michi.txt michi.cif public_key.pem cifrar
python3 RSA.py michi.cif michi.des private_key.pem descifrar
