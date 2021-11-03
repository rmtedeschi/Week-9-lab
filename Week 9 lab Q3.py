def _encrypt(message):
    for i in range(len(message)):
        print(chr(ord(message[i])+5), end = '')
    print('\n')
     

def _decrypt(message):
    for i in range(len(message)):
        print(chr(ord(message[i])-5), end = '')  
    print('\n')

_encrypt("hello world")
_decrypt("mjqqt|twqi")