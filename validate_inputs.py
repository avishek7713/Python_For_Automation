import pyinputplus as pyip

print("\nEXAMPLE 1")

result = pyip.inputInt("Enter the number of shopping bags you will need for your items: ", min = 0) # taking in input as integer and minimum = 0

print("\nYou will use", result, "store bags.")

print("\nEXAMPLE 2")

result = pyip.inputMenu(["red", "blue", "green"], lettered= True, numbered= False)
 
print("\nYou have choosen a ", result, " marker.")

print("\nEXAMPLE 3")

result = pyip.inputEmail("Enter your email address:")

print("\nThe email you entered: ", result)