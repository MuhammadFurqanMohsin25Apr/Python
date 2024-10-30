universal_set = set(range(1, 41))
hockey_only = set(range(1, 22))
both = set(range(1, 11))

cricket_only = universal_set.difference(hockey_only, both)

print("students who play only hockey are:", len(hockey_only))
print("students who play both hockey and cricket are:", len(both))
print("students who play only cricket are:", len(cricket_only))
