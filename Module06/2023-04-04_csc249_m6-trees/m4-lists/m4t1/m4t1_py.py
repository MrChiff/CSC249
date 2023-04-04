"""
CSC 249
M4T1 - simple linked list (singly linked)
norrisa
2/28/23
"""

""" 
LinkedList consists of:
// node and pointer collection of Node objects
// pointer to head and tail
// methods to access and mutate the list
Notes: 
Copilot has gotten stupider -- it was of zero help here.
Examples from  Lambert, Fundamentals of Data Structures in Python
"""



class Node:
    """ Represents a singly linked node"""
    # constructors in python use the form __init__
    def __init__(self, data=None, next=None):
        """ Instantiates a Node with None as default next """
        self.data = data
        self.next = next
    
    # str method provides a string conversion (ex. for print)
    def __str__(self):
        #return("[data=" + self.data + " | next ]")
        # nodes contain data and next
        data_string = str(self.data)
        next_string = str(self.next) 
        return "[" + data_string + " | " + next_string + "]" 
    
        
class LinkedList:
    def __init__(self):
        """ Instantiates an empty linkedlist"""
        self.head = None   # pointer to head
        self.tail = None   # pointer to tail
        
# end of class definitions        
def main():
    # add five nodes at the head
    head = None
    
    for count in range(1, 6):
        head = Node(count, head)
    # print contents
    probe = head
    while probe != None:
        print(probe.data)
        probe = probe.next
    
    
# run program
if __name__ == "__main__":
    main()

# We've turned off main, so running this .py file
# simply provides a "sandbox" of objects and methods.
# some examples
"""
nullptr = None          # example of an empty link (not a node at all)
node1 = Node(None, None) # an empty Node
node2 = Node("A", None) # data plus an empty link
node3 = Node("B", node2) # data plus a link to node2
print(nullptr)
print(node1)
print(node2)
print(node3)
"""

