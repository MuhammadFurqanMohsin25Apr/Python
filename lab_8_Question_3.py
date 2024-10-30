best_dishes = set()
best_dishes.add('Biryani')
best_dishes.add('Pulao')
best_dishes.add('Karahi')
best_dishes.add('Qorma')
best_dishes.add('Beef Biryani')

print("best dishes")
print(best_dishes)

n = len(best_dishes)
for i in range(n):
    pop = best_dishes.pop()
print("after applying pop")
print(best_dishes)
