import time
t = list(map(int, time.strftime("%H:%M:%S", time.localtime()).split(":")))
import pywhatkit
 
# 8902686826 7063990059
# using Exception Handling to avoid unexpected errors
try:
     # sending message in Whatsapp in India so using Indian dial code (+91)
     pywhatkit.sendwhatmsg("+91 9XXXXXXXXX", f"Hi, [This is an automated message. Automated at - {t[0]}:{t[1]}:{t[2]}]", t[0], t[1]+1)
 
     print("Message Sent!") #Prints success message in console
 
     # error message
except: 
     print("Error in sending the message")