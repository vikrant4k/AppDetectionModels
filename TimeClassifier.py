import numpy as np
from sklearn.cluster import DBSCAN
class TimeClassifier:


    def convertTimeToQuarters(self,featureDataList):
        """
        timeCluster=self.clusterUsingdbscan(featureDataList)
        for i in range(0,len(featureDataList)):
            featureDataList[i].timeCluster=timeCluster[i]+1;
        """
        for data in featureDataList:
            time=data.timestamp
            time=int(time)
            data.timeCluster=self.findCluster(time)
        return featureDataList

    def clusterUsingdbscan(self,featureDataList):
        timeList=[]
        for data in featureDataList:
            timeList.append(data.timestamp)
        timeArr=np.array(timeList)
        timeArr=timeArr.reshape((len(timeArr),1))
        self.db=DBSCAN(min_samples=20,eps=0.3)
        timeCluster=self.db.fit_predict(timeArr)
        timeCluster=timeCluster.tolist()
        return timeCluster




    def findCluster(self,time):

        if (time >= 6 and time < 9):
            return 1;
        if (time >= 9 and time < 12):
            return 2
        if (time >= 12 and time < 14):
            return 3
        if (time >= 14 and time < 17):
            return 4
        if (time >= 17 and time < 19):
            return 5
        if (time >= 19 and time < 22):
            return 6
        if (time >= 22):
            return 7
        return 8



