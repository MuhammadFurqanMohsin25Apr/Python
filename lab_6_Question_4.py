monthsL = ['Jan', 'Feb', 'Mar', 'May']
# (a) 
monthsL.insert(3, 'Apr')
print(monthsL)

# (b) 
monthsL.append('Jun')
print(monthsL)

# (c) 
monthsL.pop()
print(monthsL)

# (d) 
monthsL.remove('Feb')
print(monthsL)

# (e) 
monthsL.reverse()
print(monthsL)

# (f) 
monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsL.sort()
print(monthsL)


monthsT = ('Jan', 'Feb', 'Mar', 'May')

# (a) 
x = list(monthsT)
x.insert(3, 'Apr')
monthsT = tuple(x)
print(monthsT)

# (b) 
x = list(monthsT)
x.append('Jun')
monthsT = tuple(x)
print(monthsT)

# (c) 
x = list(monthsT)
x.pop()
monthsT = tuple(x)
print(monthsT)

# (d)
x = list(monthsT)
x.remove('Feb')
monthsT = tuple(x)
print(monthsT)

# (e) 
x = list(monthsT)  
x.reverse() 
monthsT = tuple(x) 
print(monthsT) 

# (f)
x = list(monthsT)
x.sort()
monthsT = tuple(x) 
print(monthsT)  
