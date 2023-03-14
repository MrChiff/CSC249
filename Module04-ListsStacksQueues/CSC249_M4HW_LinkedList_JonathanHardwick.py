# This file exstablishes the Node Class and the Linked List Class for python.

#=========#
class Node:
#=========#

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
        # return f'{self.data:<16}{self.next:<16}'
        return f'{self.item:<16}{self.price:<16}{self.quant:<16}'
        # print(self.data)

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
            new_node.prev = self.tail
            self.tail = new_node
        
    def prepend(self, new_node):
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_after(self, current_node, new_node):
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
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
    
    def remove(self, current_node):
        
        successor_node = current_node.next
        predecessor_node = current_node.prev
    
        if successor_node is not None:
            successor_node.prev = predecessor_node
    
        if predecessor_node is not None:
            predecessor_node.next = successor_node
    
        if current_node is self.head:
            self.head = successor_node
    
        if current_node is self.tail:
            self.tail = predecessor_node
    
    def ListSearch(self, key):
        
        current_node = self.head # start at head
        
        while (current_node != None): 
            if (current_node.item == key): 
                return current_node
            # print(current_node)
            current_node = current_node.next
            
        return None
    
    def inventoryValue(self):
        
        current_node = self.head 
        total = 0
        while (current_node != None): 
            total += (current_node.price * current_node.quant)
            current_node = current_node.next
            
        return total
    
    def __repr__(self):
        
        current_node = self.head 
        print("-"*48 + "\n")
        print(f'{"ITEM:":<16}{"PRICE:":<16}{"QUANTITY:":<16}')
        print(f'{"-----":<16}{"------":<16}{"---------":<16}')
        while (current_node != None): 
            print(f'{current_node.item:<16}{current_node.price:<16}{current_node.quant:<16}')
            current_node = current_node.next
            # if (current_node.next == None):
            #     break
        if (current_node == None):
            return "-"*48 + "\n"
        
        

