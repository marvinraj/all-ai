""" a simple code to perform matrix operations """

import numpy as np


# adds two array
def addition(a,b):
    print(a+b)

# subtracts two array
def subtraction(a,b):
    print(a-b)

# multiply two array
def multiplication(a,b):
    print(a*b)

# determines operation based on user input
def action(a,b, user_action):
    if user_action == "add":
        print(addition(a,b))
    elif user_action == "subtract":
        print(subtraction(a,b))
    elif user_action == "multiply":
        print(multiplication(a,b))

# main function
def main():

    array_one = np.array([[1,2,3],[1,2,3]])
    array_two = np.array([[4,5,6],[7,8,9]])

    user_action = input("would you like to add, subtract or multiply?\n")
    action(array_one, array_two, user_action)

# execute main function if the script is run directly
if __name__ == "__main__":
    main()