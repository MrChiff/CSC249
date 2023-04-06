#include <iostream>
#include "SinglyLinkedList.h"
using namespace std;

/*
CSC 249
M4T2 - Singly Linked Lists (cpp)
original from zybooks 4.6
modified to use Templates as shown in Gaddis C++ ch18
(which allows for lists containing any one type of data)
your name
today's date
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

   // TODO: finish adding template to insertafter/removeafter
   //numList.InsertAfter(nodeC, nodeD);  // Insert 95 after 44
   //numList.InsertAfter(nodeE, nodeF);  // Insert 17 after tail (42)

   // Output list
   cout << "List after adding nodes: ";
   numList.PrintList(cout);

   // Remove the tail node, then the head node
   //numList.RemoveAfter(nodeE);
   //numList.RemoveAfter(nullptr);

   // Output final list
   cout << "List after removing nodes: ";
   numList.PrintList(cout);
  //*/

  
   // LinkedList destructor frees remaining nodes

  // example 2 - strings 
  LinkedList<string> strList;
  Node<string>* node_a = new Node<string>("a");
  Node<string>* node_b = new Node<string>("b");
  strList.Append(node_a);
  strList.Append(node_b);
  cout << "list of two string nodes:";
  strList.PrintList(cout);
  
}