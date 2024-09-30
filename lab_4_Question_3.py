p = input("Enter the string: ")
p = p.casefold()  
e = "".join(reversed(p))  

if p == e:
    print("Yes, your string is a palindrome")
else:
    print("Sorry, your string is not a palindrome")
