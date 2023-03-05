# ==================================================================================================
# M4HW
# Jonathan Hardwick
# 2023/03/?
# 
# In the previous Lab assignments, we created a few classes (Nodes, LinkedLists, and Items) and 
# confirmed that they work as expected.
# 
# Now we'll put those together to create a working program.
# 
# Assignment:
# Create a video game inventory shop system using linked lists. The system should allow players to 
# purchase items such as swords, potions, and armor from the shop, view their inventory, and sell 
# items back to the shop. The system should also calculate the total cost of the items in the 
# player's inventory.
# 
# Requirements:
#     -The program should be implemented in Python or C++ using linked lists.
#     -The program should have a menu system that allows the player to choose from the following 
#      options:
#         -Purchase an item
#         -View inventory
#         -Sell an item
#         -View total inventory value
#         -Exit the program
#     -When purchasing an item, the program should prompt the player for the item name and price.
#     -When viewing the player's inventory, the program should display the item name, quantity, and 
#      value for each item in the inventory.
#     -When selling an item back to the shop, the program should prompt the player for the name of 
#      the item to sell and the quantity to sell.
#     -When viewing the total inventory value, the program should display the total value of all 
#      items in the player's inventory.
# 
# Rubric:
# -The requirements above are for GOLD (100/100 max) tier. 
# -For Bronze : You do not have to handle "sell back to store", and you do not have to handle 
#  quantities of items. (So the player either has a potion, or they don't.)
# -For Silver :  You do not have to handle quantities of items.
#  
# Requirement	Required For:
# -Implementation in Python or C++ using linked lists	                                    Bronze
# -Menu system that allows the player to choose from the required options	                Bronze
# -Ability to purchase items with correct name and price	                                Bronze
# -Ability to view the player's inventory with correct name, (quantity?), and value	    Silver
# -Ability to sell items back to the shop with correct name and quantity	                Gold
# -Ability to properly handle quantities of items	                                        Gold
# Total Points: 100
# 
# Notes:
# You are welcome to fulfill the requirements any way you like -- here's how I would attack the 
# problem.
# 
# player_inventory and shop_inventory are clearly both linked lists. Individual items (whether in 
# the shop, or in the player's backpack) are nodes.
#                                                                                      
# Viewing items in the shop, or in the inventory, is an example of traversing a linked list, and 
# printing out the contents of each node in the list.
# 
# Purchasing an item is a multi-step process: First, you search a list, to see if the item the 
# player asked for (by typing in its name) actually exists. If it does, you then make a copy of it, 
# and add that copy to the player's inventory. (You'll also need to subtract money from the player's 
# total.) If you implement quantity, then this could get a little tricky. (You probably want to 
# traverse the list, and count how many of the same item are found.)
# 
# Selling an item back is the reverse of purchasing an item, except you can just remove the node 
# from the player's inventory (we assume the store never runs out of items). Again, if you implement 
# quantity, this could get tricky. (You may want to traverse the list, and count how many of the 
# same item are found.)
# 
# ==================================================================================================
