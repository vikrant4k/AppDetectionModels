from ReadFiles import ReadFiles
from FeatureData import FeatureData
class ConvertData:

    def __init__(self):
        print("Convert Data Inititated");

    def mainFunc(self):
        userDataMap=self.readFiles();
        userObjMap=self.convertDataToObj(userDataMap);
        return userObjMap


    def readFiles(self):
        re=ReadFiles()
        userDataMap=re.readFolder(["/home/vik1/Downloads/data/vikrant/"])
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
                    if(featureData.convertTimeToDay(dataArr[0])=="15"):
                        featureData.dataType="test"
                    userObjList.append(featureData)
            userObjMap[key]=userObjList
        return userObjMap




