
import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "chatting-system-8351b-default-rtdb.firebaseapp.com",
  "databaseURL": "https://chatting-system-8351b-default-rtdb.firebaseio.com",
  "storageBucket": "chatting-system-8351b-default-rtdb.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

def enroll():
    
    C = input("Enter your username/loginID:")
    e = input("Enter your password:")
    f = input("Confirm your password:")
    if C == e:
             print("Password and username cannot be same:")
             e = input("Enter your password:")
             f = input("Confirm your password:")
    if len(e) != 4 and len(f) != 4: 
             print("Password must be of 4 characters")
             e = input("Enter your password:")
             f = input("Confirm your password:")
    else:
             print(e)
    if e == f:
             print("Password confirmed")        
    else:
            print("Password does not matched..")
           
    while(1):
        g = {C:int(e)}
        db.child("Messaging").child("User Data").update(g)




def auth():
                       
         while(1):
             print("Enter your username:")
             usem = input()

             u = db.child("Messaging/User Data/input()").get()
             print(u.key())
             print(list(u.val()))
             
             
             if user_name in (list(u.key())):
                  print("Enter your password:")
                  passw = int(input())
                  if passw == (u.val()):
                      print("Login Done..")
             else:
                  print("User does not exist")
                  print("Do you want to sign up? Press 1 if 'Yes'")
                  d = int(input())
                  if d == 1:
                      enroll()
             

while(1):
    dict = {}
    n = 10
    while(1):
        print("Press 1 for Enrollment:")
        print("Press 2 for Authentication:")
        a = int(input("Enter the mode:"))
        if a!=1 and a!=2:
          print("Wrong selection!!! \n Press either 1 or 2")
        if(a == 1):
             enroll()     
        elif(a == 2):
            auth()




