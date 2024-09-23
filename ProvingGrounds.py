
userName = input("Please enter a username that is no more than 12 characters, has no spaces and no digits: ")

if len(userName) > 12:
    print("Username is over 12 characters.")

elif userName.count(" ") > 0:
    print("No spaces allowed.")

elif not userName.isalpha():
    print("No digits allowed.")


