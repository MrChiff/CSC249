# ==================================================================================================
# CSC 249
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
# Requirement	                                                                       Required For:
# -Implementation in Python or C++ using linked lists	                               Bronze
# -Menu system that allows the player to choose from the required options	           Bronze
# -Ability to purchase items with correct name and price	                           Bronze
# -Ability to view the player's inventory with correct name, (quantity?), and value	   Silver
# -Ability to sell items back to the shop with correct name and quantity	           Gold
# -Ability to properly handle quantities of items	                                   Gold
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


# Questions:
    # Am I going to need to use one of the searching algorithms to find the items?
    # I need help with the searching alg in LinkedList file.
    # What kind of items should I put in here and how many and how much credit?

from CSC249_M4HW_LinkedList_JonathanHardwick import Node, LinkedList

#=============#
def mainMenu():
#=============#

    """ 
    This function displays the main menu to the user. 
    
    inputs: none
    outputs: sent (user selection/sentinel value) and displays main menu
    """
    
    while True:
        
        # Ask the user to choose one of the options.
        try:
            sent = int(input("\n----------------- Menu -----------------\n"\
                               "1) Purchase an item.\n"\
                               "2) View inventory.\n"\
                               "3) Sell an item.\n"\
                               "4) View total inventory value.\n"\
                               "5) Exit the program.\n"\
                               "----------------------------------------\n"\
                               "Enter your choice:\t"))
                
        # If the user does not enter an int, display an error message.
        except ValueError:
            print("\nPlease enter an appropriate choice.")
        
        # General error statement.
        except:
            print("General Error.")
        
        # Int input validation. 
        else:
            
            # If the user's input is an integer but not and appropriate choice: 
            if (sent > 5):
                errorMessage()
                mainMenu()
            
            # If the user's input passes the previous validation steps, break the while loop and 
            # return "sent".
            else:
                break
    
    return sent

#=================#
def errorMessage():
#=================#

    """ 
    This function lets the user know that the option chosen is not in the menu. 
    
    inputs: none
    outputs: displays error message and the main menu
    """
    
    print("\nError:  Your choice is not valid.  Please enter a corrrect value.")
    
#====================#
def playerInventory():
#====================#    

    """
    This function creates the player's inventory.
    """

    node1 = Node("sword")
    node2 = Node("sheild")
    node3 = Node("boots")
    node4 = Node("shirt")
    node5 = Node("pants")
    node6 = Node("potion")
    node7 = Node("bow")
    node8 = Node("arrows")
    node9 = Node("llama")
    node10 = Node("helmet")
    
    player_inventory = LinkedList()
    player_inventory.append(node1)
    player_inventory.append(node2)
    player_inventory.append(node3)
    player_inventory.append(node4)
    player_inventory.append(node5)
    player_inventory.append(node6)
    player_inventory.append(node7)
    player_inventory.append(node8)
    player_inventory.append(node9)
    player_inventory.append(node10)
    
    return player_inventory

#==================#
def shopInventory():
#==================#    

    """
    This function creates the shop's inventory.
    """

    node1 = Node("sword")
    node2 = Node("sheild")
    node3 = Node("boots")
    node4 = Node("shirt")
    node5 = Node("pants")
    node6 = Node("potion")
    node7 = Node("bow")
    node8 = Node("arrows")
    node9 = Node("llama")
    node10 = Node("helmet")
    node11 = Node("horse")
    node12 = Node("saddle")
    node13 = Node("gold")
    node14 = Node("sleeping bag")
    node15 = Node("book")
    node16 = Node("key")
    node17 = Node("apple")
    node18 = Node("jewel")
    node19 = Node("axe")
    node20 = Node("bomb")
    
    
    shop_inventory = LinkedList()
    shop_inventory.append(node1)
    shop_inventory.append(node2)
    shop_inventory.append(node3)
    shop_inventory.append(node4)
    shop_inventory.append(node5)
    shop_inventory.append(node6)
    shop_inventory.append(node7)
    shop_inventory.append(node8)
    shop_inventory.append(node9)
    shop_inventory.append(node10)
    
    return shop_inventory



    
#=========#
def main():
#=========#

    # Initialize the sentinel value to zero.
    sent = 0

    # While the user wants to continue to use the program (the sentinel value is not equal to 6):
    while sent != 5:
    
        # Display the main menu to the user.
        sent = mainMenu()
        
        # Creating Player inventory:
        player_inventory = playerInventory()
            
            
        # Creating shop inventory:
        shop_inventory = shopInventory()
        
        #==============================#
        # OPTION 1:  Purchase an item. #
        #==============================#
        
        # If the user chooses option 1:
        if sent == 1:
            
            print("\n |==============================|"\
                  "\n | OPTION 1:  Purchase an item. |"\
                  "\n |==============================|")
            
            # Call 
            
        #============================#
        # OPTION 2:  View inventory. #
        #============================#
        
        # If the user chooses option 2:
        elif sent == 2:
            
            print("\n |============================|"\
                  "\n | OPTION 2:  View inventory. |"\
                  "\n |============================|")
                
        #==========================#
        # OPTION 3:  Sell an item. #
        #==========================#
        
        # If the user chooses option 3:
        elif sent == 3:
            
            print("\n |==========================|"\
                  "\n | OPTION 3:  Sell an item. |"\
                  "\n |==========================|")
                
        #========================================#
        # OPTION 4:  View total inventory value. #
        #========================================#
        
        # If the user chooses option 4:
        elif sent == 4:
            
            print("\n |========================================|"\
                  "\n | OPTION 4:  View total inventory value. |"\
                  "\n |========================================|")
            
            
        #==============================#
        # OPTION 5:  Exit the program. #
        #==============================#
        
        # If the user chooses option 5:
        elif sent == 5:
            
            # Display a good-bye message and terminate the program.
            print("\nExiting Program.")
        
        #=================#
        # INCORRECT ENTRY #
        #=================#
            
        # If the user chooses an option that is not 1-5:
        # else: 
            
        #     # Display a message that tells them their entry was invalid and ask that they renter a
        #     # correct value. This is a redundency for the input validation in the mainMenu() 
        #     # function.
        #     errorMessage()
        #     mainMenu()

# Call the main function.
if __name__ == "__main__":    
    main()