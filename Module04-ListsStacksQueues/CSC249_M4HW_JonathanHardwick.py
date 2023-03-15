# ==================================================================================================
# CSC 249
# M4HW
# Jonathan Hardwick
# 2023/03/19
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
    # Why do I have to return a string for __repr__

import os
os.system('cls' if os.name == 'nt' else 'clear')

from CSC249_M4HW_LinkedList_JonathanHardwick import Node, LinkedList
import random
import time

TESTING = True

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

#===================#    
def inventoryItems():
#===================#
    
    items = ["sword", "sheild", "boots", "shirt", "pants", "potion", "bow", "arrows", "llama", \
             "helmet", "horse", "saddle", "gold", "sleeping bag", "book", "key", "apple", "jewel", \
             "axe", "bomb"]
        
    prices = [8, 5, 3, 5, 6, 2, 4, 1, 300, 7, 100, 30, 50, 10, 3, 6, 2, 25, 10, 3]
    
    return (items, prices)

#====================#
def playerInventory():
#====================#    

    """
    This function creates the player's inventory.
    """
    
    player_inventory = LinkedList()
    items, prices = inventoryItems()
    player_quantities = []
    for i in range(10):
        player_quantities.append(random.randint(1,10))
    
    for i in range(10):
        player_inventory.append(Node(items[i], prices[i], player_quantities[i]))
    
    return player_inventory

#==================#
def shopInventory():
#==================#    

    """
    This function creates the shop's inventory.
    """

    shop_inventory = LinkedList()
    items, prices = inventoryItems()
    shop_quantities = []
    for i in range(len(prices)):
        shop_quantities.append(random.randint(1,10))
    
    for i in range(len(items)):
        shop_inventory.append(Node(items[i], prices[i], shop_quantities[i]))
    
    return shop_inventory

#==============================================================#
def existingItemQuantityUpdate(inventory, old_entry, new_entry):
#==============================================================#
    
    # if the quantity of the head is <= 0, remove the head
    if (old_entry.prev is None and new_entry.quant <= 0):
        inventory.remove(old_entry)
        
    # if updating the head:
    elif (old_entry.prev is None):
        inventory.prepend(new_entry)
        inventory.remove(old_entry)
    
    # if the quantity is zero => remove item entirely from list
    elif (new_entry.quant <= 0):
        inventory.remove(old_entry)
        
    # if any other node in linked list:
    else:
        inventory.insert_after(old_entry.prev, new_entry)
        inventory.remove(old_entry)

#==================================#
def printInventory(name, inventory):
#==================================#   

    print(name.capitalize() + " Inventory")
    print(inventory)
    
    

#=========#
def main():
#=========#

    # Initialize the sentinel value to zero.
    sent = 0
    
    # Thoughts: !!!!!!!!!!!
    # could save the player/shop inventory by saving to a file and reading in the file at the start 
    # of the program.
    # if file exists:
    #   read in file contents
    # else:
    #   initialize player/shop inventory with the playerInventory() and shopInventory() functions
    # use json.loads and json.dumps to save the cart
    
        
    # Creating Player inventory:
    player_inventory = playerInventory()
    player_money = 100
    
    # Creating shop inventory:
    shop_inventory = shopInventory()

    # While the user wants to continue to use the program (the sentinel value is not equal to 6):
    while sent != 5:
    
        # Display the main menu to the user.
        sent = mainMenu()
        
        #==============================#
        # OPTION 1:  Purchase an item. #
        #==============================#
        
        # If the user chooses option 1:
        if sent == 1:
            cont = 1
            while cont != 2:
                while True:
                    print("\n |==============================|"\
                          "\n | OPTION 1:  Purchase an item. |"\
                          "\n |==============================|\n")
                        
                    printInventory("shop", shop_inventory)
                    print("Amount of gold: ", player_money)
                    
                    itemName = input("\nWhat is the item that you want to purchase? (cancel to exit)\t")
                    itemName = itemName.strip().lower()
                    if itemName == "cancel":
                        break
                    
                    # Assigns the node with the matching name to a new variable to make it shorter
                    # to use the components of the Node() class.
                    purchase = shop_inventory.ListSearch(itemName)
                    
                    if purchase:
                    
                        # add exception handling
                        itemQuantity = int(input("\nHow many " + itemName + "s do you want to buy?\t"))
                        
                        # Check to see if the item is in the shop inventory
                        if (itemQuantity < purchase.quant):
                            
                            print("\n" + itemName.capitalize() + " found in stock! (quantity: " \
                                  + str(purchase.quant) + ")")
                                
                            time.sleep(3)
                        
                            # Subtract price from player's money.
                            # !!!!!!Consider adding this as a class (review 221)
                            # check to make sure funds are available
                            if (player_money < purchase.price*itemQuantity):
                                print("\nYou do not have enough funds to make this purchase.")
                                time.sleep(3)
                                break
                            
                            else:
                                
                                player_money = player_money - purchase.price * itemQuantity
                            
                            if TESTING:
                                
                                print()
                                printInventory("player (before purchase)", player_inventory)
                            
                            # Does the player already have this item?
                            item_in_player_inventory = player_inventory.ListSearch(itemName)
                            
                            # Updating player inventory.
                            # If the same type of item already exists in the player inventory:
                            if item_in_player_inventory:
                                
                                # Increase the quantity of the item in the player's inventory
                                update_player_node = Node(item_in_player_inventory.item,\
                                                          item_in_player_inventory.price,\
                                                          item_in_player_inventory.quant + itemQuantity)
                                
                                # can update node.quant directly
                                # node.quant = node.quant +/- itemQuantity
                                
                                
                                # Updating player_inventory linked list
                                existingItemQuantityUpdate(player_inventory, item_in_player_inventory,\
                                                           update_player_node)
                                
                            # If the item is not in the player inventory:
                            else:    
                                # Add new item to player's inventory.
                                player_inventory.append(Node(purchase.item, purchase.price, itemQuantity))
                                
                            printInventory("player", player_inventory)
                            print("Amount of gold: ", player_money)
                            
                            # Create new shop_inventory node
                            update_shop_node = Node(purchase.item, purchase.price, purchase.quant - itemQuantity)
                            # Update shop_inventory item quantity
                            existingItemQuantityUpdate(shop_inventory, purchase, update_shop_node)
                            
                            if TESTING:
                                print()
                                printInventory("updated shop", shop_inventory)
                        
                        # Make sure there are enough items in stock.
                        else:
                            
                            print("\nThere are not " + str(itemQuantity) + " " + itemName + "s in stock. "\
                                  "You can only purchase " + str(purchase.quant) + " or fewer." )
                            time.sleep(3)
                    
                    else:
                        
                        print("\n" + itemName.capitalize() + " not found! Try again!")
                    
                while True:
                    try:
                        # Asking the player if he wants to purchase another item
                        cont = int(input("\nDo you want to purchase another item?\n" + \
                                     "1) Yes\n" + \
                                     "2) No\n"))
                    
                    # If the user does not enter an int, display an error message.
                    except ValueError:
                        
                        print("\nPlease input a valid integer value.")
                    
                    # Catch-all general error.
                    except:
                        print("\nGeneral Error.")
                        
                    else:
                        
                        break
                    
        #============================#
        # OPTION 2:  View inventory. #
        #============================#
        
        # If the user chooses option 2:
        elif sent == 2:
            
            print("\n |============================|"\
                  "\n | OPTION 2:  View inventory. |"\
                  "\n |============================|\n")
                
            printInventory("player", player_inventory)
             
        #==========================#
        # OPTION 3:  Sell an item. #
        #==========================#
        
        # If the user chooses option 3:
        elif sent == 3:
            
            cont = 1
            while cont != 2:
                
                while True:
                    print("\n |==========================|"\
                          "\n | OPTION 3:  Sell an item. |"\
                          "\n |==========================|\n")
                        
                    printInventory("player", player_inventory)
                        
                    itemName = input("""\nWhat is the item that you want to sell? ("cancel" to exit)\t""")
                    itemName = itemName.strip().lower()
                    
                    if itemName == "cancel":
                        break
                    
                    # Finding the item the player wants to sell.
                    selling = player_inventory.ListSearch(itemName)
                    
                    if selling:
                    
                        # add exception handling
                        itemQuantity = int(input("\nHow many " + itemName + "s do you want to sell? \t"))
                        
                        if TESTING:
                            print("\nYou want to sell " + str(itemQuantity) + " " + itemName + "s.\n")
                        else:
                            print()
                        
                        # If the item is found in the player's inventory and the quantity to sell does
                        # not exceed the inventory quantity:
                        if (itemQuantity <= selling.quant):
                            
                            # print("\n" + itemName.capitalize() + " found in your inventory! (quantity: " \
                            #       + str(selling.quant) + ")")
                            
                            player_money = player_money + selling.price * itemQuantity
                            
                            if TESTING:
                                printInventory("shop (before sale)", shop_inventory)
                                
                            # Does the player already have this item?
                            item_in_shop_inventory = shop_inventory.ListSearch(itemName)
                            
                            # Updating shop inventory.
                            # If the same type of item already exists in the shop's inventory:
                            if item_in_shop_inventory:
                                
                                # Increase the quantity of the item in the shop's inventory
                                update_shop_node = Node(item_in_shop_inventory.item,\
                                                          item_in_shop_inventory.price,\
                                                          item_in_shop_inventory.quant + itemQuantity)
                                    
                                # Updating player_inventory linked list
                                existingItemQuantityUpdate(shop_inventory, item_in_shop_inventory,\
                                                           update_shop_node)
                                    
                            # If the item is not in the shop inventory:
                            else:    
                                # Add new item to shop's inventory.
                                shop_inventory.append(Node(selling.item, selling.price, itemQuantity))
                            
                            if TESTING:
                                printInventory("shop", shop_inventory)
                            
                            # Create new player_inventory node
                            update_player_node = Node(selling.item, selling.price,\
                                                      selling.quant - itemQuantity)
                            # Update player_inventory item quantity
                            existingItemQuantityUpdate(player_inventory, selling, update_player_node)
                            
                            if TESTING:
                                printInventory("player", player_inventory)
                            
                            print("Amount of gold: ", player_money)
                            break
                        
                        # If the item is found in the player's inventory but the quantity to sell
                        # exceeds the inventory quantity:  display an error
                        else:
                            print("You don't have " + str(itemQuantity) + " " + itemName + \
                                  "s. (quantity cannot exceed inventory)")
                                
                    else:
                        
                        print("\n" + itemName.capitalize() + " not found! Try again!")
                        
                while True:
                    try:
                        # Asking the player if he wants to purchase another item
                        # Add exception handling 
                        cont = int(input("\nDo you want to sell another item?\n" + \
                                     "1) Yes\n" + \
                                     "2) No\n"))
                    
                    # If the user does not enter an int, display an error message.
                    except ValueError:
                        
                        print("\nPlease input a valid integer value.")
                    
                    # Catch-all general error.
                    except:
                        print("\nGeneral Error.")
                        
                    else:
                        break
                            
                    
                
        #========================================#
        # OPTION 4:  View total inventory value. #
        #========================================#
        
        # If the user chooses option 4:
        elif sent == 4:
            
            print("\n |========================================|"\
                  "\n | OPTION 4:  View total inventory value. |"\
                  "\n |========================================|")
            
            printInventory("player", player_inventory)
            print("Total Value = ", player_inventory.inventoryValue())
            
            
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