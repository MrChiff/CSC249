#ifndef DOUBLYLINKEDLIST_H
#define DOUBLYLINKEDLIST_H

/* 
Implementation of the doubly linked list
used by main.cpp
*/

#include <iostream>
#include "Node.h"


/*
This version uses templated Nodes, and so will work
with different data types.
Note that you still must have all Nodes within the list
using the same type of data.
*/
template <class T>
class LinkedList {
private:
   Node<T>* head;
   Node<T>* tail;
   
public:
   LinkedList() {
      head = nullptr;
      tail = nullptr;
   }
   
   virtual ~LinkedList() {
      Node<T>* currentNode = head;
      while (currentNode) {
         Node<T>* toBeDeleted = currentNode;
         currentNode = currentNode->next;
         delete toBeDeleted;
      }
   }

  Node<T>* getHead() {
    // to manually walk the list, we need a pointer to the head
    return head;
  }
    
   void Append(Node<T>* newNode) {
     // append adds a node to the end of the list
      if (head == nullptr) {
         head = newNode;
         tail = newNode;
      }
      else {
         Node<T>* old_tail = tail; // old_tail is a probe, basically
         old_tail->next = newNode; // add new tail at the end
         newNode->prev = old_tail; // new tail is after old tail
         tail = newNode;
      }
   }
   
   void Prepend(Node<T>* newNode) {
     // prepend adds a node to the beginning of the list
      if (head == nullptr) {
         head = newNode;
         tail = newNode;
      }
      else {
         Node<T>* old_head = head; // probe
         newNode->next = old_head; // old head is after new head
         old_head->prev = newNode; // new head is before old head
         head = newNode;
      }
   }
   
   void PrintList(std::ostream& printStream, const std::string& separator = ", ") {
     // walk the list, printing each item
     // this could be a single while loop, except
     // for those pesky commas (separators)
      Node<T>* node = head;
      if (node) {
          // Head node is not preceded by separator
          printStream << node->data;
          node = node->next;
      }
      while (node) {
         printStream << separator << node->data;
         node = node->next;
      }
      printStream << std::endl;
   }
  
   void InsertAfter(Node<T>* currentNode, Node<T>* newNode) {
     // given a node, add new node directly after it
      if (head == nullptr) {
         head = newNode;
         tail = newNode;
      }
      else if (currentNode == tail) {
         Node<T>* old_tail = tail;
         old_tail->next = newNode;
         newNode->prev = old_tail;
         tail = newNode;
      }
      else {
         //newNode->next = currentNode->next;
         //currentNode->next = newNode;
         // example: insert C after A in the list (A,B)
         // A = currentNode, B = successor, C = newNode
         // successor is a probe to the node after the splice point
         Node<T>* successor = currentNode->next; // successor is B
         newNode->next = successor;         // C->next = B
         newNode->prev = currentNode;   // C->prev = A
         currentNode->next = newNode;       // A->next = C
         successor->prev = newNode;         // B->prev = C
      }
   }
   

    // Doubly Linked List uses Remove, not RemoveAfter
   void Remove(Node<T>* currentNode) {
     // given a node, remove it and splice the links
     Node<T>* successor = currentNode->next;
     Node<T>* predecessor = currentNode->prev;
     /*
     Example: (A, C, B) then remove C
     A = predecessor, B = successor, C = currentNode
     */
        
     if (successor) { // if not the tail
        successor->prev = predecessor;
     }
     if (predecessor) { // if not the head
        predecessor->next = successor;
     }
     // if this node is new head or tail, update those pointers
     if (currentNode == head) {
        head = successor;
     }
     if (currentNode == tail) {
        tail = predecessor;
     }
     // dispose of C
     delete currentNode;
  }
};


#endif  
//DOUBLYLINKEDLIST_H