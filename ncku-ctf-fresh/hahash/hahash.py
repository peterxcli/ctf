import hashlib
# from secret import FLAG
import string

output = ""


def hahash(s):
    assert len(s) % 2 == 0
    chunk_num = len(s) // 2
    output = ""

    for i in range(chunk_num):
        chunk = s[2 * i : 2 * (i + 1)]
        ret = hashlib.md5(chunk)
        output += ret.hexdigest()[:8]

    return output


# print(hahash(FLAG))

with open("hahash.txt", "r") as file:
    hahash_txt_content = file.read()

print(hahash_txt_content)

for i in range(0, len(hahash_txt_content), 8):
    # print(hahash_txt_content[: i-8])
    for a in string.printable[:-6]:
        for b in string.printable[:-6]:
            seg = (a + b).encode()
            res = hahash(seg)
            if res == hahash_txt_content[i: i+8]:
                output += a + b
                break

print(output)
