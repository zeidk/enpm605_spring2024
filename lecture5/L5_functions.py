# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 47    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# # Define the number for which to calculate the factorial
# number = 5

# # Initialize the factorial result to 1 (the identity value for multiplication)
# factorial = 1

# # Use a for loop to multiply the result by each number from 1 to the specified number
# for i in range(1, number + 1):
#     factorial *= i

# # Print the result
# print(f"The factorial of {number} is {factorial}")


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 49    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# # Function to get dimensions of the rectangle
# def get_dimensions():
#     length = float(input("Enter the length: "))
#     width = float(input("Enter the width: "))
#     return length, width


# # Function to calculate the area of the rectangle
# def calculate_area(length, width):
#     return length * width


# # Function to display the area
# def display_area(area):
#     print(f"The area of the rectangle is: {area}")


# # Main function to orchestrate the procedural steps
# def main():
#     length, width = get_dimensions()
#     area = calculate_area(length, width)
#     display_area(area)


# # Entry point of the program
# if __name__ == "__main__":
#     main()


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 52    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def greet(name):
#     return f"Hello, {name}!"


# say_hello = greet
# print(say_hello("Alice"))  # Hello, Alice!

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 53    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def shout(text):
#     return text.upper() + "!"


# def whisper(text):
#     return text.lower() + "..."


# def greet(style, name):
#     message = f"Hello, {name}"
#     return style(message)


# # Passing the 'shout' and 'whisper' functions as arguments
# print(greet(shout, "Bob"))  # HELLO, BOB!
# print(greet(whisper, "Eve"))  # hello, eve...

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 54    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def make_multiplier(factor):
#     def multiplier(number):
#         return number * factor

#     return multiplier


# # Creating a doubler and tripler function
# doubler = make_multiplier(2)
# tripler = make_multiplier(3)

# print(doubler(5))  # Output: 10
# print(tripler(5))  # Output: 15

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 55    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def add(x, y):
#     return x + y


# def subtract(x, y):
#     return x - y


# operations = [add, subtract]
# print(operations[0](5, 3))  # Output: 8 (addition)
# print(operations[1](5, 3))  # Output: 2 (subtraction)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 58    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# add = lambda x, y: x + y
# print(add(1, 3))  # 4

# double = lambda x: x * 2
# print(double(2))  # 4

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 59    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# import dis

# # lambda expression
# dis.dis(lambda x: x * 2)

# print("-------------------")

# # standard function
# def double(x):
#     return x * 2


# dis.dis(double)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 60    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# print((lambda x: x + 1)(2))  # 3
# print((lambda x: assert x == 2)(2))  # SyntaxError
# (lambda x: int: x + 1)(2)
# print((lambda x: 
#     x + 1)(2))
# print((lambda x, y, z: x + y + z)(1, 2, 3))  # Positional arguments
# print((lambda x, y, z=3: x + y + z)(1, 2))  # Default arguments
# print((lambda x, y, z: x + y + z)(1, z=2, y=2))  # Keyword arguments
# print((lambda *args: sum(args))(1, 2, 3))  # lambda with *args
# print((lambda **kwargs: kwargs)(a=1, b=2, c=3))  # lambda with **kwargs

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 62    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)  # [1, 4, 9, 16, 25]

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 63    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# numbers = [1, 2, 3, 4, 5]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # [2, 4]

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 64    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# pairs = [(1, "b"), (3, "a"), (2, "c")]
# sorted_pairs = sorted(pairs, key=lambda x: x[1])
# print(sorted_pairs)  # [(3, 'a'), (1, 'b'), (2, 'c')]

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 65    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# total = reduce(lambda x, y: x + y, numbers)  # ((((1+2)+3)+4)+5)
# print(total)  # 15

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 68    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# import tkinter as tk


# # Function to handle button click
# def button_click():
#     print("Button clicked!")


# # Create a Tkinter window
# window = tk.Tk()
# window.title("Button Click Example")

# # Create a button widget with a lambda expression as its command
# button = tk.Button(window, text="Click Me", command=lambda: button_click())
# button.pack()

# # Run the Tkinter event loop
# window.mainloop()