#Task 4

"""Program that determines the award a person competing in a triathlon will receive
The program should read in the times (in minutes) for all three events of a triathlon, namely swimming, cycling, and running, and then calculate and display the total time taken to complete the triathlon
The award a participant receives is based on the total time taken to complete the triathlon. The qualifying time for awards is 100 minutes. 
Display the award that the participant will receive based on the following criteria:
0-100 minutes: Provincial Colours
101 - 105 minutes: Provincial Half Colours
106 - 110 minutes: Provincial Scroll
111+ minutes: No award"""

print("Hello, I'll help you to find which award you'll receive!")
time_swimming = int(input("How was your time (in minutes) for swimming? "))
time_cycling = int(input("How was your time (in minutes) for cycling? "))
time_running = int(input("How was your time (in minutes) for running? "))

time_total = time_cycling + time_running + time_swimming
print("Your time total is " + str(time_total) + ".")

if time_total <= 100:
    print("Your award is: Provincial Colours!")
elif time_total <= 105:
    print("Your award is: Provincial Half Colours!")
elif time_total <= 110:
    print("Your award is: Provincial Scroll!")
else:
    print("Sorry, you didn't win an award.")
