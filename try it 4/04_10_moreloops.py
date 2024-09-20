cubes = [i ** 3 for i in range(1, 11)]

print(cubes)
print("The first three items in the list are:", cubes[:3])
middle_index = len(cubes) // 2 
print("Three items from the middle of the list are:", cubes[middle_index-1:middle_index+2])

print("The last three items in the list are:", cubes[-3:])