#ifndef NODE_H
#define NODE_H

#include <string>
using namespace std;
/* 
Implementation of the Node class
used by linked lists
v2 (3.9.23 - modified to use doubly linked lists)

first pass of using different data types in nodes 
would be to define different Node classes, based on 
what data they hold (IntNode, StringNode, etc.)

The problem here is that LinkedList is defined to work
on Node objects, so now you need IntLinkedList, StringLinkedList,
etc. This isn't easily scalable.

*/


/*
A more workable option is to use the C++ concept
of templates. 
*/


template <class T>
class Node {
  public:
    T data;
    Node<T>* prev;
    Node<T>* next;

    Node(T initialData) {
      data = initialData;
      prev = nullptr;
      next = nullptr;
    }
};

class Item {
  // an inventory item in the shop
  // contains product name and price
  public:
    string name;
    double price;

  // default constructor
  Item() {
    name = "default";
    price = 0.0;
  }

  // constructor using user-supplied values
  Item(string item_name, double item_price) {
     name = item_name;
     price = item_price;
  }

  void print(std::ostream& printStream) {
    printStream << name << " " << price << endl;
  }

  // overload << so we can cout these objects
  // (this should be double checked)
  ostream& operator<<(ostream& os)
  {
      os << name << " " << price;
      return os;
  }

};

#endif // NODE_H