# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import CipherC as Cipher
import textract
#check the above function
text = "CEASER cipher DEMO"
s = 4



tex =textract.process("test.docx")
tex=tex.decode("utf-8")

#Encrtypted file
encrypted=Cipher.encrypt(tex,s)
print ("\nEncrypt: \n ", encrypted,"\n")
#Decrypt file
decrypted =Cipher.decrypt(encrypted,s)
f=open("test.doc","wt")
# if(f.mode=="wt"):
#     f.write(decrypted)
#     f.close()
print ("Decrypt: \n" + Cipher.decrypt(encrypted,s))

