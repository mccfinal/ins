import math
l="abcdefghijklmnopqrstuvwxyz"
pt=input("Enter plain text: ")
pt=pt.replace("","")
lenk=int(input("Enter length of key: "))
k=[]
for i in range(0,lenk):
    v=int(input("Enter key"+str(i+1)+": "))
    k.append(v)
en=""
de=""
n=0
for i in range(0,len(pt)):
    if(n<len(k)):
        n=n+1
    if(n>=len(k)):
        n=0
    ind=l.index(pt[i])+k[n-1]
    en=en+l[ind%26]
n=0
print("Encrypted text: ",en)
for i in range(0,len(pt)):
    if(n<len(k)):
        n=n+1
    if(n>=len(k)):
        n=0
    ind=l.index(en[i])-k[n-1]
    de=de+l[ind%26]

print("Decrypted text: ",de)
