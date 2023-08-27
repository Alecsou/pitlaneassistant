## On suppose disposer d'une liste lst des binaires (taille 8)

## Little endian bizarre : si on a \xab \xcd et qu'on veut u16, on prends \xcd\xab et on convertit

import inspect;

def getUnsigned(lst,size):
    div = size//8
    data = lst[:div]
    data.reverse()
    res = ""
    for i in data:
        res+=i
    return lst[div::],int(res,2)

def getSigned(lst,size):
    div = size//8
    data = lst[:div]
    data.reverse()
    res = data[0][1::]
    if len(data)>1:
        for i in data[1::]:
            res+=i
    return lst[div::],pow(-1,int(data[0][0]))*(int(res,2))

    
def getFloat(lst):
    data = lst[:4]
    data.reverse()
    res = ""
    for i in data:
        res+=i
    frac = 0
    for j in range(len(res[9::])):
        frac+=int(res[j])*pow(2,-j)
    return lst[4::],pow(-1,int(res[0]))*pow(2,int(res[1:9],2)-127)*(1+frac)

def getDouble(lst):
    data = lst[:8]
    data.reverse()
    res = ""
    for i in data:
        res+=i
    frac = 0
    for j in range(len(res[12::])):
        frac+=int(res[j])*pow(2,-j)
    return lst[8::],pow(-1,int(res[0]))*pow(2,int(res[1:12],2)-127)*(1+frac)

def getChar(lst):
    data = lst[:1]
    data.reverse()
    res = ""
    for i in data:
        res+=i
    return lst[1::],chr(int(res,2))

def getStr(slf):
    s="{"
    for i in inspect.getmembers(slf):
        if not i[0].startswith('_'):
            if not inspect.ismethod(i[1]):
                if type(i[1]) is list:
                    ss = "["
                    for _ in i[1]:
                        ss+=str(_)+", "
                    ss=ss[:-2]
                    ss+="]"
                elif "classes" in str(type(i[1])):
                    ss=str(i[1])
                else:
                    ss='"'+str(i[1])+'"'
                s+='"'+str(i[0])+'"'+ " : " +ss+", "
    return s[:-2]+"}"