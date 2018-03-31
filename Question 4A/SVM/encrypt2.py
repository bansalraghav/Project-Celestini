

file2 = open("encryted_vigenere.txt","w")
file1 = open("plain_intelligent2.txt","r")
i=1
columnno=0
while True:
 
    c=file1.read(1)
    if not c:
        print("end of file")
        break
   

    char=ord(c)-64
    if(char==-32):
        enc=' '

    elif(0<char<27):
        columnno=char
        r=i%3
        if r==1:
            row=11
        if r==2:
            row=5
        if r==0:
            row=25
        i+=1
        

        print("rowno",row,"columnno",columnno)
        value=row+columnno
        value=value%26
        if value==0:
            value=26
        value=value+64
        print("value",value)

        enc=chr(value)
    file2.write(enc)
file1.close()   
file2.close()


