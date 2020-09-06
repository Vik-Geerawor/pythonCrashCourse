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
        if l_name == 'exit':
            break

        formatted_name = get_formatted_name(f_name, l_name)
        print("\nHello, " + formatted_name + "!")


## greet_users
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


def print_models(unprinted_designs, completed_models):
    """"Print each design and then move it to completed_models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate printing
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all printed models"""
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)


def print_models(unprinted_designs, completed_models):
    """"Print each design and then move it to completed_models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate printing
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all printed models"""
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)