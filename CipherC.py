import hashlib
from cryptography.fernet import Fernet

letterPL = [260, 262, 280, 321, 323, 211, 246, 377, 379, 261, 263, 281, 322, 324, 243, 347, 378, 380,
            164,143,168,157,227,224,151,141,189,165,134,169,136,228,162,152,171,190]

def EncryptFile(choosenAlgorithm, text, pattern):
    if(choosenAlgorithm=='Cesar'):
        return encrypt(text,pattern)



def EncryptSHA(text,key):
    f = Fernet(key)
    token = f.encrypt(text)
    return token

def DecryptSHA(text,key):

    f = Fernet(key)
    return f.decrypt(text)
def encrypt(text, s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            sign = ord(char)
            if (48 > sign > 31):
                result += chr(sign + 4)
            elif (sign == 10):
                result += chr(252)
            elif (sign > 122):
                for k in letterPL:
                    if (sign == k):
                        result += chr(k)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def decrypt(text, s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            sign = ord(char)
            if (sign < 65):
                result += chr(sign - 4)
            elif (sign == 252):
                result += '\n'
            elif (sign > 200):
                for k in letterPL:
                    if (k == sign):
                        result += chr(k)
            else:
                result += chr((ord(char) - s - 97) % 26 + 97)
    return result
