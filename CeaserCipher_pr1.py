def encryption(pt,key):
    list1='abcdefghijklmnopqrstuvwxyz'
    en=""
    de=""
    for i in pt.lower():
        k=(list1.index(i)+key)%26
        en+=list1[k] 
    print('Encrypted text: ',en)
pt=input("Enter plain text: ")
key=int(input("Enter key: "))
encryption(pt,key)    


#Decryption
def decryption(pt,key):
    list1='abcdefghijklmnopqrstuvwxyz'
    de=""
    for i in pt.lower():
        k=(list1.index(i)-key)%26
        de+=list1[k]
    print('Decrypted text: ',de)
pt=input("Enter plain text: ")
key=int(input("Enter key: "))
decryption(pt,key)    
