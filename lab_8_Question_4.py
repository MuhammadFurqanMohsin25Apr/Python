items = {'biscuits', 'candies', 'ice cream', 'popcorns', 'plain cake', 'chocolate'}
d1 = {}
price = []
total_amount = 0
n = len(items)

for i in range(n):
    a = items.pop()
    print("Enter the price for", a, ":")
    d1[a] = int(input())

for j in d1.values():
    price.append(j)
    total_amount += j

for x, y in d1.items():
    print(x, ":", y)

print("Total amount:", total_amount)
print("The maximum price:", max(price))
print("The minimum price:", min(price))
