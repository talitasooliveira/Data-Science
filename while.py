#Task 7
list_input=[]
#A program that continually asks the user to enter a number.
user_input=int(input("Enter a number: "))
#When the user enters “-1”, the program should stop requesting the user to enter a number
while user_input!=-1:
    list_input.append(user_input)
    user_input=int(input("Enter a number: "))
    sum_list=sum(list_input)
#The program must then calculate the average of the numbers entered,excluding the -1.
    average_list=sum_list/len(list_input)
print("The numbers entered are " + str(list_input))
print("The average is " + str(average_list))