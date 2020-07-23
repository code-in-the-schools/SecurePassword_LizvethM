specialChara=('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=','+','=','[', ']','{', '}')
#Whether password if valid
valid = False
#While Loop
while valid == False:
#Loops until password is 8-16 chara at least one lowercase, one uppercase
  password = str(input("Enter Valid Password: "))

#Reviewing if password is valid
  if(len(password) < 8 or len(password) > 16):
    print("Please enter a password with 8 to 16 characters. ")
#Checking for special chara
  for  i in range(len(password)):
    if(len(password)!= specialChara):
      print("Please enter a password with at least one special character.")
  

  
