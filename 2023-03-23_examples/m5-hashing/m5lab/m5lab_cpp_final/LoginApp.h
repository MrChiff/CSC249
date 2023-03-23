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
    // member functions
    User login(string name, string password);
    User register_account(string name, string password);    // register is a reserved word in c++
    User change_password(User acct, string new_password);   // can only change password of a
    // unimplemented
    // void save_data();
    // void load_data();
                                                                // valid (logged in) user
  private:
    // member variables
    map <string, User> user_map;



};

LoginApp::LoginApp() {
    // start with one demo user
    User demo = User();
    demo.username = "demo";
    demo.password = "demo";
    // store demo user in map
    user_map.emplace(demo.username, demo); // could also use insert
}

LoginApp::~LoginApp() {

}

User LoginApp::login(string name, string password) {
    // input: name, password
    // output: User object (empty if login failed)
    User u = User(); // potential user
    if (name == "demo" && password == "demo") {
        // key exists, retrieve User and check password
        // (using dummy for now)
        u.username = name;
        u.password = password;
        return u;
    }
    else {
        // user not found
        return u; // return dummy user
    }
}

#endif // LOGIN_APP_H
