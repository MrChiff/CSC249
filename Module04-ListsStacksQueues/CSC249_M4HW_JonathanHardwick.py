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
    # Why do I have to return a string for __repr__
    # Should I use a dictionary or a set of lists to store the items, values, and quantity?
    # How to setup item, price and quantity in the Node class?  (individual vars, tuple, dictionary)
    # Do I need to add a while loop around each option in order to keep doing it until the player 
    #   opts out?

from CSC249_M4HW_LinkedList_JonathanHardwick import Node, LinkedList
import random

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
    
    shop_quantities = []
    for i in range(len(prices)):
        shop_quantities.append(random.randint(1,10))
        
    player_quantities = []
    for i in range(10):
        player_quantities.append(random.randint(1,10))
    
    itemDict = {"sword":8, "sheild":5, "boots":3, "shirt":5, "pants":(6,5), "potion":2, "bow":4, \
                "arrows":1, "llama":300, "helmet":7, "horse":100, "saddle":30, "gold":50, \
                "sleeping bag":10, "book":3, "key":6, "apple":2, "jewel":25, "axe":10, "bomb":3}
        
    shopDict = {}
    for i in range(len(items)):
        shopDict[items[i]] = (prices[i], shop_quantities[i])
        
    playerDict = {}
    for i in range(10):
        playerDict[items[i]] = (prices[i], player_quantities[i])
    
    # Displays the keys of the dictionary
    # print(itemDict.keys())
    # print(itemDict.values())
    
    # return (items, prices, shop_quantities, player_quantities)
    return (items, prices)#, shop_quantities, player_quantities)

#====================#
def playerInventory():
#====================#    

    """
    This function creates the player's inventory.
    """
    
    player_inventory = LinkedList()
    items, prices = inventoryItems()
    for i in range(10):
        player_inventory.append(Node(items[i], prices[i]))
    
    return player_inventory

#==================#
def shopInventory():
#==================#    

    """
    This function creates the shop's inventory.
    """

    shop_inventory = LinkedList()
    items, prices = inventoryItems()
    for i in range(len(items)):
        shop_inventory.append(Node(items[i], prices[i]))
    
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
        player_money = 900
            
            
        # Creating shop inventory:
        shop_inventory = shopInventory()
        
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
                          "\n |==============================|")
                        
                    print("\nShop Inventory:")
                    print(shop_inventory)
                    
                    itemName = input("What is the item that you want to purchase? (cancel to end)\t")
                    itemName = itemName.strip()
                    if itemName == "cancel":
                        break
                    
                    while True:
                        try:
                           reqPrice = int(input("\nWhat is the price of the " + itemName + \
                                                " you want to purchase?\t"))
                        
                        # If the user does not enter an int, display an error message.
                        except ValueError:
                            
                            print("\nPlease input a valid integer value.")
                        
                        # Catch-all general error.
                        except:
                            print("\nGeneral Error.")
                            
                        else:
                            break
                    
                    # TODO:
                        # Subtract value from player money (how much money to start with?)
                        # print updated shop inventory (remove node and then add updated node)
                        
                    # Verify the item exists in the shop inventory.
                    # !!!!!!!!! Thoughts:  This way I can pass the entire Node() with all values and 
                    # then choose the value I want when using ListSearch()
                    # if shop_inventory.ListSearch(itemName) == None:
                        # print(product not found. Try again.)
                    # elif shop_inventory.ListSearch(itemName) == reqPrice:
                        # item found and subtract money and add to player inventory
                        
                    if (shop_inventory.ListSearch(itemName) == reqPrice):
                        # print("\n" + itemName.capitalize() + " found!")
                    
                        # Subtract price from player's money.
                        # !!!!!!Consider adding this as a class (review 221)
                        player_money = player_money - reqPrice
                        
                        
                        # print("Player Inventory before addition:")
                        # print(player_inventory)
                            
                        # Add new item to player's inventory.
                        player_inventory.append(Node(itemName, reqPrice))
                             
                        print("\nPlayer Inventory:")
                        print(player_inventory)
                        break
                    
                    else:
                        print("\n" + itemName.capitalize() + " not found! Try again!")
                
                
                    
                while True:
                    try:
                        # Asking the player if he wants to purchase another item
                        # Add exception handling 
                        cont = int(input("Do you want to purchase another item?\n" + \
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
                
            print("Player Inventory")
            print(player_inventory)
            
            # TODO:
                # talley the number of each item to show
            
                
        #==========================#
        # OPTION 3:  Sell an item. #
        #==========================#
        
        # If the user chooses option 3:
        elif sent == 3:
            
            print("\n |==========================|"\
                  "\n | OPTION 3:  Sell an item. |"\
                  "\n |==========================|")
                
            itemName = input("What is the item that you want to sell?\t")
            itemQuantity = input("How many ", itemName,"s do you want to sell?\t")
                
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