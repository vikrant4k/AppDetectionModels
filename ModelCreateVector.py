from ModelCreateData import ModelCreateData
from ModelAggData import ModelVectorData
class ModelCreateVector:

    def __init__(self):
        print("Model Create Vector Initiated")

    def mainFunc(self):
        modelCreateData=ModelCreateData()
        modelAggData=modelCreateData.mainFunc()
        userDataVector=self.convertDataIntoVector(modelAggData)
        return userDataVector,modelAggData

    def convertDataIntoVector(self,modelAggData):
        userDataVector={}
        userObjMap=modelAggData.userObjMap
        for key in userObjMap:
            timeList=modelAggData.userTimeCluster[key]
            userAppsList = modelAggData.userApps[key]
            activityList = modelAggData.activityMap[key]
            userGeoList = modelAggData.userGeoMap[key]
            userAudioList=modelAggData.userAudioCluster[key]
            featureDataList=userObjMap[key]
            userHotVector=[]
            userAppUsed=[]
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
                userAppUsed.append(userAppsList.index(data.appName))
                userHotVector.append(vectorData)
            userDataVector[key]=ModelVectorData(userHotVector,userAppUsed)
        return userDataVector



    def createVectorForList(self,element,lis,dataList):
        index=lis.index(element)
        for i in range(0,len(lis)):
            if(i==index):
                dataList.append(1)
            else:
                dataList.append(0)
        return dataList



##ModelCreateVector().mainFunc()

