# M6HW

# M6HW (Due last class meeting)

# For this assignment, you will implement the Runway Reservation System as a menu-based program. 
# (See the previously posted documents in this module for the specifications of the system.)

# Bronze:
    
# Implement a RunwayReserver class which has the following features:
    
#     1.  Add a plane at time t to the list of R, runway reservation times.
#     2.  Find a plane scheduled for time t (if it exists)
#     3.  Print the list of planes in R.
#     4.  Remove a plane scheduled for time t.

# Silver:
    
# As above, plus:
    
#     1.  The underlying data structure used must be a Binary Search Tree. (The code provided in 
#         6-12 is a reasonable starting point.)
#     2.  The RunwayReserver has a constant time k (set this 
#         to k=3). A plane cannot be added if it's landing 
#         time is within k minutes of an already scheduled 
#         plane.
        
# For Bronze and Silver, you can write some sample code in main to add planes, remove planes, and 
# list planes, but you do not have to provide a full user interface. (You should at least 
# demonstrate two actions of each of add, remove, find, and list.)

# Gold:
    
# As above, plus the program should now be menu-driven. The user can:
    
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


# Main program to test Binary search tree.
from Node import Node
from BinarySearchTree import BinarySearchTree

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
                               "3) Print the list of planes.\n"\
                               "4) Remove a plane scheduled for time t.\n"\
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


def main():
    
    tree = BinarySearchTree()
    
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
