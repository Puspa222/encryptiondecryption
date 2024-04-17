#Encryption and decryption Of msg
import random
import string


print("\n\n\n")
str=input("Enter Your Msg to Encrypt:")


#Encryption Process

mmsg=str.split()
res1=''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase+string.digits, k=13 ))
eemsg=""
for msg in mmsg:
   if len(msg)==1:
       emsg=''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=2)) +msg+''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=3))
   if len(msg)==2:
       emsg=''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=2))+''.join(reversed(msg))+ ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=4))
   if len(msg)>2:
       emsg= ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=4))+''.join(reversed(msg[1:]))+''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=3))+msg[0:1]+''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=2))
   eemsg=eemsg+ res1 +emsg


    
print("\n\n\n Encrypted Msg:\t",eemsg)
ddmsg=input("\n\nEnter msg to Decrpty:")

#Decryption Process

ddmsg=ddmsg[13:]
ddmmsg=ddmsg.split(res1)
dstr=""
for dmsg in ddmmsg:
   if len(dmsg)==6:
       ddmmsg=dmsg[2]
   elif len(dmsg)==8:
       ddmmsg=''.join(reversed(dmsg[2:4]))
   elif len(dmsg)>8:
       dmsg=dmsg[4:len(dmsg)-2]
       ddmmsg=dmsg[len(dmsg)-1]+''.join(reversed(dmsg[:len(dmsg)-4]))
   else:
       ddmmsg=''.join(random.choices(string.digits,k=2))
   dstr=dstr+" "+ddmmsg


print("\n\n\n Decrypted Msg:\t",dstr)
