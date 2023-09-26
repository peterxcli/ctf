from subprocess import Popen, PIPE, STDOUT
import shutil

def decrypt_file(input_file, output_file, password, algorithm):
    # Use OpenSSL to decrypt the file
    cmd = f'openssl enc -d -{algorithm} -in {input_file} -out {output_file} -pass pass:{password}'
    process = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    output, _ = process.communicate()

    # Check if the decryption was successful by examining the return code
    if process.returncode == 0:
        print("Decryption successful.")
    else:
        print(f"Decryption failed. Error: {output.decode('utf-8')}")

# File paths
input_file_path = 'ipad.enc'
output_file_path = 'file.txt'

# Password and algorithm
password = 'kazma'
algorithm = 'aes-256-cbc'

# Decrypt the file
decrypt_file(input_file_path, output_file_path, password, algorithm)

# Optionally, rename the output file
decrypted_file_path = 'file.dec'
shutil.move(output_file_path, decrypted_file_path)
