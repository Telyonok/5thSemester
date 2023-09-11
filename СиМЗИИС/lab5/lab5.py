import random
import math
import os
import sys


def generate_prime_number(bit_length):
    while True:
        p = random.getrandbits(bit_length)
        p |= (1 << bit_length - 1) | 1
        if is_prime(p):
            return p

def is_prime(n, k=5):
    if n <= 3:
        return n == 2 or n == 3
    elif n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y
    
def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g == 1:
        return x % m

def generate_keypair(bit_length):
    p = generate_prime_number(bit_length)
    q = generate_prime_number(bit_length)
    while p == q:
        q = generate_prime_number(bit_length)
    n = p * q               
    phi = (p - 1) * (q - 1)     # Значение функции Эйлера
    e = 65537                   # Полностью состоит из '1' в двоичном представлении. Открытая экспонента.
    d = mod_inverse(e, phi)     # Мультипликативно обратное к числу e по модулю n.
    return (e, n), (d, n)       # Открытый и закрытый ключи.

def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message] # Вычисление криптограммы
    return encrypted_message


def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message] # Расшифрование
    return "".join(decrypted_message)


def sign(message, private_key):
    d, n = private_key
    signature = [pow(ord(char), d, n) for char in message]
    return signature


def verify(message, signature, public_key):
    e, n = public_key
    decrypted_signature = [pow(char, e, n) for char in signature]
    decrypted_message = [chr(char) for char in decrypted_signature]
    return message == "".join(decrypted_message)


def save_key(key, filename):
    with open(filename, "w") as file:
        key_str = ",".join(str(num) for num in key)
        file.write(key_str)


def load_key(filename):
    with open(filename, "r") as file:
        key_str = file.read()
        key = tuple(int(num) for num in key_str.split(","))
        return key

def get_file_path(filename):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, filename)

def main():
    if len(sys.argv) != 2:
        print("Usage: python rsa.py <message>")
        return

    bit_length = 1024
    public_key, private_key = generate_keypair(bit_length)
    save_key(public_key, get_file_path("public_key.txt"))
    save_key(private_key, get_file_path("private_key.txt"))

    message = sys.argv[1]
    encrypted_message = encrypt(message, public_key)
    save_key(encrypted_message, get_file_path("encrypted_message.txt"))

    loaded_private_key = load_key(get_file_path("private_key.txt"))
    decrypted_message = decrypt(encrypted_message, loaded_private_key)
    print("Decrypted message:", decrypted_message)

    signature = sign(message, private_key)
    save_key(signature, get_file_path("signature.txt"))

    loaded_public_key = load_key(get_file_path("public_key.txt"))
    loaded_signature = load_key(get_file_path("signature.txt"))
    is_valid = verify(message, loaded_signature, loaded_public_key)
    print("Signature is valid:", is_valid)


if __name__ == "__main__":
    main()