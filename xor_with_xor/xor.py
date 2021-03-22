from io import BytesIO
from itertools import cycle

def xor(data, key):
    l = len(key)
    return bytearray(((data[i] ^ key[i % l]) for i in range(0,len(data))))

data = bytearray(open('xor-with-xor.bin', 'rb').read())

key = bytearray('xor', 'utf8')
print(type(data))
print(type(key))

ans = xor(data, key)

print(ans[0:100])

f2 = open("after_xor.zip", "wb")
f2.write(ans)
f2.close()
