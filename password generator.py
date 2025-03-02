import secrets
import string

passLen = input("\n\nEnter leng1th of your password: ")

lowerLetter = string.ascii_lowercase
upperLetter = string.ascii_uppercase
number = string.digits
symbols = string.punctuation

allChar = lowerLetter + upperLetter + number + symbols

password = ''.join(secrets.choice(allChar) for i in range(int(passLen)))

print("\n\nYour Password is: "+password+"\n\n")
