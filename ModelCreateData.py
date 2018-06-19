from PreprocessData import PreProcessData
from ModelAggData import ModelAggData
class ModelCreateData:

    def __init__(self):
        print("Model Preprocessing Initiated")
        self.preprocess=PreProcessData()

    def mainFunc(self):
        userObjMap=self.preprocess.mainFunc()
        userApps=self.findUniqueApps(userObjMap)
        activityMap=self.findUniqueActivity(userObjMap)
        userGeoMap=self.findUniqueGeoCluster(userObjMap)
        userTimeCluster=self.findUniqueTimeQuarters(userObjMap)
        userAudioCluster=self.findUniqueAudioDevices(userObjMap)
        modelAggData=ModelAggData(userObjMap,userApps,activityMap,userGeoMap,userTimeCluster,userAudioCluster)
        return modelAggData



    def findUniqueApps(self,userObjMap):
        userApps = {}
        for key in userObjMap:
            featureDataList=userObjMap[key]
            userApps[key]=[]
            for data in featureDataList:
                if(data.appName not in userApps[key]):
                    (userApps[key]).append(data.appName)
        return userApps;

    def findUniqueActivity(self,userObjMap):
        userActivity={}
        for key in userObjMap:
            featureDataList = userObjMap[key]
            userActivity[key] = []
            for data in featureDataList:
                if (data.activityType not in userActivity[key]):
                    (userActivity[key]).append(data.activityType)
        return userActivity;

    def findUniqueGeoCluster(self,userObjMap):
        userGeoCluster={}
        for key in userObjMap:
            featureDataList = userObjMap[key]
            userGeoCluster[key] = []
            for data in featureDataList:
                if (data.geoCluster not in userGeoCluster[key]):
                    (userGeoCluster[key]).append(data.geoCluster)
        return userGeoCluster

    def findUniqueTimeQuarters(self,userObjMap):
        userTimeCluster = {}
        for key in userObjMap:
            featureDataList = userObjMap[key]
            userTimeCluster[key] = []
            for data in featureDataList:
                if (data.timeCluster not in userTimeCluster[key]):
                    (userTimeCluster[key]).append(data.timeCluster)
        return userTimeCluster

    def findUniqueAudioDevices(self,userObjMap):
        userAudioCluster = {}
        for key in userObjMap:
            featureDataList = userObjMap[key]
            userAudioCluster[key] = []
            for data in featureDataList:
                if (data.audio not in userAudioCluster[key]):
                    (userAudioCluster[key]).append(data.audio)
        return userAudioCluster


##ModelCreateData().mainFunc()