#ifndef LOGIN_APP_H
#define LOGIN_APP_H

#include <map> 
using namespace std;
/*
LoginApp - contains all the actual program logic
(main still contains the basic UI)

This is a simple demo of separating UI from business logic
(Note we don't include iostream -- we can't use cin or cout here.)
*/

// User struct
struct User {
  string username;
  string password;
};

// LoginApp object, used to store:
// - all necessary data
// - all functions needed
class LoginApp {
  public:
    LoginApp();
    ~LoginApp();
    void menu();      // entry point to app

  private:
    // member variables
    map <string, User> user_map;
    // member functions
    User login();    
    User register_account();    // register is a reserved word in c++
    User change_password(User acct, string new_password);
    // unimplemented
    // void save_data();
    // void load_data();

};

LoginApp::LoginApp() {
  
}

LoginApp::~LoginApp() {
  
}

#endif // LOGIN_APP_H