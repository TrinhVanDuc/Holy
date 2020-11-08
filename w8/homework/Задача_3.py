# map(function, iterable)
numbers = [-2, -1, 0, 1, 2]
abs_values = list(map(abs, numbers))
print(*abs_values)

# zip
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(list(zipped))

# filter
aquarium_tanks = [11, False, 18, 21, "", 12, 34, 0, [], {}]
filtered_tanks = filter(None, aquarium_tanks)
print(list(filtered_tanks))

# enumerate
animals = ['cat','dog','buffalo','pig']
enumerate_animals = enumerate(animals)
print(list(enumerate_animals))

