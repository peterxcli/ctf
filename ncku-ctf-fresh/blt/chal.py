from Crypto.Util.number import *
from itertools import product
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

# Step 1: Enumerate possible primes for f, g, and r
possible_f_values = [getPrime(N // 2) for _ in range(100)]  # Replace 100 with a reasonable number
possible_g_values = [getPrime(N // 4) for _ in range(100)]  # Replace 100 with a reasonable number
possible_r_values = [getPrime(N // 2) for _ in range(100)]  # Replace 100 with a reasonable number

# Step 2: Attempt decryption for each combination
for f, g, r in product(possible_f_values, possible_g_values, possible_r_values):
    f_inv = inverse(f, p)
    if f_inv * g % p == h:  # Check if this f and g could produce the given h
        # Attempt decryption
        m_candidate = (c - r * h) * f_inv % p
        m_candidate_bytes = long_to_bytes(m_candidate)

        # If the decrypted bytes make sense or match some known pattern, we may have found the flag
        if m_candidate_bytes.startswith(b'NCKUCTF{') and m_candidate_bytes.endswith(b'}'):
            print(f"Found the flag: {m_candidate_bytes.decode()}")
            break