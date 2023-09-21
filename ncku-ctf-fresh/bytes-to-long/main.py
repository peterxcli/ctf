from Crypto.Util.number import long_to_bytes

number = 13244450863494047605825006411187863089110804298522984451942523304347184035193280522988022813656920792436221744079819183346774909
# number = 12045757888239720710727008441727923173117452188741573932222032901948484557105264590521582342522349838037134087579773

# Convert the given number to bytes using long_to_bytes
decoded_bytes = long_to_bytes(number)

# Decode the bytes to a string (assuming it's utf-8 encoded)
try:
    decoded_str_using_long_to_bytes = decoded_bytes.decode('utf-8')
except UnicodeDecodeError:
    decoded_str_using_long_to_bytes = "Unable to decode as UTF-8."

print(decoded_str_using_long_to_bytes)
