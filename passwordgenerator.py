import random 

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890#$%&?"
times = 30
length = 64

for i in range (times):
    password = ""
    for x in range(length):
        password += random.choice(chars)
    with open('passwords.txt','w') as f:
        f.write(str(password))
        f.write(str('\n')) 
    print(password)