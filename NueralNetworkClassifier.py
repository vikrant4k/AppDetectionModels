from sklearn.neural_network import MLPClassifier
from SaveModels import SaveModels
import numpy as np
class NueralNetworkClassifier:

    def __init__(self,key):
        model = SaveModels.readModel(key, "nueral")
        if (model is not None):
            print("File Model Used")
            self.clf = model
        else:
            print("New Model Created")
            self.clf=MLPClassifier((300,300,400,600,900,600,300,100,50,25),learning_rate='adaptive',max_iter=1000,verbose=True,tol=0.00001)

    def train(self,userData,output):
        print("Nueral Fitting started ")
        self.clf.fit(userData,output)

    def saveModel(self,key):
        SaveModels.saveModel(key,self.clf,"nueral")

    def predict(self,userData):
        userData=np.reshape(userData,(1,-1))
        return self.clf.predict(userData)

    def predictProbability(self,userData):
        userData = np.reshape(userData, (1, -1))
        probability=self.clf.predict_proba(userData)
        probability=np.reshape(probability,(probability.shape[1]))
        ##probability=probability.tolist()
        ##print(probability)
        problList=[]
        for i in range(0,len(probability)):
            temp=[]
            temp.append(probability[i])
            temp.append(i)
            problList.append(temp)
        ##print(problList)
        for i in range(0,len(problList)):
            for j in range(i+1,len(problList)):
                if(problList[i][0]<problList[j][0]):
                    temp=problList[i]
                    problList[i]=problList[j]
                    problList[j]=temp
        indexs=[]
        for i in range(0,4):
            indexs.append(problList[i][1])
        return indexs

