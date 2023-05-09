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



# Main program to test Binary search tree.
from Node import Node
from BinarySearchTree import BinarySearchTree
import random

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
                               "5) Land the next plane.\n"\
                               "0) Exit the program.\n"\
                               "----------------------------------------\n"\
                               "Enter your choice:  "))
                
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

#=============#
def contMenu():
#=============#

    """
    This function asks the user if he wants to continue for the option he is currently
    using at the time.

    inputs: none
    outputs: cont (the continuation sentinel value)
    """

    while True:
        try:
            # Asking the player if he wants to purchase another item.
            cont = int(input("\nDo you want to add another plane?\n" + \
                         "1) Yes\n" + \
                         "2) No\n" + \
                         "Enter your choice:  "))
            
            # If the user does not enter 1 or 2.
            if (cont < 1 or cont > 3):
                raise ValueError
        
        # If the user does not enter an int, display an error message.
        except ValueError:
            
            print("\nPlease input a valid integer value.")
        
        # Catch-all general error.
        except:
            print("\nGeneral Error.")
            
        else:
            break
    
    return cont

#=============================#
def landing(landingTime, tree):
#=============================#

     # move to main and iterate in function and just use remove for all first 
     # nodes less than current time
        
    # inorderList = tree.inorderList()
    
    while (tree.inorderList()[0] < landingTime):
        tree.remove(tree.inorderList()[0])
        # del inorderList[0]

#==========================#    
def printLandingSched(tree):
#==========================#

    print("Landing Schedule: ", ', '.join(tree.inorderList()))



#=========#
def main():
#=========#

    # Main program to test Binary search tree.

    # TODO: - Work on datetime conversion to seconds or minutes.  Or just add funtionality to land
    #         next plane and advance time to the time of the next plane (then remove the plane)
    #       - Print tree at the start of each option so that the user knows the times.
    #       - Add k = 3 provisions. (Ask the user for the value of k.) (@ insert and initial tree
    #         creation)
    #       - Add while loop for the user to input the planes one-at-a-time and check to see if
    #         the planes have proper separation (k value).
    #       - Try a plane list inorder, random, reverse order to debug the program

    # Initialize the sentinel value to zero.
    sent = -1
    time = 0
    tree = BinarySearchTree()

    if DEBUG != True:
        while True:
                        
            try:
                k = float(input("What should the time between landings be? \n" +\
                              "(Please only use integers.)\n" + \
                              "k = "))
                
                
                        
            # If the user does not enter an int, display an error message.
            except ValueError:
                            
                print("\nPlease input a valid integer value.")
                        
            # Catch-all general error.
            except:
                print("\nGeneral Error.")
                            
            else:
                break
        
        # Input plane times.
    
    
        userList = []
        while True:
            
            try:
                i = 0
                
                user_value = float(input('Enter values of plane landing times (-1 to exit): '))
                
                if user_value == -1:
                    break
                
                if userList is None:
                    continue
                else: 
                    for i in range(len(userList)):
                        
                        if abs(user_value - userList[i]) < k:
                            raise ValueError("The current plane is too close to the other planes you" + 
                                             "have already entered.")
                
                userList.append(user_value)
                new_node = Node(int(user_value))
                tree.insert(new_node)
                
                i+=1
                        
            # If the user does not enter an int, display an error message.
            except ValueError:
                            
                print("\nPlease input a valid integer value.")
                        
            # Catch-all general error.
            except:
                print("\nGeneral Error.")
                
                
    # user_values = 15 8 72 13 1 0 45 38 42"
    # user_values = 5 10 16 23 37 42 49 54"
    user_values = []
    for i in range(10):
        user_values.append(round(random.uniform(0.0, 100.0), 2))
        
    
    print("\nLanding Schedule:  ", ', '.join(user_values))
    print()
    
    k = 3
    print("k = ", k)
    print()
    
    
    # a list with input values
    for value in user_values:
        new_node = Node(value)
        tree.insert(new_node)
    
    if DEBUG:
        print('Initial tree:')
        print(tree)
        print()
        
    # tree.printInorder()
    # inorderList = tree.inorderList()
    # print("Tree List: ", inorderList)
    # print("Least value in tree: ", inorderList[0])
        
    
    # landing(9, tree)
    # print(tree)
    # tree.printInorder()
    
    

    # While the user wants to continue to use the program (the sentinel value is not equal to 5):
    while sent != 0:
    
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
                        printLandingSched(tree)
                        # Print option label.
                        print("\n |===================================|"\
                              "\n | OPTION 1:  Add a plane at time t. |"\
                              "\n |===================================|\n")
                        
                        # Insert a node. Must send a Node object to the insert method instead of a number.
                        insert_value = float(input("Enter a value to insert into the tree: "))
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
                    
                cont = contMenu()
                    
                    
        #===============================================#
        # OPTION 2:  Find a plane scheduled for time t. #
        #===============================================#
        
        # If the user chooses option 2:
        elif sent == 2:

            # Initialize the continuation value. (just for this option)
            cont = 1
            
            # While the user wants to continue with the purchase:
            while cont != 2:
                
                while True:
                    
                    try:
                        printLandingSched(tree)
                        # Print option label.
                        print("\n |===============================================|"\
                              "\n | OPTION 2:  Find a plane scheduled for time t. |"\
                              "\n |===============================================|\n")
            
                        # Search for a number.
                        search_value = float(input("Enter a value to look for in the BST: "))
                        # search_value = 45
                        print()                        
                    
                    # If the user does not enter an int, display an error message.
                    except ValueError:
                        
                        print("\nPlease input a valid Node value.")
                    
                    # Catch-all general error.
                    except:
                        print("\nGeneral Error.")
                        
                    else:
                        
                        if tree.search(search_value):
                            print("The node exists in the tree.\n")
                        else:
                            print("Value not found.\n")
                            
                        printLandingSched(tree)
                        
                        if DEBUG:
                            print(tree)
                        
                        break                    
                    
                cont = contMenu()
             
        #=================================================#
        # OPTION 3:  Remove a plane scheduled for time t. #
        #=================================================#
        
        # If the user chooses option 3:
        elif sent == 3:

            # Initialize the continuation value. (just for this option)
            cont = 1
            
            # While the user wants to continue with the purchase:
            while cont != 2:
                
                while True:
                    
                    try:
                        printLandingSched(tree)
                        # Print option label.
                        print("\n |=================================================|"\
                              "\n | OPTION 3:  Remove a plane scheduled for time t. |"\
                              "\n |=================================================|\n")
                        
                        # Remove a node. Only need to send a "key" value to the remove method.
                        remove_value = float(input('Enter value to remove: '))
                        print()

                        if tree.search(remove_value):
                            print("The node exists in the tree.")
                        else:
                            print("Value not found.")
                            raise ValueError
                    
                    # If the user does not enter an int, display an error message.
                    except ValueError:
                        
                        print("\nPlease input a valid Node value.")
                    
                    # Catch-all general error.
                    except:
                        print("\nGeneral Error.")
                        
                    else:
                        
                        print('Tree after removing %d:' % remove_value)
                        tree.remove(remove_value)
                        printLandingSched(tree)
                        
                        if DEBUG:
                            print(tree)
                        
                        break                    
                    
                cont = contMenu()
                            
        #======================================#
        # OPTION 4:  Print the list of planes. #
        #======================================#
        
        # If the user chooses option 4:
        elif sent == 4:
            
            print("\n |======================================|"\
                  "\n | OPTION 4:  Print the list of planes. |"\
                  "\n |======================================|\n")
            
            if DEBUG:
                print(tree)
                
            printLandingSched(tree)
            
            cont = contMenu()
            
        #=================================#
        # OPTION 5:  Land the next plane. #
        #=================================#
        
        # If the user chooses option 4:
        elif sent == 5:
            
            print("\n |=================================|"\
                  "\n | OPTION 5:  Land the next plane. |"\
                  "\n |=================================|\n")
            
            if DEBUG:
                print(tree)
                
            print("Current time: ", time)
            printLandingSched(tree)
            time = float(input("What time do you want to advance to?\t"))
            
            landing(time, tree)
            
            print("New time: ", time)
            printLandingSched(tree)
            
            cont = contMenu()
            
        #==============================#
        # OPTION 0:  Exit the program. #
        #==============================#
        
        # If the user chooses option 0:
        elif sent == 0:
            
            # Display a good-bye message and terminate the program.
            print("\nExiting Program.")

# Call the main function.
if __name__ == "__main__":    
    main()
