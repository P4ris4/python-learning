#get a number from the use through input method
#the purpose of this assignment is to see if a number is odd or even 
number_to_check = int(input("Please enter any whole number that you want me to check: "))
#check for even or odd through modulor 
if number_to_check % 2 == 0:
    print("The number you inputed is even.")
else:
    print("The number you inputed is odd.")
