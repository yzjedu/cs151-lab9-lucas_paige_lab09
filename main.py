# Programmers: Lucas Podowski, Paige Ronan
# Course:  CS151, Dr. Z
# Due Date: 11/13/2024
# Lab Assignment:  9
# Problem Statement:  * Create a program to read in all the attendees and then output the seat assignments.
# Data In: file name
# Data Out: the table and seat each person in the list will sit
# Credits: Dr. Z for teaching us the code
# Input Files: .txt files
import os


# Purpose: Ask the user what file they want to choose.
# Parameters: none
# Return: filename
def file_name_choice():
    file_name = input("Enter the file name for the guest list: ")
    while not os.path.isfile(file_name): # Checks to make sure filename exists
        print("Error: File does not exist")
        file_name = input("Renter the file name for the guest list: ")
    return file_name

# Purpose: Read the first file to a list
# Parameters: filename
# Return: names
def read_file_to_list(file_name):
    fd = open(file_name, "r") # Opens file for reading
    names = fd.readlines()
    fd.close()
    return names

# Purpose: Assign seats to the names
# Parameters: names
# Return: none
def assign_seats(names):
    table = 1
    seat = 1
    for name in names:
        print(f'Table:{table}, Seat:{seat}, {name}')
        seat += 1
        if seat > 5:
            table += 1
            seat = 1


# Purpose: Main loop to execute the code
# Parameters: none
# Return: none
def main():
    print("This program will ask you which guest list file you want to use.\n"
          "Each name in that file will then be assigned to  one of five seats at a specific table.")
    file_name = file_name_choice()
    names = read_file_to_list(file_name)
    assign_seats(names)

main()