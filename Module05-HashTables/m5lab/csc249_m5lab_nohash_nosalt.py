# CSC 249
# M5LAB - Hashing and Salting
# norrisa
# 3/16/23

import getpass  # allows non-echo password input
#import hashlib
"""
example hashing and salting password program
The program requirements are:

    Allow a user to register an account.
        They will need to enter a username and password.
        These will be added to the password file (assuming the username is not already used).
    Allow a user to login.
        They will need to enter a username and password.
        These are checked against the values in the password file.
        TODO: (The hashed entered password is compared with the hashed stored password. If they are equal, then the user has entered the correct password.)

TODO: The password must be saved in hashed format, and a random "salt" is generated at registration, which is saved along with the hashed password.

"""

passwords = {"admin": "admin", "user": "password"}


def main():
  """ entry point"""
  menu()


def menu():
  """ main menu """
  choice = ""
  while choice != 0:
    print("Main Menu")
    print("1. Login")
    print("2. Register Account")
    print("3. Change Password")
    print("0. Exit")
    try:

      choice = int(input("> "))
      if choice == 1:
        user = login()
        if user != None:
          print("Login successful -- welcome", user)
        else:
          print("Login failed")
      elif choice == 2:
        register()
      elif choice == 3:
        change_password()
      elif choice == 0:
        print("Goodbye.")
    except ValueError:
      print("Unrecognized command.")


def login():
  """ 
  User login. They will need to enter a username and password.
  These are checked against the values in the password file.
  (The hashed entered password is compared with the hashed stored       
  password. If they are equal, then the user has entered the correct password.)
  Input: none
  Output: returns a valid username if successful login, None otherwise
  """
  username = input("Login: ")
  #password = input("password: ") # this shows the password!
  try:
    password = getpass.getpass()  # does not echo the password
  except Exception as error:
    print('ERROR', error)
    return None
  print("your username is", username, "with password", password)
  #pw_hash = hashlib.sha256(password).hexdigest()
  # binary encode password before hashing
  #print("SHA256 hash is:", pw_hash)
  if username in passwords.keys():
    # username exists, check password
    storedpass = passwords[username]
    if password == storedpass:
      print("password matches:", password, storedpass)
      return username
    else:
      print("password mismatch:", password, storedpass)
      return None


def register():
  """
  User registration. They will need to enter a username and password.
  These will be added to the password file 
  (assuming the username is not already used).
  """
  print("Creating new account.")
  username = input("Username: ")
  #password = input("password: ") # this shows the pas sword!
  try:
    password = getpass.getpass()  # does not echo the password
  except Exception as error:
    print('ERROR', error)
    return
  print("your username is", username, "with password", password)

  if username in passwords.keys():
    print("ERROR: Account exists.")
    return
  print("Creating account for ", username)
  # store hash rather than password
  #pw_hash = hashlib.sha256(password).hexdigest()
  #print("SHA256 hash is:", pw_hash)
  passwords.update({username: password})


def change_password():
  """
  First, require user to log in.
  If successful, allow them to enter new password,
  then update the stored password.
  """
  user = login()
  if user == None:
    print("Incorrect password.")
    return
  print("Enter new password for", user, ".")
  newpass = getpass.getpass()
  passwords.update({user: newpass})
  print("Password changed.")


if __name__ == "__main__":
  main()
