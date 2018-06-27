from ModelCreateData import ModelCreateData
from ModelAggData import ModelVectorData
class ModelCreateVector:
    hotVectorMap={}
    prevLength=0


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
            index=0
            for data in featureDataList:
                vectorData=[]
                vectorData=self.createVectorForList(data.timeCluster,timeList,vectorData)
                self.setNamingMap(vectorData,"time")
                vectorData=self.createVectorForList(data.activityType,activityList,vectorData)
                self.setNamingMap(vectorData, "activity")
                vectorData=self.createVectorForList(data.geoCluster,userGeoList,vectorData)
                self.setNamingMap(vectorData, "geo")
                vectorData=self.createVectorForList(data.audio,userAudioList,vectorData)
                self.setNamingMap(vectorData, "audio")
                vectorData=self.createVectorForApps(featureDataList,userAppsList,index,vectorData)
                self.setNamingMap(vectorData, "apps")
                ##vectorData=self.isItNewSession(featureDataList,index,vectorData)
                vectorData=self.timeSinceLastUsed(featureDataList,index,vectorData,userAppsList)
                self.setNamingMap(vectorData, "lastused")
                vectorData.append(data.bluetooth)
                self.setNamingMap(vectorData, "bluetooth")
                vectorData.append(data.wifi)
                self.setNamingMap(vectorData, "wifi")
                vectorData.append(data.illuminance)
                self.setNamingMap(vectorData, "illuminance")
                vectorData.append(data.weekday)
                self.setNamingMap(vectorData, "weekday")
                vectorData.append(data.charging)
                self.setNamingMap(vectorData, "charging")
                if(data.dataType=="train"):
                    userAppTrainUsed.append(userAppsList.index(data.appName))
                    userHotTrainVector.append(vectorData)
                    userDataTrainVector[key]=ModelVectorData(userHotTrainVector,userAppTrainUsed)
                else:
                    userAppTestUsed.append(userAppsList.index(data.appName))
                    userHotTestVector.append(vectorData)
                    userDataTestVector[key] = ModelVectorData(userHotTestVector, userAppTestUsed)
                index=index+1
        print(ModelCreateVector.hotVectorMap)
        return userDataTrainVector,userDataTestVector

    def setNamingMap(self,vectorData,name):
        count=1;
        for i in range(ModelCreateVector.prevLength,len(vectorData)):
            ModelCreateVector.hotVectorMap[str(i)]=name+"_"+str(count)
            count=count+1
        ModelCreateVector.prevLength=len(vectorData)

    def timeSinceLastUsed(self,featureDataList,index,vectorData,userAppList):
        mapApp={}
        for data in userAppList:
            mapApp[data]=0
        for i in range(0,index):
            appName=featureDataList[i].appName
            timeIni=featureDataList[i].timeIni
            mapApp[appName]=timeIni
        if(index>0):
            currentTimeIni=featureDataList[index].timeIni
        else:
            currentTimeIni=0
        for key in mapApp:
            val=(currentTimeIni-mapApp[key])/60000;
            vectorData.append(val)
        return vectorData





    def isItNewSession(self,featureDataList,index,vectorData):
        if(index>0):
            timeIni=featureDataList[index].timeIni
            prevTime=featureDataList[index-1].timeIni
            if(((timeIni-prevTime)/60000)>10):
                vectorData.append(1)
            else:
                vectorData.append(0)
        else:
            vectorData.append(1)
        return vectorData



    def createVectorForApps(self,feautreDataList,userAppsList,index,dataVector):
        if(index==0):
            for i in range(0,len(userAppsList)):
                dataVector.append(0)
            return  dataVector
        if(index==1):

            dataVector=self.createVectorForList(feautreDataList[index-1].appName,userAppsList,dataVector)
            return dataVector
        else:
            indexs=[]
            indexs.append(userAppsList.index(feautreDataList[index - 1].appName))
            indexs.append(userAppsList.index(feautreDataList[index - 2].appName))
            for i in range(0, len(userAppsList)):
                if (i in indexs):
                    dataVector.append(1)
                else:
                    dataVector.append(0)
            return dataVector



    def createVectorForList(self,element,lis,dataList):

        index=lis.index(element)
        for i in range(0,len(lis)):
            if(i==index):
                dataList.append(1)
            else:
                dataList.append(0)
        return dataList



##ModelCreateVector().mainFunc()

