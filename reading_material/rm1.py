# --------------------------------
# Reading Material
# --------------------------------


# # --- SLIDE 6 --- #
# x = 10
# if x > 15:
#     print("x is greater than 15")
# elif x > 5:
#     print("x is greater than 5 but not greater than 15")

# # --- SLIDE 7 --- #
# x = 10
# if x > 15:
#     print("x is greater than 15")
# elif x > 5:
#     print("x is greater than 5 but not greater than 15")

# # --- SLIDE 8 --- #
# x = 3
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is 5 or less")

# # --- SLIDE 9 --- #
# x = 20
# if x > 15:
#     print("x is greater than 15")
# elif x > 10:
#     print("x is greater than 10 but not greater than 15")
# else:
#     print("x is 10 or less")

# # --- SLIDE 10 --- #
# x = 5
# if x > 3:
#     print("x is greater than 3")

# if x >= 5:
#     print("x is also at least 5")
# else:
#     print("x is less than 5")

# # --- SLIDE 11 --- #
# x = 7
# if x > 5 and x < 10:
#     print("x is greater than 5 and less than 10")

# if not x == 7:
#     print("x is not equal to 7")
# else:
#     print("x is equal to 7")

# # --- SLIDE 14 --- #
# fruits = ['apple', 'banana', 'cherry']

# for fruit in fruits:
#     print(fruit)

# # --- SLIDE 15 --- #
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# # --- SLIDE 17 --- #
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num == 3:
#         break  # Exit the loop when num is 3
#     print(num)

# # --- SLIDE 18 --- #
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num == 3:
#         continue  # Skip the rest of the loop for num == 3
#     print(num)

# # --- SLIDE 19-1 --- #
# numbers = [1, 2, 4, 5]
# for num in numbers:
#     if num == 3:
#         break
# else:
#     print("Number 3 not found in list.")

# # --- SLIDE 19-2 --- #
# count = 1
# while count < 4:
#     print(count)
#     count += 1
# else:
#     print("Count reached", count)

# # --- SLIDE 22 --- #
# try:
#     # Code block where exceptions can occur
#     result = 10 / 0
# except ZeroDivisionError:
#     # Handle the exception
#     print("Cannot divide by zero!")

# # --- SLIDE 23 --- #
# try:
#     # Code that can raise multiple exceptions
#     x = int(input("Enter a number: "))
#     result = 10 / x
# except (ValueError, ZeroDivisionError) as e:
#     # Handle the exceptions
#     print(f"An error occurred: {e}")

# # --- SLIDE 24 --- #
# try:
#     print("Trying to execute code")
#     # No exceptions raised here
# except Exception as e:
#     print(f"An error occurred: {e}")
# else:
#     print("Executed successfully without errors.")

# # --- SLIDE 25 --- #
# try:
#     file = open("example.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found.")
#     file = None  # Explicitly set file to None to indicate it wasn't opened
# finally:
#     if file is not None:
#         file.close()
#     print("File closed.")

# # --- SLIDE 26 --- #
# def set_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     print(f"Age set to {age}")


# try:
#     set_age(-1)
# except ValueError as e:
#     print(e)
