#ifndef SINGLYLINKEDLIST_H
#define SINGLYLINKEDLIST_H

/* 
Implementation of the singly linked list
used by main.cpp
*/

#include <iostream>

class Node { 
public:
	Data data; // what is Data class?... its the right data
	// imagine Data as a polymorphic variable which contains 
	// any type you want it to container
	Node* next;

   Node(int initialData) {
      data = initialData;
      next = nullptr;
   }
};

class IntNode {
public:
   int data;
   Node* next;

   Node(int initialData) {
      data = initialData;
      next = nullptr;
   }
};

class StringNode {
public:
   int data;
   Node* next;

   Node(int initialData) {
      data = initialData;
      next = nullptr;
   }
};

class LinkedList {
private:
   Node* head;
   Node* tail;
   
public:
   LinkedList() {
      head = nullptr;
      tail = nullptr;
   }
   
   virtual ~LinkedList() {
      Node* currentNode = head;
      while (currentNode) {
         Node* toBeDeleted = currentNode;
         currentNode = currentNode->next;
         delete toBeDeleted;
      }
   }
    
   void Append(Node* newNode) {
      if (head == nullptr) {
         head = newNode;
         tail = newNode;
      }
      else {
         tail->next = newNode;
         tail = newNode;
      }
   }
   
   void Prepend(Node* newNode) {
      if (head == nullptr) {
         head = newNode;
         tail = newNode;
      }
      else {
         newNode->next = head;
         head = newNode;
      }
   }
   
   void PrintList(std::ostream& printStream, const std::string& separator = ", ") {
      // node here is the "probe" variable
      Node* node = head;
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

   
   void InsertAfter(Node* currentNode, Node* newNode) {
      if (head == nullptr) {
         head = newNode;
         tail = newNode;
      }
      else if (currentNode == tail) {
         tail->next = newNode;
         tail = newNode;
      }
      else {
         newNode->next = currentNode->next;
         currentNode->next = newNode;
      }
   }
   
   void RemoveAfter(Node* currentNode) {
      if (currentNode == nullptr && head) {
         // Special case: remove head
         Node* nodeBeingRemoved = head;
         head = head->next;
         delete nodeBeingRemoved;
         
         if (head == nullptr) {
             // Last item was removed
             tail = nullptr;
         }
      }
      else if (currentNode->next) {
         Node* nodeBeingRemoved = currentNode->next;
         Node* succeedingNode = currentNode->next->next;
         currentNode->next = succeedingNode;
         delete nodeBeingRemoved;
         if (succeedingNode == nullptr) {
            // Remove tail
            tail = currentNode;
         }
      }
   }
};

#endif