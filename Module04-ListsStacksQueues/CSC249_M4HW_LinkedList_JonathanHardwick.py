# This file exstablishes the Node Class and the Linked List Class for python.

#=========#
class Node:
#=========#

    """
    This class creates a Node of any type. 
    """

    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

#===============#
class LinkedList:
#===============#

    """
    This class creates and modifies a linked list of Nodes.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
    
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def prepend(self, new_node):
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_after(self, current_node, new_node):
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node
    
    def remove_after(self, current_node):
    
        # Special case, remove head
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node  
            if succeeding_node == None: # Remove last item
                self.tail = None
        elif current_node.next != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None: # Remove tail
                self.tail = current_node
                
    # ListSearch(list, key):
    #     current_node = list⇢head 
    #     while (current_node != None): 
    #         if (current_node⇢data == key): 
    #             return current_node
      
    #         current_node = curNode⇢next
   
    #     return null
    
    def ListSearch(self, key):
        current_node = self.head 
        while (current_node != None): 
            if (current_node.data == key): 
                return current_node
      
            current_node = current_node.next
   
        return None
