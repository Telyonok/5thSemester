import random

def find_primitive_element(modulus):
    for g in range(2, modulus):
        powers = set()
        for i in range(1, modulus):
            power = pow(g, i, modulus)
            if power in powers:
                break
            powers.add(power)
        else:
            return g
    return None

def generate_private_key():
    return random.randint(1000, 9999)

P = 7351
g = find_primitive_element(P)
print("Primitive element g in GF({}) is: {}".format(P, g))

private_key_A = generate_private_key()
print("Generated private key A:", private_key_A)
public_key_A = pow(g, private_key_A, P)
print("Public key A:", public_key_A)

private_key_B = generate_private_key()
print("Generated private key B:", private_key_B)
public_key_B = pow(g, private_key_B, P)
print("Public key B:", public_key_B)

shared_secret_A = pow(public_key_B, private_key_A, P)

shared_secret_B = pow(public_key_A, private_key_B, P)

print("Shared secret A:", shared_secret_A)
print("Shared secret B:", shared_secret_B)



#Используя библиотеку:

#import galois

#P = 7351
#GF = galois.GF(P)
#g = GF.primitive_elements[0]
#print("Primitive element g in GF({}) is: {}".format(P, g))