from io import BytesIO
from itertools import cycle

for i in range(1000):
    file_name = str(i) + ".dat"

    data = bytearray(open(file_name, 'rb').read())

    f2 = open("merge.zip", "ab")
    f2.write(data)
    f2.close()

