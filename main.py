from collections import OrderedDict

import functions as f
import car as c
import files_and_exceptions as fe


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test_func():
    ## greet_users
    # usernames = ['hannah', 'ty', 'margot']
    # f.greet_users(usernames)

    ## modifying list via f
    # unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    # completed_models = []
    # f.print_models(unprinted_designs, completed_models)
    # f.how_completed_models(completed_models)

    ## modifying list via f
    # unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    # completed_models = []
    # f.print_models(unprinted_designs, completed_models)
    # f.show_completed_models(completed_models)

    ## passing a copy of the list
    # unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    # completed_models = []
    # f.print_models(unprinted_designs[:], completed_models)
    # f.show_completed_models(completed_models)
    # print(unprinted_designs)

    ## order of precedence of types of parameters
    # f.make_pizza(16, 'pepperoni')
    # f.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    ## dealing with unknown type of arb args
    user_profile = f.build_profile('albert', 'einstein', location='princeton', field='physics')
    print(user_profile)


def test_class():
    # my_dog = c.Dog('willie', 6)
    # print("My dog's name is " + my_dog.name.title() + ".")
    # print("My dog is " + str(my_dog.age) + " years old.")
    # my_dog.sit()
    # my_dog.roll_over()

    # my_new_car = c.Car('mercedes', 'c-class', 2013)
    # print(my_new_car.get_descriptive_name())
    # my_new_car.odometer_reading = 34
    # my_new_car.update_odometer(-14)
    # my_new_car.read_odometer()

    ## inheritance
    my_tesla = c.ElectricCar('tesla', 'model 3', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()


def test_std_lib():
    favourite_langs = OrderedDict()

    favourite_langs['jen'] = 'python'
    favourite_langs['sarah'] = 'c'
    favourite_langs['edward'] = 'ruby'
    favourite_langs['phil'] = 'python'

    for name, language in favourite_langs.items():
        print(name.title() + "'s favourite language is " \
              + language.title() + ".")


def test_fe():
    # fe.file_reader_all()
    # fe.file_read_line()
    # fe.file_read_lines()
    # fe.concat_pi()
    fe.pi_search()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # test_func()
    # test_class()
    # test_std_lib()

    ## files and exceptions
    test_fe()



