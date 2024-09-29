#HMAC SHA1
import hashlib
import hmac
#def hmac_sha(key, message):
 #   return hmac.new(key.encode("utf-8"), message.encode("utf-8"), hashlib.sha1).hexdigest()
#key = input("Enter your key: ")
#message = input("Enter your message: ")
#print("HMAC-SHA1 isgnature of your message is ", hmac_sha(key, message))



def sha(m):
    hash1 = hashlib.sha1(m.encode())  # Encode the message to bytes
    print("SHA-1 signature of your message is:", hash1.hexdigest())
pt = input("Enter message: ")
sha(pt)
