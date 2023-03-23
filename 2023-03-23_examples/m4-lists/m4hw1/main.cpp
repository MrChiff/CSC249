#include <iostream>
#include "Inventory.h"
using namespace std;

/*
CSC 249 
M4HW1 - Store Inventory (planning phase)
norrisa
3/16/23

One way to build M4HW is to start from the lab, and add
features. Another would be to lay out the specific 
requirements (user stories), and build from scratch.
In this project I'll do the latter.

User story structure:
As a customer, I want to <X> so that I can shop for items.
In a larger program, the "As a..." and the "so that I can..." 
items may differ, as programs have multiple users and they 
have multiple goals. For this, all these stories are for the shopper.

I want to...(Iteration 1: Bronze)
- List the shop inventory
-   List my shopping cart contents
- Add items from the shop to my cart
(Iteration 2: Silver)
- Remove items from my cart
(Iteration 3: Gold)
- [I won't phrase this as user stories, but for Gold we have
  to properly handle quantities of items. For now we'll leave
  quantity at one in all cases.]
*/
// Global variables (which make me nervous)
//Inventory* store;
//Inventory* cart;
// the alternative is to pass store and cart into every 
// method that need to use them -- safe, but tedious

// Remember, as we add multiple methods we need both the
// declaration at the top of the file, and the definition
// somewhere later on. If these are in a header, we can just
// define them.

void menu(Inventory* store, Inventory* cart);             // print main menu
void list_contents(Inventory* inv);     // List contents of an inventory
void buy(Inventory* store, Inventory* cart); 
// TODO:  remove, etc.

void menu(Inventory* store, Inventory* cart) {
  // TODO, error checking, etc.
  const int LARGEST_MENU_ITEM = 3;
  int choice = -1;
  while (choice != 0) {
      cout << "Main Menu" << endl;
      cout << "1. List store contents" << endl;
      cout << "2. List cart contents" << endl;
      cout << "3. Buy product from store" << endl;
      cout << "0. Quit" << endl;

      cin >> choice;

      if (choice == 0) {
        cout << "Goodbye" << endl;
        return; // we're done
      }
      else if (choice == 1) {
        list_contents(store);
      }
      else if (choice == 2) {
        list_contents(cart);
      }
      else if (choice == 3) {
        buy(store, cart);
      }
      else {
        cout << "Command not recognized" << endl;
      }
  }  
}

void list_contents(Inventory* inv) {
  // List contents of an inventory
  inv->PrintContents(cout);
}    

void buy(Inventory* store, Inventory* cart) {
  // First, find the item in the store by name
  cout << "Enter product name: ";
  string order_name;
  cin >> order_name;
  Product* order = store->FindByName(order_name);

  // If it exists, 
  if (order != nullptr) {
    // add a copy of it to the cart
    cart->AddCopy(order);
  }
  else {
    cout << "Product not found." << endl;
  }
  
}

int main() {
  cout << "Shopping Cart Application" << endl;

  // create a product (Node)
  Product* prod_apple = new Product("apple", 0.25);
  //cout << prod_apple->name << " " << prod_apple->price << endl;
  Product* prod_banana = new Product("banana", 0.99);

  // Create a store inventory
  Inventory* store = new Inventory("Store");
  //store.PrintContents(cout);

  store->Add(prod_apple);
  store->Add(prod_banana);
  //store->PrintContents(cout);

  //store.Remove(prod_apple);
  //store.PrintContents(cout);

  // Create customer's cart
  Inventory* cart = new Inventory("Cart");
  // DEEP COPY -- we can't just add the same pointer
  // we must create a full copy of the object

  //Product* new_apple = new Product(prod_apple->name, prod_apple->price);
  /* above is equivalent to:
  Product* new_apple = new Product("blah", 0.0);
  new_apple->name = prod_apple->name;
  new_apple->price = prod_apple->price;
  */
  //cart.Add(new_apple);
  // the above is replaced with: 
  //cart->AddCopy(prod_apple);

  //store->PrintContents(cout);
  //cart->PrintContents(cout);

  // PART 2 -- the menu
  // we pass pointers to both lists through our code
  menu(store, cart);

  // we must delete shop and cart here
  
}