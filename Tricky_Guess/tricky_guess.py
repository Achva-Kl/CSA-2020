import socket
from collections import Counter

s = socket.socket()
s.connect(('3.123.155.56',2222))
print(s.recv(1500))
print(s.recv(6))


with open('words.txt') as f:
    words = f.readlines()

word_to_check = words[0]
byt=words[0].encode()
s.send(byt)
dataFromServer = s.recv(50).decode()
words.remove(word_to_check)

while len(dataFromServer) == 1 or len(dataFromServer) == 2:
    for word in words:
        common_letters = Counter(word) & Counter(word_to_check)
        num_common = sum(common_letters.values())-1
        if num_common < int(dataFromServer) or num_common > int(dataFromServer):
             words.remove(word) 

    word_to_check = words[0]
    words.remove(word_to_check)
    byt=word_to_check.encode()
    s.send(byt)
    dataFromServer = s.recv(50).decode()
    #print(dataFromServer)
print("flag: " + dataFromServer)

s.close()
