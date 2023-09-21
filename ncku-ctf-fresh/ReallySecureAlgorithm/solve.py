# Reading the content of the uploaded output.txt file
with open("output.txt", 'r') as file:
    output_content = file.read()

# output_content

def encrypt_char(char, e, N):
    # Encrypt a single character using the given mechanism.
    m = ord(char)
    return pow(m, e, N)

# Correctly parsing the content to extract the encrypted message and beefsoup value
encrypted_message_str = output_content.split("Btw, the beefsoup:")[0].split("Here's your hint:")[1].strip()[1:-1]  # Extracting the message and removing surrounding brackets
encrypted_message = list(map(int, encrypted_message_str.split(", ")))
beefsoup_new = int(output_content.split("Btw, the beefsoup:")[1].strip())

# Using the brute force approach to decrypt the entire encrypted message
decrypted_bruteforce_new = []

for encrypted_value in encrypted_message:
    for char in range(32, 127):  # Common ASCII values
        if encrypt_char(chr(char), 65536, beefsoup_new) == encrypted_value:
            decrypted_bruteforce_new.append(chr(char))
            break
    else:
        decrypted_bruteforce_new.append("?")  # If no match is found

decrypted_message_new = ''.join(decrypted_bruteforce_new)
print(decrypted_message_new)
