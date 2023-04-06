#include <iostream>
// #include "SinglyLinkedList.h"
#include "DoublyLinkedList.h"
using namespace std;

/*
CSC 249
M4LAB1 - Linked Lists of records (CPP)
modified from m4lab2
modified to use Templates as shown in Gaddis C++ ch18
(which allows for lists containing any one type of data)
your name
today's date
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


*/

int main() {
   LinkedList<int> numList;
   Node<int>* nodeA = new Node<int>(66);
   Node<int>* nodeB = new Node<int>(99);
   Node<int>* nodeC = new Node<int>(44);
   Node<int>* nodeD = new Node<int>(95);
   Node<int>* nodeE = new Node<int>(42);
   Node<int>* nodeF = new Node<int>(17);
   ///*
   numList.Append(nodeB);   // Add 99
   numList.Append(nodeC);   // Add 44, make the tail
   numList.Append(nodeE);   // Add 42, make the tail

   numList.Prepend(nodeA);  // Add 66, make the head
   cout << "list of abce: ";
  numList.PrintList(cout);

   numList.InsertAfter(nodeC, nodeD);  // Insert 95 after 44
   numList.InsertAfter(nodeE, nodeF);  // Insert 17 after tail (42)

   // Output list
   cout << "List after adding nodes: ";
   numList.PrintList(cout);

   // Remove the tail node, then the head node
   numList.Remove(nodeF);
   numList.Remove(nodeA); 
   // remove 44 from the middle
   numList.Remove(nodeC);

   // Output final list
   cout << "List after removing nodes: ";
   numList.PrintList(cout);
  //*/

  
   // LinkedList destructor frees remaining nodes

  // example 2 - strings 
  LinkedList<string> strList;
  Node<string>* node_a = new Node<string>("a");
  Node<string>* node_b = new Node<string>("b");
  Node<string>* node_c = new Node<string>("c");
  Node<string>* node_d = new Node<string>("d");
  strList.Append(node_a);
  strList.Append(node_b);
  cout << "list of two string nodes: ";
  strList.PrintList(cout);

  strList.InsertAfter(node_a, node_c);
  cout << "then adding c after a and d after b: ";
  strList.InsertAfter(node_b, node_d);
  strList.PrintList(cout);
  cout << "then remove node c: ";
  strList.Remove(node_c);
  strList.PrintList(cout);
  
}