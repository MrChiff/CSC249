# Main program to test Binary search tree.
from Node import Node
from BinarySearchTree import BinarySearchTree

tree = BinarySearchTree()

user_values = input('Enter insert values with spaces between: ')
print()

for value in user_values.split():
    new_node = Node(int(value))
    tree.insert(new_node)

print('Initial tree:')
print(tree)
print()

remove_value = int(input('Enter value to remove: '))
print()

print('Tree after removing %d:' % remove_value)
tree.remove(remove_value)
print(tree)
