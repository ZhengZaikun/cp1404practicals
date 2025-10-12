"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read the file contents and convert it into a list to output detailed information of the subject"""
    data = load_data(FILENAME)
    print(data)
    display_information(data)


def load_data(filename):
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append(parts)
        print("----------")
    input_file.close()
    return data

def display_information(data):
    """Output detailed information about the subject"""
    for part in data:
        print(f"{part[0]} is taught by {part[1]} and has {part[2]} students")



main()