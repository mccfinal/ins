def plaintext(text, key):
    text = text.lower()
    text = text.replace(" ", "")
    while len(text) % len(key) != 0:
        text += "x"
    return text

def keyList(key):
    return list(key)

def matrix_encrypt(text, list1):
    m = []
    index = 0
    for i in range(len(text) // len(list1)):
        a = []
        for j in range(len(list1)):
            if index < len(text):
                a.append(text[index])
                index += 1
        m.append(a)
    print("Matrix: ")
    for i in range(len(text) // len(list1)):
        for j in range(len(list1)):
            print(m[i][j], end=" ")
        print()
    return m

def encrypt(m, list1, list2, text):
    en = ""
    row = len(text) // len(list1)
    sorted_key = sorted(list2)
    for k in range(len(sorted_key)):
        num = list1.index(sorted_key[k])
        for i in range(row):
            en += m[i][num]
    print("Cipher text: ", en)
    return en

def encryptionAlgo(text, key):
    plain_text = plaintext(text, key)
    key_list1 = keyList(key)
    key_list2 = keyList(key)
    print("Plain text:", plain_text)
    print("Key list:", key_list1)
    m_plain = matrix_encrypt(plain_text, key_list1)
    cipher = encrypt(m_plain, key_list1, key_list2, plain_text)
    return cipher

def matrix_list(cipher, list1):
    sorted_key = sorted(list1)
    var = len(cipher) // len(list1)
    mat_list = [''] * len(cipher)
    index = 0
    for k in range(len(sorted_key)):
        num = list1.index(sorted_key[k])
        for i in range(var):
            mat_list[num + i * len(list1)] = cipher[index]
            index += 1
    print("List of matrix characters: ", mat_list)
    return mat_list

def matrix_decrypt(mat_list, list1):
    m = []
    for i in range(len(list1)):
        a = []
        for j in range(len(mat_list) // len(list1)):
            a.append(mat_list[i + j * len(list1)])
        m.append(a)
    print("Columnwise groups of matrix characters: ", m)
    print("Matrix: ")
    for i in range(len(mat_list) // len(list1)):
        for j in range(len(list1)):
            print(m[j][i], end=" ")
        print()
    return m

def decryption(m, mat_list, list1):
    de = ""
    row = len(mat_list) // len(list1)
    for i in range(row):
        for j in range(len(list1)):
            de += m[j][i]
    print("Plain text: ", de)
    return de

def decryptionAlgo(cipher, key):
    list1 = keyList(key)
    mat_list = matrix_list(cipher, list1)
    m = matrix_decrypt(mat_list, list1)
    plain = decryption(m, mat_list, list1)
    return plain

text = input("Enter plaintext: ")
key = input("Enter key: ")

print("Encryption goes here!!!")
cipher = encryptionAlgo(text, key)

print("Decryption goes here!!!")
plain = decryptionAlgo(cipher, key)
