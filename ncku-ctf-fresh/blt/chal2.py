from Crypto.Util.number import *
from itertools import product
from sympy import PolynomialRing, isprime
# from sage import *
import numpy as np
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

N = 4096  # This is the N used in the original encryption

def lll_reduction(B):
    B = np.array(B, dtype=float)
    n = len(B)
    Bstar = np.zeros_like(B, dtype=float)
    Bstar[0] = B[0]

    for j in range(1, n):
        v = B[j]
        for k in range(j):
            mu = np.dot(B[j], Bstar[k]) / np.dot(Bstar[k], Bstar[k])
            v = v - mu * B[k]
        Bstar[j] = v

    # Gram-Schmidt orthogonalization
    for i in range(n):
        for j in range(i):
            mu = np.dot(B[i], Bstar[j]) / np.dot(Bstar[j], Bstar[j])
            B[i] = B[i] - np.round(mu) * B[j]

    return B

# Defining the lattice
N = 2**7
e = 1  # Degree of the polynomial is 1

n = 1  # degree of the polynomial f(x)
M = np.zeros((n+1, n+1), dtype=object )

for i in range(n):
    M[i, i] = p
for i in range(n+1):
    M[n, i] = (h if i == 1 else c) * N ** ((n - i) / e)

# Applying LLL reduction
M = lll_reduction(M)

# Checking if we find small roots; in this simplified case, just check for the last row
g_x = np.poly1d(M[-1][::-1])
roots = np.roots(g_x)

print("Potential roots found:", roots)


