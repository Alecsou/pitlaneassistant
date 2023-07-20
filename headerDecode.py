import parseTypes as pt
import classes.headerClass as header

def headerDecode(msg) :
    data=[0 for _ in range(0,12)]
    msg,data[0]=pt.getUnsigned(msg,16)
    msg,data[1]=pt.getUnsigned(msg,8)
    msg,data[2]=pt.getUnsigned(msg,8)
    msg,data[3]=pt.getUnsigned(msg,8)
    msg,data[4]=pt.getUnsigned(msg,8)
    msg,data[5]=pt.getUnsigned(msg,8)
    msg,data[6]=pt.getUnsigned(msg,64)
    msg,data[7]=pt.getFloat(msg)
    msg,data[8]=pt.getUnsigned(msg,32)
    msg,data[9]=pt.getUnsigned(msg,32)
    msg,data[10]=pt.getUnsigned(msg,8)
    msg,data[11]=pt.getUnsigned(msg,8)
    return msg,header.Header(data)
    

