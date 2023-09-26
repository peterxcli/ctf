# (x1, 0), (x2, 0) -> (x1, x2, ..., xn)
# (x - x1) * (x - x2) = 0
# x^n + ax^(n-1) ..... + cx^2 + x + 1 = 0

from Crypto.Util.number import getPrime, bytes_to_long
from numpy.polynomial import polynomial as P
from secret import FLAG

primes = []
for i in range(5):
    primes.append(getPrime(512))

pt = bytes_to_long(FLAG)
N = primes[0] * primes[1] * primes[2] * primes[3] * primes[4]
e = 0x10001
c = pow(pt, e, N)
print(f"N = {N} \ne = {e} \nc = {c}")

coefficients = P.polyfromroots(primes)
print(f"Although I am evil, I'll give you a hint")
print(
    f"The polynomial is: ({coefficients[5]}) * x ** 5 + ({coefficients[4]}) * x ** 4 + ({coefficients[3]}) * x ** 3 + ({coefficients[2]}) * x ** 2 + ({coefficients[1]}) * x + {coefficients[0]}"
)
print(f"There is no formula for solving polynomial of degree 5, haha! Good luck. - Yona")


def test(x):
    return (
        x**5 * coefficients[5]
        + x**4 * coefficients[4]
        + x**3 * coefficients[3]
        + x**2 * coefficients[2]
        + x * coefficients[1]
        + coefficients[0]
    )


for i in primes:
    assert (
        test(i) == 0
    )  # Sanity check: f(primes[0])=f(primes[1])=f(primes[2])=f(primes[3])=f(primes[4])=0
