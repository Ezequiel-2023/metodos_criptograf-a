from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
# mensaje a encriptar
mensaje = "este es un ejemplo simetrico para cifrar."

clave = get_random_bytes(16)  #
iv = get_random_bytes(16)

# esto lo cifrara
cipher = AES.new(clave, AES.MODE_CFB, iv)
mensaje_cifrado = cipher.encrypt(mensaje.encode())

mensaje_cifrado_b64 = base64.b64encode(mensaje_cifrado).decode()

print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado (base64): {mensaje_cifrado_b64}")

# esto lo desifrara
cipher_dec = AES.new(clave, AES.MODE_CFB, iv)
mensaje_descifrado = cipher_dec.decrypt(base64.b64decode(mensaje_cifrado_b64)).decode()

print(f"Mensaje descifrado: {mensaje_descifrado}")
