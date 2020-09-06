# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from functions import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test_func():
    ## Calling the function
    # greet_user('Vik')  # argument

    ## describe_pet('hamster', 'harry')
    ## order of args is diff from params'
    # describe_pet(pet_name='harry', animal_type='hamster')

    # musician = get_formatted_name('jimi', 'hendrix')
    # print(musician)
    # musician = get_formatted_name('john', 'hooker', 'lee')
    # print(musician)

    # musician = build_person('jimi', 'hendrix', age=28)
    # print(musician['first'].title() + " " + \
    #       musician['last'].title() + \
    #       " age: " + \
    #       str(musician['age']))

    greetings()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # test_func()

    # create a list
    usernames = ['hannah', 'ty', 'margot']
    # call function
    greet_users(usernames)
