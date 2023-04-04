# RunwayReservationSystem
# Python implementation
# v1 - by ChatGPT 4/4/23

"""
Q: What are the advantages and disadvantages of these two approaches?

A:
There are advantages and disadvantages to both approaches of using an array and using a binary search tree for the Runway Reservation System.

Advantages of using an array:

    Simple implementation: Using an array is a straightforward implementation that does not require much knowledge of data structures or algorithms. This makes it easy to implement and understand.
    Efficient lookups: Since the array is sorted by time, lookups can be performed efficiently using binary search. This ensures that the time complexity of lookups is O(log n), where n is the number of planes in the system.

Disadvantages of using an array:

    Inefficient removals: Removing a plane from an array requires shifting all the elements after the removal point one position to the left. This can be inefficient for large arrays and result in O(n) time complexity for removals.
    Limited scalability: As the number of planes in the system grows, the size of the array may become impractically large. This can limit the scalability of the system.

Advantages of using a binary search tree:

    Efficient removals: Removing a plane from a binary search tree can be done efficiently in O(log n) time complexity, where n is the number of planes in the system. This is because the tree structure allows for efficient removals by simply rearranging the nodes of the tree.
    Scalability: Binary search trees can scale to handle large numbers of planes in the system without becoming impractically large. This makes them suitable for large-scale systems.
    Flexibility: Binary search trees can be modified to support additional operations, such as range queries or nearest-neighbor searches.

Disadvantages of using a binary search tree:

    More complex implementation: Implementing a binary search tree requires more knowledge of data structures and algorithms than using an array. This can make it more difficult to implement and understand.
    Unbalanced trees: In some cases, binary search trees can become unbalanced, which can result in degraded performance. This can be mitigated by using balanced binary search trees, but this adds additional complexity to the implementation.
"""

from RRS import RunwayReserver
#from RRS_BST import RunwayReserver

# sample usage by ChatGPT
def main():
  # create a new RunwayReserver object
  r = RunwayReserver()
  
  # add a plane with callsign "AA123" at time 10
  r.add_plane("AA123", 10.0)
  
  # lookup plane "AA123" at time 10
  print(r.lookup_plane("AA123", 10.0))  # "AA123 is scheduled at 10"
  
  # lookup plane "AA123" at time 8
  print(r.lookup_plane("AA123", 8.0))  # "AA123 is not scheduled at 8.0"
  
  # remove plane "AA123" at time 10
  r.remove_plane("AA123", 10.0)
  
  # lookup plane "AA123" at time 10 after removing it
  print(r.lookup_plane("AA123", 10.0))  # "AA123 is not scheduled at 10"

if __name__ == "__main__":
  main()