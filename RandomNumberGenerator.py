# RandomNumberGenerator
# The following code will generate a list of random numbers and will do following functions:
# (1) It will ask user to enter the amount of random number from 1-100.
# (2) From the data entered by user it will display total random numbers and their values.
# (3) Then it will calculate the minimum number from the list generated without min function.
# (4) Then it will calculate the maximum number from the list generated without max function.
# (5) Then it will calculate the total sum of all the numbers from the list generated without in-build function.
# (6) Then it will calculate the average of all the numbers from the list genereated without in-build function.


import random
# define the main function in which every function will be stored.
def main():
    numbers = randNum() # Because we want the value of randNum() in other functions.
    minvalue(numbers)
    maxvalue(numbers)
    total(numbers)
    avg(numbers)
# Define a function to generate the random numbers
def randNum():
    # To input the amount of random numbers from 1-100
    count = (int(input('How many random numbers you want in the range of 1 through 100?')))
    number_list=[]
    for i in range(count):
        number_list.append(random.randint(1,100))
    print(number_list)
    print('Total Random numbers to display are ',len(number_list))
    for i in range(len(number_list)):
        print('value for location',i+1, 'is', number_list[i])
    return number_list

# Define a function to calculate the minimum number from the list without in-build min function.
def minvalue (numbers):
   # To avoid using in-build function to calculate the minimum value.
    mini = numbers[0]
    for i in numbers[0:]:
        if i < mini:
            mini = i
    print("The lowest number in the list is:",mini)

# Define a function to calculate the maximum number from the list without using in-build function.
def maxvalue(numbers):
    # To avoid using in-build function to calculate the maximum value.
    maxi = numbers[0]
    for i in numbers[0:]:
        if i > maxi:
            maxi = i
    print("The largest number in the list is:",maxi)    

# Define a function to calculate the sum of all the numbers from the list without using the in0-build functiion.   
def total(numbers):
    # To avoid using the in-build function to calculate the total sum of all the numbers.
    totals = 0
    for i in numbers[0:]:
        totals = totals + i
    print("The total of the numbers in the list is:", totals)

# Define a function to calculate the average of all the numbers from the list without using the in-build function.
def avg(numbers):
    # To avoid using the in-build function to calculate the average of all numbers.
    sum = 0 
    for i in numbers[0:]:
        sum = sum + i
    average = sum / len(numbers)
    print("The average of the numbers in the list is :", average)
    
    
main()
# End of the program.