x=str(input("Enter the string to checl wheather its a palindrome or not:"))
y=x.replace(" ","")
if y==y[::-1]:
    print("The entered string is a palindrome")
else:
    print("The entered string is not a palindrome")