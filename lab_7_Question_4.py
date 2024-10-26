empty_tuple = ()
name = input("Enter the name of province of Pakistan: ")

while name != "":
    empty_tuple += (name,)
    if len(empty_tuple) == 4:
        break
    name = input("Enter the name of province of Pakistan: ")

print(empty_tuple)
