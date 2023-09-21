from Crypto.Util.number import *
from itertools import product
from sympy import isprime
# from secret import FLAG


class NTRU:
    def __init__(self, N):
        p, f, g = getPrime(N), getPrime(N // 2), getPrime(N // 4)
        self.N = N
        self.p = p
        self.h = pow(f, -1, p) * g % p

    def encrypt(self, m):
        self.r = getPrime(self.N // 2)
        self.c = (self.r * self.h + m) % self.p
        self.print()

    def print(self):
        with open("out.txt", "w") as f:
            f.write(f"p = {self.p}\nh = {self.h}\nc = {self.c}")

# if __name__ == "__main__":
#     ntru = NTRU(4096)
#     assert len(FLAG) <= 128
#     ntru.encrypt(bytes_to_long(FLAG))


with open("out.txt", "r") as f:
    output_content = f.read()
encrypted_message_str = output_content.split("\n")
# print(encrypted_message_str)
p = int(encrypted_message_str[0].split(" = ")[1])
h = int(encrypted_message_str[1].split(" = ")[1])
c = int(encrypted_message_str[2].split(" = ")[1])
# print(f"p = {p}")
# print(f"h = {h}")
# print(f"c = {c}")

N = 4096  # This is the N used in the original encryption


def find_r(diff, h, p, N):
    for r_candidate in range(2, N//2):
        if not isprime(r_candidate):
            continue
        if (r_candidate * h) % p == diff:
            return r_candidate
    return None


N = 4096

# Known prefix
known_prefix = "NCKUCTF{"
m_prefix = bytes_to_long(known_prefix.encode())

# Calculate c - m_prefix mod p
diff = (c - m_prefix) % p

# Find the value of r
r = find_r(diff, h, p, N)

if r is not None:
    # Calculate the original message m
    m = (c - r * h) % p

    # Convert m back to bytes
    flag = long_to_bytes(m).decode('utf-8')

    print("Decrypted FLAG:", flag)
else:
    print("Could not find a suitable value for r.")
