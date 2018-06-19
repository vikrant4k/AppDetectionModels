from ModelCreateData import ModelCreateData
from ModelAggData import ModelVectorData
class ModelCreateVector:

    def __init__(self):
        print("Model Create Vector Initiated")

    def mainFunc(self):
        modelCreateData=ModelCreateData()
        modelAggData=modelCreateData.mainFunc()
        userDataTrainVector,userDataTestVector=self.convertDataIntoVector(modelAggData)
        return userDataTrainVector,userDataTestVector,modelAggData

    def convertDataIntoVector(self,modelAggData):
        userDataTrainVector={}
        userDataTestVector={}
        userObjMap=modelAggData.userObjMap
        for key in userObjMap:
            timeList=modelAggData.userTimeCluster[key]
            userAppsList = modelAggData.userApps[key]
            activityList = modelAggData.activityMap[key]
            userGeoList = modelAggData.userGeoMap[key]
            userAudioList=modelAggData.userAudioCluster[key]
            featureDataList=userObjMap[key]
            userHotTrainVector=[]
            userAppTrainUsed=[]
            userHotTestVector = []
            userAppTestUsed = []
            for data in featureDataList:
                vectorData=[]
                vectorData=self.createVectorForList(data.timeCluster,timeList,vectorData)
                vectorData=self.createVectorForList(data.activityType,activityList,vectorData)
                vectorData=self.createVectorForList(data.geoCluster,userGeoList,vectorData)
                vectorData=self.createVectorForList(data.audio,userAudioList,vectorData)
                vectorData.append(data.bluetooth)
                vectorData.append(data.wifi)
                vectorData.append(data.illuminance)
                vectorData.append(data.weekday)
                vectorData.append(data.charging)
                if(data.dataType=="train"):
                    userAppTrainUsed.append(userAppsList.index(data.appName))
                    userHotTrainVector.append(vectorData)
                    userDataTrainVector[key]=ModelVectorData(userHotTrainVector,userAppTrainUsed)
                else:
                    userAppTestUsed.append(userAppsList.index(data.appName))
                    userHotTestVector.append(vectorData)
                    userDataTestVector[key] = ModelVectorData(userHotTestVector, userAppTestUsed)
        return userDataTrainVector,userDataTestVector



    def createVectorForList(self,element,lis,dataList):
        index=lis.index(element)
        for i in range(0,len(lis)):
            if(i==index):
                dataList.append(1)
            else:
                dataList.append(0)
        return dataList



##ModelCreateVector().mainFunc()

