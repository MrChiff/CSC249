# Main program to test Binary search tree.
from Node import Node
from BinarySearchTree import BinarySearchTree

tree = BinarySearchTree()

user_values = input('Enter insert values with spaces between: ')
# user_values = "15 8 72 13 1 0 45 38 42"
print()

for value in user_values.split():
    new_node = Node(int(value))
    tree.insert(new_node)

print('Initial tree:')
print(tree)
print()

# Removing a node.
remove_value = int(input('Enter value to remove: '))
# remove_value = 13
print()

print('Tree after removing %d:' % remove_value)
tree.remove(remove_value)
print(tree)

# Insert a node. Must send a Node object to the insert method instead of a number.
insert_value = int(input("Enter a value to insert into the tree: "))
# insert_value = 36
print()

print("Tree after inserting %d: " % insert_value)
tree.insert(Node(insert_value))
print(tree)

# Search for a number.
search_value = int(input("Enter a value to look for in the BST: "))
# search_value = 45
print()

if tree.search(search_value):
    print("The node exists in the tree.\n")
    
else:
    print("Value not found.\n")
    
search_value = int(input("Enter a value to look for in the BST: "))
# search_value = 94
print()

if tree.search(search_value):
    print("The node exists in the tree.")
    
else:
    print("Value not found.")

