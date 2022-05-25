import time, random, math
    
print("hello")

# functions
def findDupes(array):
    array.sort()
    print("sorted list:", array, "\n\n")
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            print(array[i])

# constants
pi = 3.14159265359

while True: # loop the program after an operation has been calculated
  
    print("select one")
    print("1 - addition")
    print("2 - subtraction")
    print("3 - multiplication")
    print("4 - division")
    print("5 - percentage")
    print("6 - circle area calc")
    print("7 - duplicate finder")

    operation = int(input("type your selection here: ")) # the user types the number next to the operation they want

    if operation < 5: # queries the user for 2 numbers if the selection is 1-4 (inclusive)
        num1 = float(input("enter the first number: "))
        num2 = float(input("enter the second number: "))

        if operation == 1: # addition
            print(f"the sum of {num1} and {num2} is {num1 + num2}")

        if operation == 2: # subtraction
            print(f"{num1} subtracted by {num2} is {num1 - num2}")

        if operation == 3: # multiplication
            print(f"the product of {num1} and {num2} is {num1 * num2}")
        
        if operation == 4: # division
            print(f"{num1} divided by {num2} is {num1 / num2}")

    if operation == 5: # percentage calculator 
        percNum = float(input("enter the number: ")) # the number to take the percentage of
        percentage = float(input("what percentage of the number do you want to get? "))

        percProduct = percNum * percentage / 100 # divides the user input by 100 so it can be multiplied with percNum for the result

        if percentage >= 100: # displays the result differently if percentage is above 100
            print(f"{percNum} multiplied by {percentage / 100} = {percProduct}")
        
        if percentage <= 100: # displays the result differently if percentage is below 100
            print(f"{percentage}% of {percNum} is {percProduct}")

    if operation == 6: # circle area calclulator
        radius = float(input("enter the radius: "))
        circleArea = (radius * radius) * pi
        print(f"the area of a circle with a radius of {radius} is {circleArea}")

    if operation == 7: # duplicate finder
        dupecalcString = input('enter the array of numbers: ')
        dupecalcList = dupecalcString.split() # splits the inputted string into an array
        print('list:', dupecalcList) # prints the list for debugging/feedback
        for i in range(len(dupecalcList)): 
            dupecalcList[i] = int(dupecalcList[i]) # turns each element in the list to an integer so the function can process it
        
        findDupes(dupecalcList)

    
        
    # end of program, loops from here
    input("press enter to continue...")

    print()
    print()