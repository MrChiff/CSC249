class Node:
    # Constructor assigns the given key, with left and right
    # children assigned with None.
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None
        
    def __repr__(self):
        print("Node: " + str(self.key))
        print("Left child: " + str(self.left))
        print("Right child: " + str(self.right))
    