##
# This program checks if input string contain a vanilla array using for/while loop.
#
# YOUR CODE HERE
##
# This program checks if input string contain a vanilla array using for/while loop.
#
valid=0 #initializing a value for the condition
while True: #setting a while loop to run as long as the condition was true
    array=input("Enter the array as string or Empty string to exit: ") #the program will not ask the user for an input unless the condition was true
   
    if array=='': #this condition will check if the array was empty
        break
    if array[0]!='{' or array[-1]!='}': #this will check if two elements of the array are equal or not
        valid=1 #changing the value of the condition after checking the elements
    else:
        if len(array)==2: #if the length of the array was equal to 2, the condition will be set to 1
            valid=1
        for digit in array: #this will extract every element in the array           
            if digit.isdigit(): #checking if the element was a digit or not
                c=digit                
                break
        for digit in array:          
            if digit.isdigit():
                if digit!=c: #this will check if two elements of the array is equal or not so it can display a proper error message
                    valid=1
                    break
    if(valid==0): #if it was equal to zero, this means that it meets the conditions of a valid vanilla array and therefore the program will display that it does
        print("The string contains a valid vanilla array.")
    else: #if it was equal to other value than zero, in this case, one, then it will display an error message telling the user that it does not contain a valid vanilla array
        print("The string does not contain a valid or a vanilla array")
