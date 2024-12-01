from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# genera clave
clave = RSA.generate(2048)
clave_publica = clave.publickey()
mensaje = "este es un ejemplo asimetrico."

# clava publica cifrada
cipher_rsa = PKCS1_OAEP.new(clave_publica)
mensaje_cifrado = cipher_rsa.encrypt(mensaje.encode())

print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado: {mensaje_cifrado}")

# clave privada desifrada
cipher_rsa_dec = PKCS1_OAEP.new(clave)
mensaje_descifrado = cipher_rsa_dec.decrypt(mensaje_cifrado).decode()

print(f"Mensaje descifrado: {mensaje_descifrado}")
