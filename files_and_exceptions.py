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


def file_not_found():
    filename = 'text_files/alice.txt'

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



