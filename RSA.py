import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# RC4-like encryption function (actually RSA encryption in the code)
def rc4(p, q, m):
    if not is_prime(p) or not is_prime(q):
        raise Exception("One or both of the numbers are not prime.")
    if m >= p * q:
        raise Exception("Plaintext must be less than the product of p and q.")
    
    n = p * q
    phi = (p - 1) * (q - 1)

    # Find e such that 1 < e < phi and gcd(e, phi) == 1
    e = 2
    while e < phi:
        if math.gcd(e, phi) == 1:
            break
        e += 1

    # Find d such that (d * e) % phi == 1
    d = 2
    while (d * e) % phi != 1:
        d += 1

    # Encryption
    ct = pow(m, e, n)
    print("Ciphertext is:", ct)

    # Decryption
    pt = pow(ct, d, n)
    print("Plaintext is:", pt)

# Main program
try:
    p = int(input("Enter the 1st prime number: "))
    q = int(input("Enter the 2nd prime number: "))
    m = int(input("Enter the plaintext (must be less than the product of both prime numbers): "))
    
    rc4(p, q, m)

except ValueError:
    print("Invalid input. Please enter integer values.")
except Exception as e:
    print(e)
