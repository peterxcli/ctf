import random
import string

flag = b"NCKUCTF{???????????????????????}"
x = flag[8:-1]
# for i in x:
#     print(i, end=", ")
# exit(0)

a = random.randint(1, 1337)
b = random.randint(1, 1337)

with open("veryez.txt", "r") as file:
    content = file.read()

content = content.split(",")
content = [int(i.strip("[] ")) for i in content]
print(content)

# for i, x in enumerate(string.printable[:-6].encode()):
#     print(i, x)
# exit(0)
# print(string.printable[:-38].encode())


seg = [[a, b] for a in range(1, 1337) for b in range(1, 1337)]
# print(seg)
ans = []

col = (string.printable[:-38] + "_")
for i in range(len(x)):
    tmp = []
    for [a, b] in seg:
        for x in col:
            # print(a, b, ord(x), a * ord(x) + b, content[i])
            if a * ord(x) + b == content[i]:
                tmp.append([a, b])

    seg = tmp
    print(len(seg))

# the proper a, b has been found
print(seg)
[a ,b] = seg[0]
for c in content:
    ans.append(chr((c - b) // a))
print("".join(ans))
# print(ord(max(col)))


# cipher = []
# for i in x:
#     cipher.append(a * i + b)
# print(cipher)
