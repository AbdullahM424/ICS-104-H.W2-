##
# This program reads some text from the user and counts each letter regardless of its case(upper or lower).
#
#

# YOUR CODE HERE
##
# This program reads some text from the user and counts each letter regardless of its case(upper or lower).
#
#

text = input("Enter text: ") #taking the input from the user
text = text.lower() #converting the text into lowercase so that the program validate both lowercase and uppercase inputs
letters = "" #saving the letters of the given text
valid = False #if it was not valid, then there are letters in the text

if text != "" and not text.isspace(): #if the given input was not empty nor it did include a space, then it is valid
    for letter in text: #this for loop will iterate through each element in the input
        if letter.isalpha(): #checking if the element is a alphabetic
            if letter not in letters: #to check other letters in the given input
                letters = letters + letter + ":" + (str(text.count(letter))) + "," #this will create a list of letters with the numbers of reoccurences of each letter in the given text
                valid = True #setting the condition to true after executing the desired operations on the letters only
    if valid == False: #if the text was not valid, this means that it contains either a space or it does not contain any letter
        print("your text does not contain any letter")
    elif valid == True: #if the text was valid, the program will proceed to give the desired output
        length=len(letters) #this will return the length of the letters set so it can be used in slicing later on 
        letters = letters[:length-1] #slicing through the set starting from the first to the last letter
        letters = "["+letters+"]" #setting the output inside closed brackets as given in the sample output
        print("The count of letters in text is: ", letters) #printing each letter with the number of its reoccurences
else :
    print("your text does not contain any letter")
