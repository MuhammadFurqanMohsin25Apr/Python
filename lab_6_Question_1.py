#(a)
sample_list=[2,1,3,5,4,3,8]
print("actual list",sample_list)
#del():
del sample_list[2]
print("list after apllying del fuction on index 2",sample_list)

#(b)
sample_list=[2,1,3,5,4,3,8]
print("actual list",sample_list)
sample_list.remove(2)
print("list after applying remove function",sample_list)

#(c)
sample_list=[2,1,3,5,4,3,8]
print("actual list",sample_list)
sample_list.sort()
print("list after sorting",sample_list)

#(d)
sample_list=[2,1,3,5,4,3,8]
print("actual list",sample_list)
sample_list.insert(2,9)
print("list after inserting 9 on index 2",sample_list)

#(e)
sample_list=[2,1,3,5,4,3,8]
print("actual list",sample_list)
sample_list.pop()
print("list after applying pop function",sample_list)

#(f)
sample_list=[2,1,3,5,4,3,8]
print("actual list",sample_list)
even=[2,4,6,8]
sample_list.extend(even)
print(sample_list)