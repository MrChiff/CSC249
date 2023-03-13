#include <iostream>
// #include "SinglyLinkedList.h"
#include "DoublyLinkedList.h"
using namespace std;

/*
CSC 249
M4T2 - Singly Linked Lists (cpp)
original from zybooks 4.6
modified to use Templates as shown in Gaddis C++ ch18
(which allows for lists containing any one type of data)
Jonathan Hardwick
2023/03/09
*/

int main() {
   LinkedList<int> numList;
   Node<int>* nodeA = new Node<int>(1);
   Node<int>* nodeB = new Node<int>(2);
   Node<int>* nodeC = new Node<int>(3);
   Node<int>* nodeD = new Node<int>(4);
   Node<int>* nodeE = new Node<int>(5);
   Node<int>* nodeF = new Node<int>(6);
   ///*
   numList.Append(nodeB);   // Add 99
   numList.Append(nodeC);   // Add 44, make the tail
   numList.Append(nodeE);   // Add 42, make the tail

   numList.Prepend(nodeA);  // Add 66, make the head
   //cout << "list of abce: ";
   //numList.PrintList(cout);
   cout << "Node A: " << nodeA->data << ", Node B: " << nodeB->data << ", Node C: " << nodeC->data << ", Node D: " << nodeD->data; 
   cout << ", Node E: " << nodeE->data << ", Node F: " << nodeF->data << endl;
   cout << endl;
   

   numList.InsertAfter(nodeC, nodeD);  // Insert 95 after 44
   numList.InsertAfter(nodeE, nodeF);  // Insert 17 after tail (42)

   // Output list
   cout << "List after adding nodes D and F: ";
   numList.PrintList(cout);

   // Remove the tail node, then the head node
   numList.Remove(nodeF);
   numList.Remove(nodeA); 
   // remove 44 from the middle
   numList.Remove(nodeC);

   // Output final list
   cout << "List after removing nodes A, C, and F: ";
   numList.PrintList(cout);
  //*/

  
   // LinkedList destructor frees remaining nodes

  // example 2 - strings 
  LinkedList<string> strList;
  Node<string>* node_a = new Node<string>("apple");
  Node<string>* node_b = new Node<string>("banana");
  Node<string>* node_c = new Node<string>("cherry");
  Node<string>* node_d = new Node<string>("blueberry");
  
  cout << "\nNode A: " << node_a->data << ", Node B: " << node_b->data << ", Node C: " << node_c->data << ", Node D: " ; 
  cout << node_d->data << endl;
  cout << endl;
  
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