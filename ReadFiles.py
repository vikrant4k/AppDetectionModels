import glob

class ReadFiles:


    def readFile(self,filename):
        userDayData=[]
        file = open(filename, 'r');
        for line in file:
            userDayData.append(line)
        return userDayData;

    def readFolder(self,folderPaths):
        mapData={}
        for folderPath in folderPaths:
            fileNames=glob.glob(folderPath+"/*.csv");
            userData=[]
            for fileName in fileNames:
                userData.append(self.readFile(fileName))
            mapData[folderPath]=userData;
        return mapData


