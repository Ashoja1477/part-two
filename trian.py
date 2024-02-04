from micromlgen import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris
iris  = load_iris()
x = iris.data
y = iris.target
t_0 = iris.target[0]
model = SVC(kernel='linear',gamma=0.001)
model.fit(x,y)
train  = model.predict([[4.9, 2.4, 3.3, 1.5]])
print("data_model",iris)
print("y :",)
if train==t_0:
    print("gooding train...")
    print("")
    import time 
    time.sleep(0.5)
    print("good nice")
else:
    print("training not good pleas check data_train or try again")