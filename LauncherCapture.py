class LauncherCapture:

    launcherList=["Samsung Experience Home","Finder","System UI","Package installer","Device maintenance","Android System","CaptivePortalLogin","SecurityLogAgent" ]

    def removeLauncher(self,featureDataList):
        newFeatureDataList=[]
        for data in featureDataList:
            if(data.appName not in LauncherCapture.launcherList):
                newFeatureDataList.append(data)
        return newFeatureDataList

