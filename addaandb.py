import datetime
import time
import ctypes
def addAandB(a, b):
    a = ctypes.c_int32(a).value
    b = ctypes.c_int32(b).value
    while(b!=0):
        carry = ctypes.c_int32(a & b).value
        #print("carry is "+str(carry))
        a = ctypes.c_int32(a ^ b).value
        #print("Modified a is "+str(a))
        b = ctypes.c_int32(carry << 1).value
        #print("Modified b is "+str(b))
    return a
start = datetime.datetime.now()
print(addAandB(9998,-9999))
#time.sleep(1)
end  = datetime.datetime.now()
diff = end - start
#print(diff.total_seconds())
diff
print("My adder is taking "+ str(diff.microseconds) )
