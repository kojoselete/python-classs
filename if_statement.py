# name = input ("Enter the name of the person at the door:")
# if (name == "Tiny"):
#     print(f"hello {name}")

username = input ("Please enter username")
password = input ("Please enter Password")

if username == "admin" and password == "1234@admin":
    print("Hello, you are logged in as Admin.")

else:
    print("Invalid username or password. Kindly try again")