from ModelCreateVector import ModelCreateVector
import numpy as np
from SvmClassifier import SVMClassifier
from XGBoostClassifier import XGBoostClassifier
from NueralNetworkClassifier import NueralNetworkClassifier
from BaggingClassifier import BaggingClassifier
from LatentFeatures import LatentFeatures
import operator
from ConvertData import ConvertData
from statistics import mean
class Models:

    def __init__(self):

        self.latent=LatentFeatures()

    def prepareData(self):
        self.createVector = ModelCreateVector()
        self.userDataTrainVector, self.userDataTestVector,self.modelAggData = self.createVector.mainFunc()

    def getModelToBeUsed(self,key):
        ##model=SVMClassifier(key)
        model=XGBoostClassifier(key)
        ##model=NueralNetworkClassifier(key)
        ##model=BaggingClassifier(key)
        return model

    def trainModel(self):
        for key in self.userDataTrainVector:
            modelVectorData=self.userDataTrainVector[key]
            userAppsList = self.modelAggData.userApps[key]
            print(userAppsList)
            print(len(userAppsList))
            ##print(modelVectorData.predict)
            inputDataArr=np.array(modelVectorData.inputData)
            predictArr=np.array(modelVectorData.predict)
            print(len(predictArr))

            self.getTopUsedApps(userAppsList,modelVectorData.predict)
            ##self.latent.fitData(pcaData)
            ##inputDataArr=self.latent.transformData(inputDataArr)
            svm=self.getModelToBeUsed(key)
            svm.train(inputDataArr,predictArr,userAppsList)
            svm.saveModel(key)
            print("Classification for user "+key+" done")

    def predictData(self):
        frequentApps=["WhatsApp","Phone","Chrome","Instagram","Maps"]
        for key in self.userDataTestVector:
            svm=self.getModelToBeUsed(key)
            modelVectorData=self.userDataTestVector[key]
            userAppsList = self.modelAggData.userApps[key]
            print(len(userAppsList))
            ##print(modelVectorData.predict)
            inputDataArr=np.array(modelVectorData.inputData)
            predictArr=np.array(modelVectorData.predict)
            ##inputDataArr = self.latent.transformData(inputDataArr)
            count=0
            totalCount=0
            freCount=0
            for i in range(0,len(inputDataArr)):
                totalCount=totalCount+1
                ##index=self.svm.predict(inputDataArr[i])
                indexs=svm.predictProbability(inputDataArr[i])
                orIndex=modelVectorData.predict[i]
                appName=userAppsList[orIndex]
                appsPredicted=[]
                for index in indexs:
                    appsPredicted.append(userAppsList[index])
                if(appName in frequentApps):
                    freCount=freCount+1
                if(appName in appsPredicted):
                    count=count+1
                    ##print("hit")
                else:
                    a=1
                    ##print("miss")

                ##print(userAppsList[orIndex]+" "+userAppsList[indexs[0]]+" "+userAppsList[indexs[1]]+" "+userAppsList[indexs[2]]+" "+userAppsList[indexs[3]])
            value=(count/totalCount)*100
            val1=(freCount/totalCount)*100
            svm.deleteModel(key)
            print("Classification for user "+key+" done")
            return value,val1


    def getTopUsedApps(self,userAppList,predictArr):
        mapApp={}
        for i in range(0,len(predictArr)):
            index=predictArr[i]
            appName=userAppList[index]
            if(appName in mapApp):
                val=mapApp[appName]
                mapApp[appName]=val+1
            else:
                mapApp[appName]=1
        sorted_d = sorted(mapApp.items(), key=operator.itemgetter(1))
        print(sorted_d)

lis=[]
lis1=[]
for i in range(12,22):
    if(i is not 11):
        print(i)
        ConvertData.testDate=str(i)
        m=Models()
        m.prepareData()
        m.trainModel()
        val,val1=m.predictData()
        if(val is not None):

          lis.append(val)
          lis1.append(val1)
    ##lis.append(m.predictData())
print(lis)
print(mean(lis))
print(lis1)
print(mean(lis1))