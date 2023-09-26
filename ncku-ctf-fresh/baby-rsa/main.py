# Let's read the contents of the uploaded file to see what it contains.
with open("output.txt", "r") as file:
    file_content = file.read()

file_content

from sympy import mod_inverse

# Extract the values from the file content
p = int(file_content.split("p: ")[1].split("\nq: ")[0])
q = int(file_content.split("q: ")[1].split("\ne: ")[0])
e = int(file_content.split("e: ")[1].split("\nc: ")[0])
c = int(file_content.split("c: ")[1])

# Calculate n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1) ## ϕ(N)

# Compute the private exponent d
d = mod_inverse(e, phi_n)

# Decrypt the message
M = pow(c, d, n)

M

from Crypto.Util.number import long_to_bytes

# Convert the decrypted message from a long integer to bytes
decrypted_bytes = long_to_bytes(M)
# decrypted_bytes.decode(errors='replace')  # Attempt to decode the bytes to a readable string
print(decrypted_bytes.decode(errors='replace'))  # Attempt to decode the bytes to a readable string