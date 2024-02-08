#Task 5 - Capstone Project
import math

# The user should be allowed to choose which calculation they want to do.
print("Hello user! This is a financial calculator: \n investment - to calculate the amount of interest you'll earn on your investment \n bond - to calculate the amount you'll have to pay on a home loan")
type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Recognised as valid entries
choose = type.lower()

if choose == "investment":
    P = float(input("Please enter the amount of money that they are depositing: ")) #amount
    rate = float(input("Please enter the interest rate (as a percentage) - only the number: ")) #rate
    t = float(input("Please enter the number of years they plan on investing: ")) #years
    # Ask the user to input if they want “simple” or “compound” interest:
    interest = input("Enter wich type of interest do you want “simple” or “compound”: ")
    r = rate / 100
    interest1 = interest.lower()
    # Simple:
    if interest1 == "simple":
        A = P *(1 + r*t)
        A = round(A,2)
    # Compound:
    elif interest1 == "compound":
        A = P * math.pow((1+r),t)
        A = round(A,2)
    print(A)
elif choose == "bond":
    P = float(input("Please enter the present value of the house: "))
    rate = float(input("Please enter the interest rate (as a percentage) - only the number: "))
    n = float(input("Please enter the number of months they plan to take to repay the bond: "))
    i = rate / 100
    repayment = (i * P)/(1 - (1 + i)**(-n))
    repayment = round(repayment,2)
    print(repayment)
# If the user doesn’t type in a valid input, show an appropriate error message.
else: 
    print("It's not a valid option.")



                     