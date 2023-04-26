# M6HW
#
# M6HW (Due last class meeting)
#
# For this assignment, you will implement the Runway Reservation System as a menu-based program. 
# (See the previously posted documents in this module for the specifications of the system.)
#
# Bronze:
#    
# Implement a RunwayReserver class which has the following features:
#    
#     1.  Add a plane at time t to the list of R, runway reservation times.
#     2.  Find a plane scheduled for time t (if it exists)
#     3.  Print the list of planes in R.
#     4.  Remove a plane scheduled for time t.
#
# Silver:
#    
# As above, plus:
#    
#     1.  The underlying data structure used must be a Binary Search Tree. (The code provided in 
#         6-12 is a reasonable starting point.)
#     2.  The RunwayReserver has a constant time k (set this 
#         to k=3). A plane cannot be added if it's landing 
#         time is within k minutes of an already scheduled 
#         plane.
#        
# For Bronze and Silver, you can write some sample code in main to add planes, remove planes, and 
# list planes, but you do not have to provide a full user interface. (You should at least 
# demonstrate two actions of each of add, remove, find, and list.)
#
# Gold:
#    
# As above, plus the program should now be menu-driven. The user can:
#    
#     1.  Add planes to the reservation list.
#     2.  Search for a plane at time t, and be told whether or 
#         not that time has a scheduled landing.
#     3.  Remove a plane at time t.
#     4.  Print the list of all planes in the reserve list
#     5.  Advance the current time, which does the following:
#         1.  Prints all planes in the list before time 
#             advances
#         2.  Removes planes in ascending time order until all    
#             planes scheduled have landed
#         3.  Prints all planes in the list after time 
#             advances.
#===================================================================================================

# Questions:
# Do I allow the user to create the initial tree or should I hard code a tree for the user to 
# manipulate?
#

# Main program to test Binary search tree.
from Node import Node
from BinarySearchTree import BinarySearchTree

DEBUG = True;

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
                               "1) Add a plane at time t.\n"\
                               "2) Find a plane scheduled for time t.\n"\
                               "3) Remove a plane scheduled for time t.\n"\
                               "4) Print the list of planes.\n"\
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

#=========#
def main():
#=========#

    # Initialize the sentinel value to zero.
    sent = 0
    tree = BinarySearchTree()
    
    # Input plane times.
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
    

    # While the user wants to continue to use the program (the sentinel value is not equal to 5):
    while sent != 5:
    
        # Display the main menu to the user.
        sent = mainMenu()
        
        #===================================#
        # OPTION 1:  Add a plane at time t. #
        #===================================#
        
        # If the user chooses option 1:
        if sent == 1:
            
            # Initialize the continuation value. (just for this option)
            cont = 1
            
            # While the user wants to continue with the purchase:
            while cont != 2:
                
                while True:
                    
                    try:
                        # Print option label.
                        print("\n |===================================|"\
                              "\n | OPTION 1:  Add a plane at time t. |"\
                              "\n |===================================|\n")
                        
                        # Insert a node. Must send a Node object to the insert method instead of a number.
                        insert_value = int(input("Enter a value to insert into the tree: "))
                        # insert_value = 36
                        print()
                    
                    # If the user does not enter an int, display an error message.
                    except ValueError:
                        
                        print("\nPlease input a valid integer value.")
                    
                    # Catch-all general error.
                    except:
                        print("\nGeneral Error.")
                        
                    else:
                        
                        print("Tree after inserting %d: " % insert_value)
                        tree.insert(Node(insert_value))
                        
                        if DEBUG:
                            print(tree)
                        
                        break

                    
                    
                    
                    
                while True:
                    try:
                        # Asking the player if he wants to purchase another item.
                        cont = int(input("\nDo you want to add another plane?\n" + \
                                     "1) Yes\n" + \
                                     "2) No\n"))
                        
                        # If the user does not enter 1 or 2.
                        if (cont < 0 or cont > 3):
                            raise ValueError
                    
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
            
            # Display player's inventory.
            printInventory("player", player_inventory)
            
            # Display player's currency
            print("Amount of gold: ", player_money)
             
        #==========================#
        # OPTION 3:  Sell an item. #
        #==========================#
        
        # If the user chooses option 3:
        elif sent == 3:
            
            cont = 1
            while cont != 2:
                
                while True:
                    
                    # Print option label.
                    print("\n |==========================|"\
                          "\n | OPTION 3:  Sell an item. |"\
                          "\n |==========================|\n")
                        
                    # Display the shops inventory to determine what and how much to purchase    
                    printInventory("player", player_inventory)
                    
                    # Remind the user how much money he has to use.
                    print("Amount of gold: ", player_money)
                    
                    # Prompt the user for the name of the item he wants to sell.
                    itemName = input("""\nWhat is the item that you want to sell? ("cancel" to exit)\t""")
                    itemName = itemName.strip().lower()
                    
                    if itemName == "cancel":
                        break
                    
                    # Finding the item the player wants to sell.
                    selling = player_inventory.ListSearch(itemName)
                    
                    if selling:
                        
                        itemQuantity = -1
                    
                        while itemQuantity < 0:
                            try: 
                                # Prompt the user for the number of items he wants to purchase.
                                itemQuantity = int(input("\nHow many " + itemName + "s do you want to sell?\t"))
                                
                                if (itemQuantity < 0):
                                    raise ValueError
                                    
                            # If the user does not enter an int, display an error message.
                            except ValueError:
                                print("\nPlease use only positive integer values.")
                            
                            # General error statement.
                            except:
                                print("General Error.")
                        
                        if TESTING:
                            print("\nYou want to sell " + str(itemQuantity) + " " + itemName + "s.\n")
                        else:
                            print()
                        
                        # If the item is found in the player's inventory and the quantity to sell does
                        # not exceed the inventory quantity:
                        if (itemQuantity <= selling.quant):
                            
                            player_money = player_money + selling.price * itemQuantity
                            
                            if TESTING:
                                printInventory("shop (before sale)", shop_inventory)
                                time.sleep(3)
                                
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
                                time.sleep(3)
                            
                            # Create new player_inventory node
                            update_player_node = Node(selling.item, selling.price,\
                                                      selling.quant - itemQuantity)
                            # Update player_inventory item quantity
                            existingItemQuantityUpdate(player_inventory, selling, update_player_node)
                            
                            if TESTING:
                                printInventory("player", player_inventory)
                                time.sleep(3)
                            
                            print("Amount of gold: ", player_money)
                            break
                        
                        # If the item is found in the player's inventory but the quantity to sell
                        # exceeds the inventory quantity:  display an error
                        else:
                            print("You don't have " + str(itemQuantity) + " " + itemName + \
                                  "s. (quantity cannot exceed inventory)")
                            time.sleep(3)
                                
                    else:
                        
                        print("\n" + itemName.capitalize() + " not found! Try again!")
                        time.sleep(3)
                        
                while True:
                    try:
                        # Asking the player if he wants to purchase another item
                        cont = int(input("\nDo you want to sell another item?\n" + \
                                     "1) Yes\n" + \
                                     "2) No\n"))
                            
                        if (cont < 0 or cont > 3):
                            raise ValueError
                    
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
                  "\n |========================================|\n")
            
            printInventory("player", player_inventory)
            print("Total Value = ", player_inventory.inventoryValue())
            
            
        #==============================#
        # OPTION 5:  Exit the program. #
        #==============================#
        
        # If the user chooses option 5:
        elif sent == 5:
            
            # Display a good-bye message and terminate the program.
            print("\nExiting Program.")

# Call the main function.
if __name__ == "__main__":    
    main()
