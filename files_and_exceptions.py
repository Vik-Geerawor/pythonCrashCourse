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