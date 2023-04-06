#ifndef NODE_H
#define NODE

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

// a Node class defined to hold integers
/*
class Node {
public:
   int data;
   Node* next;

   Node(int initialData) {
      data = initialData;
      next = nullptr;
   }
};
*/

// a Node class defined to hold strings
/*
class Node {
public:
   int data;
   Node* next;

   Node(int initialData) {
      data = initialData;
      next = nullptr;
   }
};
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
#endif // NODE_H