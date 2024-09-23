# BCC 구하기
data = "Hello python"
bcc = 0
for char in data:
    bcc = bcc^ord(char)

send = data + hex(bcc)[2:]
print(send)

recieve = send

print(send[:-2])