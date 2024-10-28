friends = {'ali', 'anas', 'wahab', 'shahzeb', 'touseef'}
print("my friends are", friends)

for j in range(2):
    friend_left_ned = input("Enter the name of student who left ned:")
    if friend_left_ned in friends:
        friends.remove(friend_left_ned)
        print("my friends are", friends)
    else:
        print("they are not my friends")
