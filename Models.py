from ModelCreateVector import ModelCreateVector
import numpy as np
from SvmClassifier import SVMClassifier
class Models:

    def __init__(self):
        print("Model Data Initilized")

    def prepareData(self):
        self.createVector = ModelCreateVector()
        self.userDataVector, self.modelAggData = self.createVector.mainFunc()

    def getModelToBeUsed(self,key):
        svm=SVMClassifier(key)
        return svm

    def trainModel(self):

        for key in self.userDataVector:
            modelVectorData=self.userDataVector[key]
            userAppsList = self.modelAggData.userApps[key]
            print(userAppsList)
            print(len(userAppsList))
            ##print(modelVectorData.predict)
            inputDataArr=np.array(modelVectorData.inputData)
            predictArr=np.array(modelVectorData.predict)
            print(len(predictArr))

            svm=self.getModelToBeUsed(key)
            svm.train(inputDataArr,predictArr)
            svm.saveModel(key)
            print("Classification for user "+key+" done")

    def predictData(self):

        for key in self.userDataVector:
            svm=self.getModelToBeUsed(key)
            modelVectorData=self.userDataVector[key]
            userAppsList = self.modelAggData.userApps[key]
            ##print(modelVectorData.predict)
            inputDataArr=np.array(modelVectorData.inputData)
            predictArr=np.array(modelVectorData.predict)
            count=0
            for i in range(0,len(inputDataArr)):
                ##index=self.svm.predict(inputDataArr[i])
                indexs=svm.predictProbability(inputDataArr[i])
                orIndex=modelVectorData.predict[i]
                appName=userAppsList[orIndex]
                appsPredicted=[]
                for index in indexs:
                    appsPredicted.append(userAppsList[index])
                if(appName in appsPredicted):
                    count=count+1

                print(userAppsList[orIndex]+" "+userAppsList[indexs[0]])
            print(count)

            print("Classification for user "+key+" done")


m=Models()
m.prepareData()
##m.trainModel()
m.predictData()