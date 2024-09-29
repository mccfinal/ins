from sympy import isprime, primitive_root

def proot(n):
    if isprime(n):
        r = primitive_root(n)
        return r
    else:
        print("enter prime number!!")
        return False

n = int(input("enter prime number"))
np = proot(n)
xa = int(input(f"enter first random number less than {n} :"))
xb = int(input(f"enter second random number less than {n} :"))
fa = np **xa % n
fb = np ** xb % n

key_a = fb ** xa % n
key_b = fa ** xb % n

print(f"key1 ={key_a} \n key2 ={key_b}")
