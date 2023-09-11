from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image


def encrypt_image_ecb(image_path, key, algorithm):
    cipher = algorithm.new(key, AES.MODE_ECB)
    image = Image.open(image_path)
    image_data = image.tobytes()
    encrypted_data = cipher.encrypt(pad(image_data, algorithm.block_size))
    encrypted_image = Image.frombytes(image.mode, image.size, encrypted_data)
    encrypted_image.show()


def decrypt_image_ecb(encrypted_image_path, key, algorithm):
    cipher = algorithm.new(key, AES.MODE_ECB)
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_data = encrypted_image.tobytes()
    decrypted_data = unpad(cipher.decrypt(encrypted_data), algorithm.block_size)
    decrypted_image = Image.frombytes(encrypted_image.mode, encrypted_image.size, decrypted_data)
    decrypted_image.show()


def encrypt_image_cbc(image_path, key, iv, algorithm):
    cipher = algorithm.new(key, AES.MODE_CBC, iv)
    image = Image.open(image_path)
    image_data = image.tobytes()
    encrypted_data = cipher.encrypt(pad(image_data, algorithm.block_size))
    encrypted_image = Image.frombytes(image.mode, image.size, encrypted_data)
    encrypted_image.show()


def decrypt_image_cbc(encrypted_image_path, key, iv, algorithm):
    cipher = algorithm.new(key, AES.MODE_CBC, iv)
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_data = encrypted_image.tobytes()
    decrypted_data = unpad(cipher.decrypt(encrypted_data), algorithm.block_size)
    decrypted_image = Image.frombytes(encrypted_image.mode, encrypted_image.size, decrypted_data)
    decrypted_image.show()


def encrypt_image_ctr(image_path, key, nonce, algorithm):
    cipher = algorithm.new(key, AES.MODE_CTR, nonce=nonce)
    image = Image.open(image_path)
    image_data = image.tobytes()
    encrypted_data = cipher.encrypt(image_data)
    encrypted_image = Image.frombytes(image.mode, image.size, encrypted_data)
    encrypted_image.show()


def decrypt_image_ctr(encrypted_image_path, key, nonce, algorithm):
    cipher = algorithm.new(key, AES.MODE_CTR, nonce=nonce)
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_data = encrypted_image.tobytes()
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_image = Image.frombytes(encrypted_image.mode, encrypted_image.size, decrypted_data)
    decrypted_image.show()