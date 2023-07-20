def rawToBin(data):
    l=[]
    for i in list(data):
        l+=[bin(i)[2::].zfill(8)]
    return l