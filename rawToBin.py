
##
#   Transform a bytearray in an array of binary bytes
#   @param {Bytearray} data Bytearray of raw data coming from the UDP reciever
#   @returns {Array} Array of binary data
##
def rawToBin(data):
    l=[]
    for i in list(data):
        l+=[bin(i)[2::].zfill(8)]
    return l