from xgboost import XGBClassifier
import numpy as np
from SaveModels import SaveModels
from xgboost import plot_importance
from matplotlib import pyplot
from ModelCreateVector import ModelCreateVector
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import matplotlib.mlab as mlab
class XGBoostClassifier:

    def __init__(self,key):
        plotly.tools.set_credentials_file(username='vikrant4.k', api_key='8QCFmtXowusykGuksRkZ')
        model=SaveModels.readModel(key,"xgboost")
        if(model is not None):
            print("File Model Used")
            self.clf=model
        else:
            print("New Model Created")
            self.clf = XGBClassifier(learning_rate=0.09,n_estimators=200,max_depth=7,n_jobs=4)

    def train(self,userData,output,userAppList):
        print("XGBOsst Fitting started ")
        self.clf.fit(userData,output)
        ##self.showFeatureImportanceWithName(userAppList)
        ##print(self.clf.feature_importances_)

    def showFeatureImportanceWithName(self,userAppList):
        lis=[]
        print(len(self.clf.feature_importances_))
        for i in range(0,len(self.clf.feature_importances_)):
            temp=[]
            temp.append(i)
            temp.append(self.clf.feature_importances_[i])
            lis.append(temp)
        for i in range(0,len(lis)):
            for j in range(i+1,len(lis)):
                if(lis[i][1]<lis[j][1]):
                    temp=lis[i]
                    lis[i]=lis[j]
                    lis[j]=temp

        for data in lis:
            key=str(data[0])
            imp=str(data[1])
            name=ModelCreateVector.hotVectorMap[key]
            if("lastused" in name):
               name=name.split("_")
               print(name[1])
               nu=name[0]+"_"+userAppList[int(name[1])]
               print(nu+" "+imp)
            else:
                print(name+" "+imp)
        ##self.createHistogram()

    def createHistogram(self):
        print(self.clf.feature_importances_)


    def saveModel(self,key):
        SaveModels.saveModel(key,self.clf,"xgboost")

    def deleteModel(self,key):
        SaveModels.deleteModel(key,"xgboost")

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





