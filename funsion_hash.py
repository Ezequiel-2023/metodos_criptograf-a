import hashlib
mensaje = "este mensaje se volvera un hash."
hash_obj = hashlib.sha256(mensaje.encode())
hash_hex = hash_obj.hexdigest()

print(f"Mensaje original: {mensaje}")
print(f"Hash (SHA-256): {hash_hex}")

