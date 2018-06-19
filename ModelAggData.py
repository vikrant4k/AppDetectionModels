class ModelAggData:

    def __init__(self,userObjMap,userApps,activityMap,userGeoMap,userTimeCluster,userAudioCluster):
        self.userObjMap=userObjMap
        self.userApps=userApps
        self.activityMap=activityMap
        self.userGeoMap=userGeoMap
        self.userTimeCluster=userTimeCluster
        self.userAudioCluster=userAudioCluster

class ModelVectorData:

    def __init__(self,inputData,predict):
        self.inputData=inputData
        self.predict=predict



