class Illuminace:

    def normalizeIlluminace(self,featureDataList):
        max_illuminance=0;
        for data in featureDataList:
            if(data.illuminance>max_illuminance):
                max_illuminance=data.illuminance
        for data in featureDataList:
            data.illuminance=data.illuminance/max_illuminance;
        return featureDataList


