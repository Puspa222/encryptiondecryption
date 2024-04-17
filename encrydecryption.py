#Encryption and decryption Of msg
import random
import string
print("\n\n\n")
msg=input("Enter Your Msg to Encrypt:")
res1 = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=2))
res2= ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=3))
res3 = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=4))
if len(msg)==1:
    emsg=res1 +msg+res2
if len(msg)==2:
    emsg=res1+''.join(reversed(msg))+res3
if len(msg)>2:
    emsg=res3+''.join(reversed(msg[1:]))+res2+msg[0:1]+res1
print(emsg)

dmsg=input("Enter msg to Decrpty:")
ddmsg=dmsg
if len(dmsg)==6:
    ddmsg=dmsg[2]
if len(dmsg)==8:
    ddmsg=''.join(reversed(dmsg[2:4]))
if len(dmsg)>8:
    dmsg=dmsg[4:len(dmsg)-2]
    ddmsg=dmsg[len(dmsg)-1]+''.join(reversed(dmsg[:len(dmsg)-4]))
else:
    ddmsg=''.join(random.choices(string.digits,k=2))
print(ddmsg)
