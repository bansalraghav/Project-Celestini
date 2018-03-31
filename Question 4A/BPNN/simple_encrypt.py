file2 = open("encryptedtxtsimple_intelligent.txt","w")
file1 = open("plain_intelligent2.txt","r")

key=['H','K','J','X','U','B','F','S','O','N','M','Y','T','E','C','Z','W','P','L','D','A','V','I','Q','R','G']

while True:
    
    c=file1.read(1)
    if not c:
        print("end of file")
        break
    val=ord(c)-64
    print(val)
    
    if(0<val<27):
        print(key[val-1])
        enc=key[val-1]
        file2.write(enc)
    elif(val==-32):
        file2.write(' ')
    
