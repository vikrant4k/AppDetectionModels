import geopy.distance
class GeoClusterT:

    def __init__(self):
        print("Geo Cluster Initiated")

    def createCluster(self,featureDataList):
        self.clusterMap={}
        clusterIndex=0
        for i in range(0,len(featureDataList)):
            count=0;
            for j in range(0,len(featureDataList)):
                if(self.calcDistance(featureDataList[i].lat,featureDataList[i].lon,featureDataList[j].lat,featureDataList[j].lon)<25):
                    count=count+1;
            if(count>5):
                isUnique=1
                for key in self.clusterMap:
                    data=self.clusterMap[key]
                    if(self.calcDistance(featureDataList[i].lat,featureDataList[i].lon,data[0],data[1])<25):
                        isUnique=0
                        break
                if(isUnique==1):
                 self.clusterMap[str(clusterIndex)]=[featureDataList[i].lat,featureDataList[i].lon,count]
                 clusterIndex=clusterIndex+1
        print(self.clusterMap)

    def getClusterIndex(self,featureDataList):
        clusterList=[]
        for i in range(0,len(featureDataList)):
            clusterIndex=-1
            prev_distance=-1
            for key in self.clusterMap:
                data=self.clusterMap[key]
                dist=self.calcDistance(data[0],data[1],featureDataList[i].lat,featureDataList[i].lon)
                if(prev_distance==-1 and dist<25):
                    clusterIndex=int(key)
                    prev_distance=dist
                else:
                    if(dist<prev_distance):
                        clusterIndex = int(key)
                        prev_distance = dist
            clusterList.append(clusterIndex)
        print(clusterList)
        return clusterList



    def calcDistance(self,lat1,lon1,lat2,lon2):
        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)


        val=geopy.distance.vincenty(coords_1, coords_2).meters
        ##print(val)
        return val
