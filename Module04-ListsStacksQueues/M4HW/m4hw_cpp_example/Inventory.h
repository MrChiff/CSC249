#ifndef INVENTORY_H
#define INVENTORY_H

#include <iostream>
#include <string>
using namespace std;
/*
Inventory class - based on the linked list data structure
Inventories can do the following:
- list their contents (which are Product objects)
- retrieve a product by name
- add a product to their contents
- remove a product from their contents

Handling quantities (which are always "one" for now" in Product 
is left to the developer.)

*/

class Product {
public:
   string name;
   double price;

   Product* next;
   Product* previous;

   Product(string prod_name, double prod_price) {
      name = prod_name;
      price = prod_price;
      next = nullptr;
      previous = nullptr;
   }
};

class Inventory {
private:
   Product* head;
   Product* tail;

public:
   string list_name;
   Inventory() {
      list_name = "";
      head = nullptr;
      tail = nullptr;
   }

   Inventory(string inv_name) {
       list_name = inv_name;
       head = nullptr;
       tail = nullptr;
   }
   
   virtual ~Inventory() {
      Product* currentNode = head;
      while (currentNode) {
         Product* toBeDeleted = currentNode;
         currentNode = currentNode->next;
         delete toBeDeleted;
      }
   }
    
   void Add(Product* newNode) {
      if (head == nullptr) {
         head = newNode;
         tail = newNode;
      }
      else {
         tail->next = newNode;
         newNode->previous = tail;
         tail = newNode;
      }
   }

  void AddCopy(Product* old_product) {
    // first make a deep copy of old_product
    // then add the new copy to the list
    Product* new_product = new Product( old_product->name,
                                        old_product->price);
    Add(new_product);
    
  }

  Product* FindByName(string product_name) {
    // traverse the list until you find a product
    // with the chosen name
    // return nullptr if it is not found
    Product* probe  = head;
    while (probe != nullptr) {
      string probe_name = probe->name;
      cout << "comparing " << probe_name << " with " << product_name << endl;
      if (product_name == probe_name) {
        cout << "match!" << endl;
        return probe;
      }
      probe = probe->next; 
    }
    // not found
    cout << "didn't find " << product_name << endl;
    return nullptr;
  }
   
   void PrintContents(std::ostream& printStream, const std::string& separator = ", ") {
      Product* probe = head;
      // Show name of inventory, then contents
      cout << list_name << " contains: "<< endl;
      // if no contents, say so
      if (probe == nullptr) {
        cout << "\tNothing";
      }
      while (probe != nullptr) {
         printStream << "\tProduct: ";
         printStream << probe->name << " ($" << probe->price << ")";
         printStream << std::endl;
         probe = probe->next;
        
      }
      printStream << endl;
   }

   
   void Remove(Product* currentNode) {
      Product* successor = currentNode->next;
      Product* predecessor = currentNode->previous;
      
      if (successor) {
         successor->previous = predecessor;
      }
      if (predecessor) {
         predecessor->next = successor;
      }
         
      if (currentNode == head) {
         head = successor;
      }
      if (currentNode == tail) {
         tail = predecessor;
      }
      
      delete currentNode;
   }
};

#endif // INVENTORY_H