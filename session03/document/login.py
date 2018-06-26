import getpass
username = input("User Name:")
if username == "Maiphuong":
    password = getpass.getpass()
    if password == "1809":
        print ("Welcome MP")
    else:
        print ("Incorrect password")
else:
    print ("You are not the user")