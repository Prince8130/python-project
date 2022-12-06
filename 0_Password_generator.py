import random
class Password:
    def generateRandomPass(n):
        # the minimum length of the password should be 12
        if n < 12:
            print("Minimum length of password should be 12.")
            return False
        # storing all upper case letters
        uc = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        # storing all lower case letters
        lc = [i for i in "abcdefghijklmnopqrstuvwxyz"]
        # storing all digits
        dg = [i for i in "0123456789"]
        # storing all special characters
        s = [i for i in "@#$%=:?./|~>*()<"]

        # Merging all the characters into a single string
        allChr = uc+lc+dg+s

        # selecting a random digit
        randomDigit = random.choice(dg)
        # selecting a random upper case letter
        randomUpper = random.choice(uc)
        # selecting a random lower case letter
        randomLower = random.choice(lc)
        # selecting a random special character
        randomSymbol = random.choice(s)

        # merging all the random selected letters and storing in our passowrd variable
        password = randomDigit + randomLower + randomSymbol + randomUpper

        # getting n-4 random character from our all character string 
        # (n-4 because we already had our 4 randomly selected character)
        # we will append the password with the random selected characters
        for i in range(n-4):
            password += random.choice(allChr)
        
        # converting the password string into a list so that it can be shuffled
        password = list(password)

        # shuffling the items in the list
        random.shuffle(password)

        # converting the shuffled string back to a string using join function
        password = ''.join(password)

        # printing the password of n length
        print(password)

# take input from the user
n = input("Enter password length: ")

# Looping till user enter exit in the input.
while n.lower() != "exit":
    Password.generateRandomPass(int(n))
    n = input("Enter length of passowrd: ")