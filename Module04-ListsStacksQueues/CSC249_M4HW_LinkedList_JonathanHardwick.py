# This file exstablishes the Node Class and the Linked List Class for python.

#===========#
class Node: #
#===========#

    """
    This class creates a Node of any type. 
    """

    def __init__(self, item="", price=0, quant=0):
        self.item = item
        self.price = price
        self.quant = quant
        self.next = None
        self.prev = None
        # print(initial_data)
        # print(self.data)
        
    def __str__(self):
        return f'{self.item:<16}{self.price:<16}{self.quant:<16}'

#===============#
class LinkedList:
#===============#

    """
    This class creates and modifies a linked list of Nodes.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        
    #----------------------------------------------------------
    def append(self, new_node):
    
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    #----------------------------------------------------------    
    def prepend(self, new_node):
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    #----------------------------------------------------------
    def insert_after(self, current_node, new_node):
        
        # if no items are in the list:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if the current node is the tail (insert before tail)
        elif current_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        else:
            successor_node = current_node.next
            new_node.next = successor_node
            new_node.prev = current_node
            current_node.next = new_node
            successor_node.prev = new_node
            
    #----------------------------------------------------------
    def remove(self, current_node):
        
        successor_node = current_node.next
        predecessor_node = current_node.prev
    
        # if the node being removed is not the tail:
        if successor_node is not None:
            successor_node.prev = predecessor_node
        # if the node being removed is not the head:
        if predecessor_node is not None:
            predecessor_node.next = successor_node
        # if the head is being removed:
        if current_node is self.head:
            self.head = successor_node
        # if the tail is being removed:
        if current_node is self.tail:
            self.tail = predecessor_node
            
    #----------------------------------------------------------
    def ListSearch(self, key):
        
        current_node = self.head # start at head
        
        while (current_node != None): 
            if (current_node.item == key): 
                return current_node
            # print(current_node)
            current_node = current_node.next
            
        return None
    #----------------------------------------------------------
    def inventoryValue(self):
        
        current_node = self.head 
        total = 0
        while (current_node != None): 
            total += (current_node.price * current_node.quant)
            current_node = current_node.next
            
        return total
    
    #----------------------------------------------------------
    def __repr__(self):
        
        current_node = self.head 
        print("-"*48)
        print(f'{"ITEM:":<16}{"PRICE:":<16}{"QUANTITY:":<16}')
        print(f'{"-----":<16}{"------":<16}{"---------":<16}')
        while (current_node != None): 
            print(current_node)
            current_node = current_node.next
            
        return "-"*48 + "\n"
        
        

