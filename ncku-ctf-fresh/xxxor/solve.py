def xor(text, key):
    return bytes(a ^ b for a, b in zip(text, key))

# Convert the ciphers from hex to bytes
cipher1_bytes = bytes.fromhex("0ad9aba65c1513e30afdd562e15890b02447832a204309bc1709d1")
cipher2_bytes = bytes.fromhex("be1854e0bbdb439920c174b445eadd287cd8e0d2c7062e679b1538")
cipher3_bytes = bytes.fromhex("fa82b413a49a16015263d9e6d6ed35c72ff60fc9b82214ecd32c94")

# Compute key2 using the XOR property
key2 = bytes(a ^ b for a, b in zip(cipher1_bytes, cipher3_bytes))

# Compute FLAG using key2
flag_bytes = bytes(a ^ b for a, b in zip(cipher2_bytes, key2))

# Convert the FLAG bytes to a string
flag = flag_bytes.decode('utf-8', errors='ignore')

print(flag)
