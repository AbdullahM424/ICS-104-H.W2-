##
# This program converts an integer number with any base into a base 10 number using for or while loop.
#

# YOUR CODE HERE
# This program converts an integer number with any base into a base 10 number using for or while loop.
#
num = input("Enter a number: ") #asking an input from the user
if num.isdigit() or num[0] == "-": #checking if the input contains digits or the first index is equal to -
    base = input("Base: ") #asking the number of the base 
    if base.isdigit(): #checking if the base is a digit or not
        i = 0 #initializing a value for the loop
        valid = True #setting a condition for the loops
        while valid and i < len(num): #this will run as long as the length of the iteration was greater than the number of iteration
            if num[i] >= base: #if the index of the number was greater than or equal to the number of base, then it will no longer be valid
                valid = False 
                print("The input number is not a legal number of a base", base)
            i = i + 1 #incrementing the loop
        if valid and int(num)>0: #this will check if the input was valid and positive
            count = "" #creating an empty string to use in the output
            result = 0 #initializing a value for the loop
            int_num = int(num) #converting the string value into an integer so it can be used properly
            if int_num > 0: 
                i = len(num)-1 #this will 
                while i >= 0:
                    for j in range(0,len(num)): #setting a loop that will iterate for as many times as the length of the input
                        base_new = int(base)**j #the new base will be the integer raised to the value of j in the previous loop
                        c = "("+num[i]+"X"+str(base_new)+")" #this will produce the desired output
                        count = count+c+"+"
                        v = base_new*int(num[i])
                        result = result+v #the result will be the new base times the integer of the index of the input number
                        i = i-1 #incremnting the loop by -1
                    print("Number in base 10: ")
                    print(count[:-1]+"=",result) #printing the results
        elif valid and int(num)<0: #same steps for negative input values
            num_new = num[1:]
            i = len(num_new)-1
            while i >= 0:
                for j in range(0,len(num_new)):
                    base_new = int(base)**j
                    c = "("+"-"+num_new[i]+"X"+str(base_new)+")"
                    count = count+c+"+"
                    v = base_new*int(num_new[i])*-1
                    result = result+v
                    i = i-1
                print("Number in base 10: ")
                print(count[:-1]+"=", result)
    else: #printing the error messages
        print("Error: the input value is not an integer number")
else:
    print("Error: the input value is not an integer number")
