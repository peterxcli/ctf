import os
from secret import FLAG

key1 = os.urandom(len(FLAG))
key2 = os.urandom(len(FLAG))
key3 = xor(key1, key2)

print(f"cipher1:{bytes.hex(xor(FLAG,key1))}")
print(f"cipher2:{bytes.hex(xor(FLAG,key2))}")
print(f"cipher3:{bytes.hex(xor(FLAG,key3))}")

