"""
Node class - used by various linked lists
included in main.py
"""

class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
