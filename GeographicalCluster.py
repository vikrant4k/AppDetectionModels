import numpy as np
import hdbscan
from Constants import Constants
from sklearn.cluster import DBSCAN
class GeographicalCluster:

    def __init__(self):

        ms_per_radian = 6371000.0088
        epsilon = 500 / ms_per_radian
        self.clusterer = hdbscan.HDBSCAN(min_cluster_size=5, gen_min_span_tree=True,metric='haversine')



    def mainFunc(self,featureDataList):
        ##geoCluster=GeoClusterT()
        ##geoCluster.createCluster(featureDataList)
        ##predictArr=geoCluster.getClusterIndex(featureDataList)
        radianArr=self.convertDataToRadians(featureDataList)
        predictArr=self.fitData(radianArr)
        featureDataList=self.predictData(featureDataList,predictArr)
        return featureDataList


    def convertDataToRadians(self,featureDataList):
        latLongList = []
        for data in featureDataList:
            temp = []
            temp.append(data.lat)
            temp.append(data.lon)
            latLongList.append(temp)
        latLongArr=np.array(latLongList)
        radianArr=np.radians(latLongArr)
        return radianArr

    def fitData(self,radianArr):
        clusters=self.clusterer.fit_predict(radianArr)
        return clusters

    def predictData(self,featureDataList,predictArr):
        for i in range(0,len(featureDataList)):
            if(featureDataList[i].activityType==3):
                cluster=predictArr[i]
                if(cluster==-1):
                    featureDataList[i].geoCluster=Constants.GEO_UNKNOWN
                else:
                    featureDataList[i].geoCluster=cluster+2;
            else:
                featureDataList[i].geoCluster=Constants.GEO_WALKING_RUNNING_TRAVELLING
        return featureDataList

