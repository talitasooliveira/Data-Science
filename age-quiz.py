"""
Input user's age
If the user is under 13, output the message "You qualify for the kiddie discount."
If the user is 21, output the message "Congrats on your 21st!"
For any other age (between 13 and 40 without 21), output the message "Age is but a number."
If the user is 40 or over, output the message "You're over the hill."
If the user is 65 or older, output the message "Enjoy your retirement!"
Assume that the oldest someone can be is 100; if the user enters a higher number, output the message "Sorry, you're dead.".
"""

age = input("Hello, please enter your age: ")
age1 = int(age)
if age1 < 13:
    print("You qualify for the kiddie discount.")
elif age1 == 21:
    print("Congrats on your 21st!")
elif age1 < 40:
    print("Age is but a number.")
elif age1 < 65:
    print("You're over the hill.")
elif age1 < 100:
    print("Enjoy your retirement!")
else:
    print("Sorry, you're dead.")


