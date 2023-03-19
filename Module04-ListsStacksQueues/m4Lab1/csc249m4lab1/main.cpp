#include <iostream>

#include "DoublyLinkedList.h"
#include "Node.h"
using namespace std;

/*
CSC 249
M4LAB1 - Linked Lists of records (CPP)
modified from m4lab2
modified to use Templates as shown in Gaddis C++ ch18
(which allows for lists containing any one type of data)
Jonathan Hardwick
2023/03/14
*/

/*
TODO 3/14/23:
- create Item class
- template nodes to contain Item objects (or just modify Node to only take Item objects)
- follow instructions from m4lab1:
We'll create a record type Item, as in "an item in a store". Items contain a name (string) and a value (numeric, int or floating point).
We'll then create a list of 3-5 Item records. (You can use singly linked lists for this.)
Then manipulate the list as follows:

    Print the list
    Remove the second item from the list.
    Add an item to the end of the list.
    Print the list again.
TODO for HW: while we don't need it for this assignment,
being able to find a node which contains specific data
is needed for the homework.

*/

void print_items(LinkedList<Item> list) {
  // print the contents of any Item list
  // TODO: segfault from scope errors
  cout << endl << "printing store items: " << endl;
  Node<Item>* probe = list.getHead();
  while (probe != nullptr) {
    Item current_item = probe->data;
    current_item.print(cout);
    probe = probe->next;
  }
  cout << endl;
}

int main() {

  // create a new item
  Item item_a = Item("apple", 0.25);
  Item item_b = Item("banana", 0.99);
  Item item_c = Item("carrot", 0.50);
  Item item_d = Item("durian", 5.99);
  //cout << item_a.name << " " << item_a.price << endl;
  //item_a.print(cout);

  // create nodes for these items
  Node<Item>* node_a = new Node<Item>(item_a);
  Node<Item>* node_b = new Node<Item>(item_b);
  Node<Item>* node_c = new Node<Item>(item_c);

  LinkedList<Item> store = LinkedList<Item>();

  store.Append(node_a);
  store.Append(node_b);
  store.Append(node_c);

  // Task 1: print the list
  //store.PrintList(cout); // requires some hacking, let's do it directly
  //print_items(store);
  cout << endl << "printing store items: " << endl;
  Node<Item>* probe = store.getHead();
  while (probe != nullptr) {
    Item current_item = probe->data;
    current_item.print(cout);
    probe = probe->next;
  }
  cout << endl;

  // Task 2: remove the second item
  probe = store.getHead();
  probe = probe->next; // now pointing to second item
  store.Remove(probe);
  /*
  alternately:
  while probe->data.name != "banana" , probe = probe->next
  or look for item with price 0.99
  */

  // Task 3: add a fourth item
  // add durian to our store inventory
  Node<Item>* node_d = new Node<Item>(item_d);
  store.Append(node_d);

  //print_items(store);
  cout << endl << "printing store items: " << endl;
  //Node<Item>* probe = store.getHead();
  probe = store.getHead();
  while (probe != nullptr) {
    Item current_item = probe->data;
    current_item.print(cout);
    probe = probe->next;
  }
  cout << endl;



}
