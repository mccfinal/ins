def mod_exp(base,exp,mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
        return result

def mod_inv(a,p):
    for x in range(1,p):
        if ((a*x) % p) == 1:
            return x
    return None

def elgamel_algo(message,p,g,x):
    y = mod_exp(g,x,p)
    k = 3
    r = mod_exp(g,k,p)
    k_inv = mod_inv(k,p-1)
    s = (k_inv * (message - x * r)) % (p-1)
    return r,s

def elgamel_verify(message,r,s,p,g,y):
    v1 = (mod_exp(y,r,p) * mod_exp(r,s,p)) % p
    v2 = mod_exp(g, message, p)
    return v1 == v2

