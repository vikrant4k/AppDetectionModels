import datetime
class FeatureData:

    def __init__(self,timestamp,appName,activityType,lat,lon,bluetooth,audio,wifi,illuminance,weekday,charging):
        self.timestamp=self.convertUnixTimestamp(timestamp);
        self.appName=appName;
        self.lat=float(lat);
        self.lon=float(lon);
        self.bluetooth=int(bluetooth);
        self.audio=int(audio);
        self.wifi=self.convertWifiValue(wifi);
        self.illuminance=float(illuminance);
        self.weekday=int(weekday);
        self.charging=int(charging)

    def convertUnixTimestamp(self,java_time_millis):
        ds = datetime.datetime.fromtimestamp(
            int(str(java_time_millis)[:10])) if java_time_millis else None
        ds = ds.replace(hour=ds.hour, minute=ds.minute, second=ds.second,
                        microsecond=int(str(java_time_millis)[10:]) * 1000)
        ds=ds.strftime("%H:%M")
        return ds

    def convertWifiValue(self,wifi):
        if(wifi=="true"):
            return 1
        else:
            return 0

