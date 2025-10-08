def is_palindrome(s: str):
    s = s.replace(" ", "").lower() #it's like cleaning the data enteres and handling the cases capital words empty spaces etc. 
    return s==s[::-1] #literally sending the boolean value using the codition itself and also reverseing the string in the same line 

s_string = input ("Enter the string to check it's palindromity : ")

b = is_palindrome(s_string)
if b == True:
    print("is palindrom")
elif b == False: 
    print("isn't palindrome")

