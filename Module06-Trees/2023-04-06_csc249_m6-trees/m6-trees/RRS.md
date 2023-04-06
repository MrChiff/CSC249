# Runway Reservation System
## From MIT 6.006 FA11

Assume an airport with a single runway. 
(For example: San Diego Airport: https://youtu.be/U-phx0QV39w?t=690 or https://youtu.be/LigswTr9yzY)
Our problem is to reserve times for future landings. 

Add time t to the set R of landing times IF no other landings are scheduled within k minutes
(for example, k=3 minutes. k might vary based on weather.)

Reserving a landing time means inserting into the set if the constraint is satisfied.

as t increments, check the data structure and remove times as they have passed.

Our performance goal:
O(lg n) time, where n is the size of the set (|R| = n)

Example of use:
with k=3

now 37, 41.2, 49, 56.3
insert 53 -> OK
insert 44 -> not allowed (too close to 41.2)
insert 20 -> not allowed (in the past)

--
Proposing to use all the data structures we know, and then ruling them out
(with audience interaction)
1. unsorted list/array
	- every action is O(n)
2. sorted array
	- binary search means finding items is O(lg n) , so that's good
	- ex. to insert 34, i can find the 'insertion point' (the value below it, and above it)
	- now i look at both of those and do the k-constraint check
	- but insertion is O of what?
	formally:
	- it can find the smallest i such that R[i] >= t in O(lg n) time
	- compare R[i] and R[i-1] in O(1) time
	- but insertion is linear time since it requires shifting items to make room

3. Linked list
	- insertion is constant time
	- search is ...?

4. Heaps (not yet coverd) - minheaps, maxheaps
	- an array that you can visualize as a tree
	- the <=k or >=k from t check is O(n) time with a heap

5. Hash Table / Dictionary
	- good insertion time and search time
	- but the <=k or >=k from t check is O(n) time with a dictionary

Our pipe dream:
	- if we could do fast insertion into
	- a sorted array
then we would meet all of our constraints.

This is what BSTs do for us.

Binary Search Tree invariant:
	for all nodes x:
	- if y is in the left subtree of x, key(y) <= key(x)
	- if y is in the right subtree of x, key(y) >= key(x)


now model RRS with BST:
- insert O(h) where h=height of tree
- check (do the check during the search)
- delete
we haven't covered delete yet, when we do, we'll need to move pointers around (like with linked lists)


sample run:
insert 49, 79, 46, 41
insert 42, 45 

--
not quite done yet.
Many operations can be done on a BST in O(h) time, some in O(k) time

- find_min() -> keep going to the left
- find_max() -> keep going to the right
- next_largest(x) -> (find x, go one to the right)

--
Augmented BSTs - contain more data than just the pointers covered
("amending the design", for example add a record that our key relates to)

Let's assume that there's an additional constraint added to spec, that we have to solve with our BST design
- Be able to compute Rank(t) : How many planes are scheduled to land at times <= t ?

we augment the BST to handle this new spec change, without losing our performance
Augment the BST structure by adding to the node
- int: how many nodes are below this node

ex: 49, 46, 79, 64, 83
so the key is t, the value is associated with that key
when we insert or delete, we modify this 'size' value
we're using this to track the size of our 'subtree' (count yourself)
so 46 [1] , 64 [1] , 83 [1], 79 [3], 49 [5]

insert 43, follow the insertion path, as you go, increment each node by one,
so now 49 [6], 46 [2], 43 [1]
(note that you don't want to actually update these if the insert will fail, so search first then insert.)
there's a more efficient way (recursive, 1 pass) way to do this, but it's OK for a first look.

Now, how can we calculate Rank(t) from these subtree sizes?
(this comes later)
What lands before t?
1. walk down tree to find the desired time
2. add in the nodes that are smaller
3. add in the subtrees size to the left

do a lookup on time, and do the "<" operator to find all elements <= to t
ex. <= 79 t=79
49? it's less, add 1
- since i moved to the right, add the subtree size to the left (+2 from subtree 46)
79 <= 79, add 1
- add the subtree size to the left of 79 (so add 1)







