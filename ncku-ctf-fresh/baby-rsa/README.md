# RSA Challenge Write-up

## Introduction

RSA encryption is a form of public key cryptography that uses the mathematical properties of large prime numbers to encrypt and decrypt data. While RSA is secure with large prime numbers, using smaller numbers or weak parameters can expose vulnerabilities.

## Challenge

We were provided with values for $p$, $q$, $e$, and $c$ from an RSA implementation:

- $p$ and $q$: Two prime numbers used in RSA.
- $e$ : Public exponent (commonly set to 65537).
- $c$ : Ciphertext (encrypted message).

The goal was to decrypt the ciphertext$c$and retrieve the original message.

## Approach

### 1. **Compute $n$ and $\varphi(n)$:**

- Calculate $n = p \times q$. This value serves as the modulus for both public and private keys.
- Compute the totient $\varphi(n) = (p-1)(q-1)$. This is used in determining the private key.

### 2. **Calculate the Private Exponent$d$:**

- The private exponent $d$ is the modular multiplicative inverse of $e$ modulo $\varphi(n)$.
- This means $d \times e \equiv 1 \mod \varphi(n)$.

### 3. **Decrypt the Message:**

- The original plaintext message$( M )$can be found by calculating$M = c^d \mod n$.

### 4. **Convert the Number to Text:**

- The decrypted value was a large number, which indicated that the original message might have been encoded as a numerical representation of a text string.
- Using the `long_to_bytes` function from the Crypto library, the number was converted back to its original string format.

## Solution

By following the above approach, the decrypted message was:

`NCKUCTF{t0O_345y?Go_try_puRely high School mAth}`

This appears to be a flag for a Capture The Flag (CTF) challenge, indicating that the decryption was successful.

### Conclusion

This challenge highlighted the importance of using secure parameters in RSA. With the provided small prime numbers, the RSA encryption was easily broken. It serves as a reminder that in real-world scenarios, it's crucial to use large prime numbers and secure configurations to ensure the safety of encrypted data.
