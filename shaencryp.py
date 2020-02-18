import hashlib
#print(hashlib.algorithms_available)
#password="JASNA"
obj=hashlib.sha1(b'password')
encrypted_password=obj.hexdigest()
print(encrypted_password)