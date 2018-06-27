from ReadFiles import ReadFiles
from FeatureData import FeatureData
class ConvertData:
    testDate="18"



    def mainFunc(self):
        userDataMap=self.readFiles();
        userObjMap=self.convertDataToObj(userDataMap);
        return userObjMap


    def readFiles(self):
        re=ReadFiles()
        userDataMap=re.readFolder(["/home/vik1/Downloads/data/navpreet/"])
        return userDataMap

    def convertDataToObj(self,userDataMap):
        userObjMap={}
        for key in userDataMap:
            userObjList=[]
            userDataList=userDataMap[key]
            for userData in userDataList:
                for data in userData:
                    dataArr=data.split(",");
                    featureData=FeatureData(dataArr[0],dataArr[1],dataArr[2],dataArr[3],dataArr[4],dataArr[5],dataArr[6],dataArr[7],dataArr[8],dataArr[9],dataArr[10])
                    time=featureData.convertTimeToDay(dataArr[0])
                    if(time==ConvertData.testDate):
                        featureData.dataType="test"
                    userObjList.append(featureData)
            for i in range(0,len(userObjList)):
                for j in range(i+1,len(userObjList)):
                    if((userObjList[i]).timeIni>(userObjList[j]).timeIni):
                        temp=userObjList[i]
                        userObjList[i]=userObjList[j]
                        userObjList[j]=temp
            for i in range(0, len(userObjList)):
                if(i!=0):
                    val=userObjList[i].timeIni-userObjList[i-1].timeIni
                    val=val/1000;
                    val=val/60;

            userObjMap[key]=userObjList
        return userObjMap




