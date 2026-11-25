username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Welcome")
elif username == "admin":
    print("Wrong password")
else:
    print("Unknown user")
