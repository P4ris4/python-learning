#Prompt the user to enter make and model of their car:
make_model_car = input ("Enter the make and model of your car: ")

#Prompt the user to enter the number of miles they've traveled since their last fill up
number_of_mi = int(input("Enter the number of miles you traveled since your last fill up: "))

#Prompt the user to enter the number of gallons it took to fill up
number_of_gal = float(input("Enter the number of gallons of gas it took to fill up this time: "))

#Create a variable called 'mpg' that calculates the miles per gallon
mpg = number_of_mi / number_of_gal

#Create a formatted print statement that rounds appropriately and generates the same output shown above
print (f"You traveled {number_of_mi} miles on {number_of_gal} gallons of gas.")
print (f"Your {make_model_car} averaged {mpg:.1f} miles per gallon.")
