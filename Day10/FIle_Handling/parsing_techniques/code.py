## dumps(): Encryption
## loads(): Decryption 

'''
1. JSON
2. pickle

'''

import json
file = open('temp1.txt', 'a+')
data = {
    'Fullname' : 'Rakhi Ahuja',
    'userId' : 'user123',
    'password' : '*****'
}

# print(f'Original Data: {data}')
# print(f'type of Original data: {type(data)}')
# enc_data = json.dumps(data)
# file.write(enc_data)

# file.seek(0)

# enc_data = file.read()
# print(type(enc_data))

# ori_data = json.loads(enc_data)
# print(ori_data, type(ori_data))

# enc_data = json.dumps(data)

# print(f'Encrypted Data: {enc_data}')
# print(f'type of Encrypted data: {type(enc_data)}')
# print()

# decrpt_data = json.loads(enc_data)

# print(f'Decrypted Data: {decrpt_data}')
# print(f'type of Decrypted data: {type(decrpt_data)}')
# print()


import pickle
file = open('temp.txt', 'ab+')
data = {
    'Fullname' : 'Rakhi Ahuja',
    'userId' : 'user123',
    'password' : '*****'
}

print(f'Original Data: {data}')
print(f'type of Original data: {type(data)}')
enc_data = pickle.dumps(data)
file.write(enc_data)

file.seek(0)

enc_data = file.read()
print(type(enc_data))

ori_data = pickle.loads(enc_data)
print(ori_data, type(ori_data))

# enc_data = pickle.dumps(data)

# print(f'Encrypted Data: {enc_data}')
# print(f'type of Encrypted data: {type(enc_data)}')
# print()

# decrpt_data = pickle.loads(enc_data)

# print(f'Decrypted Data: {decrpt_data}')
# print(f'type of Decrypted data: {type(decrpt_data)}')
# print()

file.close()
