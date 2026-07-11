 

# # for loops
# fruits = ["apple", "pear", "banana"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# high = 0
# largest = 199
# top = [185, 171, 184, 199]
# good = [149, 142, 120, 150]
# bad = [24, 59, 68, 78, 65, 89, 86]
# student_scores = [top, good, bad]

# for score in student_scores:
#     print(score)
# for topscore in top:
#     print(topscore)
#     if topscore >= largest:
#         print(f"This is the highest score: {largest}")

# high = 0
# largest = 199
# top = [185, 171, 184, 199]
# good = [149, 142, 120, 150]
# bad = [24, 59, 68, 78, 65, 89, 86]
# student_scores = [185, 171, 184, 199,149, 142, 120, 150, 24, 59, 68, 78, 65, 89, 86]

# for score in student_scores:
#     if score > high:    
#         high = score    
# print(f"The highest score in the class is: {high}")

#the gaussian sum formula or the gauss challenge

# total = 0
# for number in range(1, 101):
#     if number >= 1:
#        total = (total + number)
# print(total)

# total = 0
# for number in range(1, 101, 50):
#     total += number
# print(total)


# Your program should print each number from 1 to 100 in turn and include number 100.



# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".



# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`



# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:        print(number)


#password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))      
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))  
random_letters = random.choices(letters, k=nr_letters)
random_numbers = random.choices(numbers, k=nr_numbers)
random_symbols = random.choices(symbols, k=nr_symbols)
password_list = random_letters + random_numbers + random_symbols
random.shuffle(password_list)
password = ''.join(password_list)
print(f"Your generated password is: {password}")

