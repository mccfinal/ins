import hashlib
import random

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def hash_function(data):
    return int(hashlib.sha256(data.encode()).hexdigest(), 16)

def generate_signature(p, q, a, s, M):
    r = random.randint(1, q-1)
    X = mod_exp(a, r, p)
    e = hash_function(f"{M}{X}") % q
    y = (r + s * e) % q
    return X, e, y

def verify_signature(p, q, a, v, M, X, e, y):
    X_prime = (mod_exp(a, y, p) * mod_exp(v, e, p)) % p
    e_prime = hash_function(f"{M}{X_prime}") % q
    return e == e_prime

# Input parameters
p = int(input("Enter the prime number p: "))
q = int(input(f"Enter the factor q of {p-1}: "))
a = int(input(f"Enter the base a such that a^{q} = 1 mod {p}: "))
s = int(input(f"Enter the private key s (0 < s < {q}): "))
M = input("Enter a message to be signed: ")

# Public key v
v = mod_exp(a, q - s, p)  # Correct modular exponentiation for public key

# Generate signature
X, e, y = generate_signature(p, q, a, s, M)
print(f"Generated Signature:")
print(f"X: {X}")
print(f"e: {e}")
print(f"y: {y}")

# Verify signature
is_valid = verify_signature(p, q, a, v, M, X, e, y)
print(f"Signature valid: {is_valid}")
