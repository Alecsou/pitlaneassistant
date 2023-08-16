import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class WeatherForecastSample:
    def __init__(self,data):
        self.sessionType = data[0]
        self.timeOffset = data[1]
        self.weather = data[2]
        self.trackTemperature = data[3]
        self.trackTemperatureChange = data[4]
        self.airTemperature = data[5]
        self.airTemperatureChange = data[6]
        self.rainPercentage = data[7]
    
    def __str__(self):
        s="{"
        for i in inspect.getmembers(self):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]):
                    if type(i[1]) is list:
                        ss = "["
                        for _ in i[1]:
                            ss+=str(_)+", "
                        ss+="]"
                    else:
                        ss=str(i[1])
                    s+=str(i[0])+ " : " +ss+", "
        return s+"}"

def decode(data):
    packet=[]
    tmp = 0
    for _ in range(3):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    for _ in range(4):
        data,tmp = pt.getSigned(data,8)
        packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    return data,WeatherForecastSample(packet)    