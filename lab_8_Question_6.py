dog = set(range(1,39)) | set(range(39,70)) | set(range(70,78)) | set(range(78,84))
cat = set(range(84,138)) | set(range(39,70)) | set(range(70,78)) | set(range(138,148))
fish = set(range(70,78)) | set(range(78,84)) | set(range(138,148)) | set(range(148,154))
others = set(range(154,188))

only_dogs = dog - (cat | fish)
print("people who purchased dog products only", len(only_dogs))

only_cats = cat - (fish | dog)
print("people who purchased cat products only", len(only_cats))

only_fish = fish - (cat | dog)
print("people who purchased fish products only", len(only_fish))

dog_or_fish = set(only_fish | only_dogs)
print("people who purchased dog or fish products only", len(dog_or_fish))

total_purchase = dog | cat | fish | others
print("total purchases", len(total_purchase))
