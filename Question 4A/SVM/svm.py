import numpy as np
from sklearn import preprocessing, cross_validation, neighbors,svm

X=np.load("X_intelligent.npy")
X_test=np.load("X_test.npy")
np.random.shuffle(X)

train=X
test=X_test

x=np.array([i[0] for i in train])
y=[i[1] for i in train]

test_x=np.array([i[0] for i in test])
test_y=[i[1] for i in test]

x= np.array(x)
#x=preprocessing.scale(x)
y=np.array(y)
print(x.shape)
print(y.shape)
y = np.ravel(y)

test_x= np.array(test_x)
#test_x=preprocessing.scale(test_x)
test_y=np.array(test_y)
print(test_x.shape)
print(test_y.shape)
test_y = np.ravel(test_y)


clf =  svm.SVC()

clf.fit(x,y)
confidence = clf.score(test_x,test_y)
print(confidence)






