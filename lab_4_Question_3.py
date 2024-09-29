p = input("Enter the string: ")
p = p.casefold()  # Convert the string to lowercase to handle case-insensitivity
e = "".join(reversed(p))  # Reverse the string

if p == e:
    print("Yes, your string is a palindrome")
else:
    print("Sorry, your string is not a palindrome")
