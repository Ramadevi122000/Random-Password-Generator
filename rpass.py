#Miniproject on Random password generator
from random import randint
#Genearting all uppercase password
password = ""
for i in range(8):
    i = chr(randint(65, 98))
    password = str(password) + i

print("The uppercase random password is: ",password)

#Generating upper and lower case password
password = ""
for i in range(5):
    i = chr(randint(65, 98))
    for j in range(5):
        j = chr(randint(65, 98)).lower()

    password = str(password) + i + j

print("The uppercase and lowercase random password is: ",password)

#Genearating uppercase ,lowecase and digits
password = ""
for i in range(3):
    i = chr(randint(65, 98))
    for j in range(3):
        j = chr(randint(65, 98)).lower()
        for k in range(2):
            k = str(randint(1, 10))
    password = str(password) + i + j + k
print("The Random password(uppercase,lowercase & digits) is: ",password)