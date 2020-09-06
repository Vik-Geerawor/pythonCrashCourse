# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from functions import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # test_func()

    ## greet_users
    # usernames = ['hannah', 'ty', 'margot']
    # greet_users(usernames)

    ## modifying list via functions
    # unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    # completed_models = []
    # print_models(unprinted_designs, completed_models)
    # show_completed_models(completed_models)

    ## modifying list via functions
    unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []
    print_models(unprinted_designs, completed_models)
    show_completed_models(completed_models)