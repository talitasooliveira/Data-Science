#Task 8
#This is a code to output the star pattern shown in the task, using an if-else statement in combination with a single for loop
#Definition of star
test="*"
j=1
#Total of lines
for i in range (1,10):
    #Increase by if condition
    if i<6:
       j=i
       print(j*test)
    #Decrease by else condition
    else:
        j=j-1
        print(j*test)
        