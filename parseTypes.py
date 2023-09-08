## On suppose disposer d'une liste lst des binaires (taille 8)

## Little endian bizarre : si on a \xab \xcd et qu'on veut u16, on prends \xcd\xab et on convertit

import inspect;
import struct;
import unidecode;

##
#   Decode an unsigend int from his data bytes form to readable int
#   @param {Array} lst Array of binary data
#   @param {Int} size Number of bytes to use (8,13 or 32)
#   @returns {Array} Array of binary data trimed from the treated data
#   @returns {Int} Treated data
##
def getUnsigned(lst,size):
    div = size//8
    data = lst[:div]
    data.reverse()
    res = ""
    for i in data:
        res+=i
    return lst[div::],int(res,2)


##
#   Decode a sigend int from his data bytes form to readable int
#   @param {Array} lst Array of binary data
#   @param {Int} size Number of bytes to use (8,13 or 32)
#   @returns {Array} Array of binary data trimed from the treated data
#   @returns {Int} Treated data
##
def getSigned(lst,size):
    div = size//8
    data = lst[:div]
    data.reverse()
    res = data[0][1::]
    if len(data)>1:
        for i in data[1::]:
            res+=i
    return lst[div::],pow(-1,int(data[0][0]))*(int(res,2))

##
#   Decode a float32 from his data bytes form to readable float
#   @param {Array} lst Array of binary data
#   @returns {Array} Array of binary data trimed from the treated data
#   @returns {Float} Treated data
##
def getFloat(lst):
    data = lst[:4]
    data.reverse()
    res = ""
    for i in data:
        res+=i
    f = int(res, 2)
    return lst[4::],round(struct.unpack('f', struct.pack('I', f))[0],3)

##
#   Decode a double64 from his data bytes form to readable float
#   @param {Array} lst Array of binary data
#   @returns {Array} Array of binary data trimed from the treated data
#   @returns {Double} Treated data
##
def getDouble(lst):
    data = lst[:8]
    data.reverse()
    res = ""
    for i in data:
        res+=i
    f = int(res, 2)
    return lst[8::],round(struct.unpack('f', struct.pack('I', f))[0],3)

##
#   Decode a char (UTF-8) from his data bytes form to readable char
#   @param {Array} lst Array of binary data
#   @returns {Array} Array of binary data trimed from the treated data
#   @returns {char} Treated data
#
#   Workaround for accents and all characters that need two bytes
#   (ex: é = \xC3 \xA9)
#   If the byte read at first is a leading bytes for a sequence, we transform the int in byte data in Python,
#   get the next byte in the data structure, and then use the decode method to transform bytearray to char
#
#   After it, we return the array of binary data trimmed by the first byte ONLY, and we replace the second byte
#   by a null byte ("OOOOOOOO")
#
##
def getChar(lst):
    data = lst[:1]
    data.reverse()
    res = ""
    for i in data:
        res+=i
    if (int(res,2)>=194) and (int(res,2)<=245):
        first = bytearray(struct.pack('B', int(res,2)))
        data = lst[:2]
        data.reverse()
        data=data[0]
        res = ""
        for i in data:
            res+=i
        first.append(bytearray(struct.pack('B', int(res,2)))[0])
        return ["00000000"]+lst[2::],first.decode("utf-8") 
    else:
        if int(res,2)==0:
            return lst[1::],""
        else :
            return lst[1::],chr(int(res,2))

##
#   Creates a string that represents a class into a readable and valid JSON
#   @param {Class} slf Class to stringify
#   @returns {String} String representing the class as a valid JSON stringified object
##
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