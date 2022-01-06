import json
from json.decoder import JSONDecodeError


def file_read_all():
    """Displays the entire contents of a file"""

    # read an entire file
    with open('text_files/pi_digits.txt') as file_object:
        contents = file_object.read()
        print(contents.rstrip())


def file_read_line():
    """Displays the contents of a file one line at a time"""

    # read one line at a time
    with open('text_files/pi_digits.txt') as file_object:
        for line in file_object:
            print(line.rstrip())


def file_read_lines():
    """Displays the contents of a file using readlines()"""

    filename = 'text_files/pi_digits.txt'

    with open(filename) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())


def concat_pi():
    """Concat the lines in a file"""

    filename = 'text_files/pi_digits.txt'

    with open(filename) as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    print(pi_string)


def pi_search():
    """Concat the lines in a file"""

    filename = 'text_files/pi_million_digits.txt'

    with open(filename) as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    birthday = input("Enter your birthday (mmddyy): ")
    if birthday in pi_string:
        print("Your birthday appears in first million digits of pi!")
    else:
        print("Your birthday is not in first million digits of pi.")


def write_message():
    filename = 'text_files/programming.txt'

    with open(filename, 'a') as file_object:
        file_object.write("I also love finding meaning in large datasets.\n")
        file_object.write("I love creating apps that can run in a browser.\n")


def zero_division_error():
    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quite")

    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("\nSecond number: ")
        if second_number == 'q':
            break
        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("You can't divide by zero.")
        else:
            print(answer)


def count_words(filename):
    """Count the approx. no. of words in a file"""

    try:
        with open(filename, 'r') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


def json_dump(data, filename):
    with open(filename, 'w') as f_obj:
        json.dump(data, f_obj)


def json_load(filename):
    with open(filename, 'r') as f_obj:
        data = json.load(f_obj)
    return data


def remember_me(username, filename):
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)


def get_stored_username(filename):
    """Get username if exists"""

    # filename = 'text_files/username.json'

    try:
        with open(filename, 'r') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    except JSONDecodeError:
        return None
    else:
        return username


def get_new_username(filename):
    """Prompt for an new username"""

    # filename = 'text_files/username.json'
    username = input("What is your username: ")

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user(filename):
    """Greet the user with username"""

    username = get_stored_username(filename)
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username(filename)
        print("We'll remember you know " + username + "!")


