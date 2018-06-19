from ConvertData import ConvertData
from GeographicalCluster import GeographicalCluster
from LauncherCapture import LauncherCapture
from IllumPreProcess import Illuminace
from TimeClassifier import TimeClassifier
class PreProcessData:

    def __init__(self):
        print("Pre Process Intialized ")

    def mainFunc(self):
        convertData=ConvertData()
        userObjMap=convertData.mainFunc()
        for key in userObjMap:
            geoCluster = GeographicalCluster()
            featureDataList=userObjMap[key]
            featureDataList=LauncherCapture().removeLauncher(featureDataList)
            featureDataList=Illuminace().normalizeIlluminace(featureDataList)
            featureDataList=self.fillInMissingValue(featureDataList)
            featureDataList=geoCluster.mainFunc(featureDataList)
            featureDataList=TimeClassifier().convertTimeToQuarters(featureDataList)
            userObjMap[key]=featureDataList
        return userObjMap





    def fillInMissingValue(self,userDataList):
        for i in range(0,len(userDataList)):
            if(userDataList[i].lat==0.0):
                closestIndex=self.findClosestLatLong(userDataList,i)
                userDataList[i].lat=userDataList[closestIndex].lat
                userDataList[i].lon=userDataList[closestIndex].lon
            if(userDataList[i].illuminance==0.0):
                closestIndex=self.findClosestIlluminance(userDataList,i)
                userDataList[i].illuminance=userDataList[closestIndex].illuminance
        return userDataList


    def findClosestLatLong(self,userDataList,index):
        prev_index=-1
        next_index=-1
        for i in range(index,0,-1):
            if(userDataList[i].lat!=0.0):
                prev_index=i
                break;
        for i in range(index,len(userDataList)):
            if (userDataList[i].lat != 0.0):
                next_index = i
                break;
        if(prev_index==-1):
            return next_index
        if(next_index==-1):
            return prev_index;
        diff=index-prev_index
        diff_1=next_index-index;
        if(diff_1<diff):
            return next_index
        else:
            return prev_index

    def findClosestIlluminance(self,userDataList,index):
        prev_index = -1
        next_index = -1
        for i in range(index, 0, -1):
            if (userDataList[i].illuminance != 0.0):
                prev_index = i
                break;
        for i in range(index, len(userDataList)):
            if (userDataList[i].illuminance != 0.0):
                next_index = i
                break;
        if (prev_index == -1):
            return next_index
        if (next_index == -1):
            return prev_index;
        diff = index - prev_index
        diff_1 = next_index - index;
        if (diff_1 < diff):
            return next_index
        else:
            return prev_index





##pr=PreProcessData()
##pr.mainFunc()



