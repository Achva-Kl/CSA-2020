from stegano import lsb
import base64

encoded_flag = lsb.reveal('pic.png')
decode = base64.b64decode(encoded_flag.encode())
print("flag:", base64.b64decode(decode).decode())