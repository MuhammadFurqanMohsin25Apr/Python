a = int(input("Enter first term: "))
d = int(input("Enter common difference: "))

while True:
    n = int(input("Enter the number of terms: "))
    T = a + (n - 1) * d
    print("The nth term is:", T)
    
    x = input("You want to continue? (yes or no): ")
    if x != "yes":
        break
