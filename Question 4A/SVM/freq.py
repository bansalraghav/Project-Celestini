import numpy as np



X=[]




file1 = open("plain_intelligent2.txt","r")
file2 = open("encryptedtxtsimple_intelligent.txt","r")
file3 = open("abc.txt","r")



for i in range(0,50):
    freq=np.ones(26)
    freq2=np.ones(26)
    freq3=np.ones(26)

    for i in range(0,200):
        
        c=file1.read(1)
        if not c:
            break
        val = ord(c)-64
        if(0<val<27):
            freq[val-1]+=1
        c2=file2.read(1)
        val2 = ord(c2)-64
        if(0<val2<27):
            freq2[val2-1]+=1
        c3=file3.read(1)
        print(c3)
        val3=ord(c3)-64
        if(0<val3<27):
            freq3[val3-1]+=1
        
    print("simple",freq)
    freq=np.sort(freq)
    print(freq)

    print("encsimple",freq2)
    freq2=np.sort(freq2)
    print(freq2)
    
    print("poly",freq3)
    freq3=np.sort(freq3)
    print(freq3)

    obs=np.divide(freq2,freq)
    print(obs)
    obs1=np.divide(freq3,freq)
    print(obs1)

    X.append([np.array(obs),np.array([1,0])])
    X.append([np.array(obs1),np.array([0,1])])


             
np.save("X_neuralnetwork.npy",X)

file1.close()
file2.close()
