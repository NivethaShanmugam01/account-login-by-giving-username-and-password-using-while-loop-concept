user="nivetha"
pw="shivan123"
i=0
while i<3:
  i=i+1
  user_name=input("enter the user name: ")
  if (user==user_name):
    password=input("enter your password : ")
    if (pw==password):
      print("login sucess")
      break
    else:
      print("incorrect password")
  else:
    print("invalid username")
