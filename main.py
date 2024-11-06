# Programmers:  [your names here]
# Course:  CS151, [Instructors Name]
# Due Date: [date assignment is due]
# Lab Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Input Files: [description of the format of the input files you need for this program to work]
import os


# Purpose:
# Parameters:
# Return:
def file_name_choice():
    file_name = input("Enter file name: ")
    while not os.path.isfile(file_name):
        print("Error: File does not exist")
        file_name = input("Enter file name: ")
    return file_name

# Purpose:
# Parameters:
# Return:
def read_file_to_list(file_name):
    fd = open(file_name, "r")
    names = fd.readlines()
    fd.close()
    return names

# Purpose:
# Parameters: read_file_to_list
# Return:
def assign_seats(names):
    table = 1
    seat = 1
    for name in names:
        print(f'Table:{table}, Seat:{seat}, {name}')
        seat += 1
        if seat > 5:
            table += 1
            seat = 1


# Purpose:
# Parameters: read_file_to_list
# Return:
def main():
    file_name = file_name_choice()
    names = read_file_to_list(file_name)
    assign_seats(names)

main()