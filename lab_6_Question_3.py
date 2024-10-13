#(a)
lst=['1','2','3','4','5','6']
b=len(lst)//2
print("the index of the middle term is:",b)

#(b)
lst=['1','2','3','4','5','6']
c=lst[len(lst)//2]
print("the middle element of lst is:",c)

#(c)
lst=['1','2','3','4','5','6']
d=sorted(lst,reverse=True)
print("the lst in decending order is:",d)

#(d)
lst=['1','2','3','4','5','6']
lst.remove('1')
lst.append('1')
print(lst)