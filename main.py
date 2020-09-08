import functions


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # test_func()

    ## greet_users
    # usernames = ['hannah', 'ty', 'margot']
    # functions.greet_users(usernames)

    ## modifying list via functions
    # unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    # completed_models = []
    # functions.print_models(unprinted_designs, completed_models)
    # functions.how_completed_models(completed_models)

    ## modifying list via functions
    # unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    # completed_models = []
    # functions.print_models(unprinted_designs, completed_models)
    # functions.show_completed_models(completed_models)

    ## passing a copy of the list
    # unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    # completed_models = []
    # functions.print_models(unprinted_designs[:], completed_models)
    # functions.show_completed_models(completed_models)
    # print(unprinted_designs)

    ## order of precedence of types of parameters
    # functions.make_pizza(16, 'pepperoni')
    # functions.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    ## dealing with unknown type of arb args
    user_profile = functions.build_profile('albert', 'einstein', location='princeton', field='physics')
    print(user_profile)
