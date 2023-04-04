#include <iostream>
#include <map> 
#include "LoginApp.h"
using namespace std;

/*
csc 249
m5lab

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


NOTE ON STRUCTURE:
In this version, we have separated the UI from the Logic of 
the program. Functions like "login_ui" only do print and input
as needed, and the actual computation is done by LoginApp.
*/



// function definitions
void menu_ui(LoginApp* app);
void login_ui(LoginApp* app);
void register_ui(LoginApp* app);
void change_password_ui(LoginApp* app);

int main() {
  // start program
  // create LoginApp object
  LoginApp* app = new LoginApp();
  menu_ui(app);

  // relinquish memory when finished
  delete app;
  
}
void menu_ui(LoginApp* app) {

  
  // main menu UI
  int choice;
  do {
    cout << "Main Menu" << endl;
    cout << "1. Login" << endl;
    cout << "2. Register" << endl;
    cout << "3. Change password" << endl;
    cout << "0. Exit" << endl;
    cin >> choice;
    switch (choice) {
      case 1:
        login_ui(app);
        break;
      case 2:
        register_ui(app);
        break;
      case 3:
        change_password_ui(app);
        break;
      case 0:
        cout << "Ending program" << endl;
        break;
      default:
        cout << "ERROR: Unrecognized command." << endl;
    }
  } while (choice != 0);
  // non-numeric entries are recognized as zero
  cout << "Goodbye.";
  
}

// Function definitions for UI
void login_ui(LoginApp* app) {
  
}
void register_ui(LoginApp* app) {
  
}
void change_password_ui(LoginApp* app) {
  
}
