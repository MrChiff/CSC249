# CSC 249
# M5LAB - Hashing and Salting
# norrisa
# 3/16/23

import getpass # allows non-echo password input
import hashlib 
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

The password must be saved in hashed format
and a random "salt" is generated at registration, which is saved along with the hashed password.

"""

passwords = {}
"""
We would need to hash the default users' passwords before
the menu loads -- this is doable but would take some extra code.
So we'll start without any users.
"""

def make_hash(password, salt=""):
  """
  input: password, (optional) salt
  output: hexencoding of the has of password + salt
  """
  # add salt to password
  password += salt
  # convert string to binary data
  password = password.encode('UTF-8') # blob - binary large object
  # hash the binary data
  # possible algorithms: sha1, md5 (very broken), sha256 (ok)
  pw_hash = hashlib.sha256(password).hexdigest()

  return pw_hash

def main():
  """ entry point"""
  print("Please register an account to begin.")
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
  print("your username is", username,"with password", password)
  
  # binary encode password before hashing
  #pw_bytes = password.encode('UTF-8')
  #pw_hash = hashlib.sha256(pw_bytes).hexdigest()
  pw_hash = make_hash(password)
  print("SHA256 hash is:", pw_hash)
  if username in passwords.keys():
    # username exists, check password
    stored_hash = passwords[username]
    if pw_hash == stored_hash:
      print("password matches:", pw_hash, stored_hash)
      return username
    else:
      print("password mismatch:", pw_hash, stored_hash)
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
  print("your username is", username,"with password", password)
  
  if username in passwords.keys():
    print("ERROR: Account exists.")
    return
  print("Creating account for ", username)
  # store hash rather than password
  #pw_hash = hashlib.sha256(password.encode('UTF-8')).hexdigest()
  pw_hash = make_hash(password)
  print("SHA256 hash is:", pw_hash)
  passwords.update({username: pw_hash})


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
  print("Enter new password for",user,".")
  newpass = getpass.getpass() 
  pw_hash = make_hash(newpass)
  passwords.update({user: pw_hash})
  print("Password changed.")

if __name__ == "__main__":
  main()