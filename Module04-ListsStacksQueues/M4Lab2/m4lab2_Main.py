# CSC 249 Module 4 CH 4
# Jonathan Hardwick
# 2023/03/19

# M4LAB2 - Stacks and Queues

# Part 1: Stack ADT
# Implement the code from 4.22 for Stack in your preferred language.

# Part 2: Queue ADT
# Implement the code from 4.22 for Queue in your preferred language

# For both parts, create and manipulate data as listed in the main file.

def main():
    
    from m4lab2_Stack import Stack
    from m4lab2_Queue import Queue
    
    # Stack operations
    num_stack = Stack()
    num_stack.push(45)
    num_stack.push(56)
    num_stack.push(11)
    
    # Output stack
    print('Stack after push:', end=' ')
    node = num_stack.list.head
    while node != None:
       print(node.data, end=' ')
       node = node.next
    print()
    
    # Pop 11
    popped_item = num_stack.pop()
    print('Popped:', popped_item)
    
    # Output final stack
    print('Stack after pop:', end=' ')
    node = num_stack.list.head
    while node != None:
       print(node.data, end=' ')
       node = node.next
    print('\n')
    
    
    # Queue operations
    num_queue = Queue()
    num_queue.enqueue(17)
    num_queue.enqueue(24)
    num_queue.enqueue(18)
    
    # Output queue
    print('Queue after enqueue:', end=' ')
    node = num_queue.list.head
    while node != None:
       print(node.data, end=' ')
       node = node.next
    print()
    
    # Dequeue 17
    dequeued_item = num_queue.dequeue()
    print('Dequeued:', dequeued_item)
    
    # Output final queue
    print('Queue after dequeue:', end=' ')
    node = num_queue.list.head
    while node != None:
       print(node.data, end=' ')
       node = node.next
    print()

# Call the main function.
if __name__ == "__main__":    
    main()