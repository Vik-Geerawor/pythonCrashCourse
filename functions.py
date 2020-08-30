# Defining a function
def greet_user(username):  # parameter
    """ Display a simple greeting."""
    print("hello " + username)


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age

    return person

def greetings():
    while True:
        print("\nPlease tell me your name. Enter exit to quit")
        f_name = input("First name: ")
        if f_name == 'exit':
            break
        l_name = input("Last name: ")

        formatted_name = get_formatted_name(f_name, l_name)
        print("\nHello, " + formatted_name + "!")
