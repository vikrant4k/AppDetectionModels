class LauncherCapture:

    launcherList=["Samsung Experience Home","Finder","System UI","Package installer","Device maintenance","Android System","CaptivePortalLogin","SecurityLogAgent","Pixel Launcher","AppDetection","Settings","Huawei startside"
                  ,"Nova Launcher","Sys.gr.snitt","Android-system","Samsung Pay","Lenovo Launcher"];

    def removeLauncher(self,featureDataList):
        newFeatureDataList=[]
        for data in featureDataList:
            if(data.appName not in LauncherCapture.launcherList):
                if(data.appName=="Contacts"):
                    data.appName="Phone"
                newFeatureDataList.append(data)
        return newFeatureDataList

