import pywhatkit
 
# using Exception Handling to avoid
# unprecedented errors
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+91 XXXXXXXXXX", "This is an automated message",1,58,10)
  print("Successfully Sent!") # xxx are the phone number part
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")