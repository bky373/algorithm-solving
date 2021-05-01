import hashlib

s = input()
hash_object = hashlib.sha256()
hash_object.update(s.encode())
result = hash_object.hexdigest()

print(result)
