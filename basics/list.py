# a list is array of data, which is ordered, and mutable, meaning it can be changed when any functions are applied to it
#it can be made using square brackets []
my_list = ["Aarush", 16, "Programming"]
unsorted_list = [3,6,2,45,12,67,34,89,6]
#sort

unsorted_list.sort()
sorted_list = unsorted_list
print(sorted_list)
#access a data from a list, a item in a list is stored in order, and has a index, the first item has index 0, the next one has index 1 and so on
name = my_list[0]
age = my_list[1]
interest = my_list[2]

print(f"{name} is {age} years old and like {interest}")

#append

my_list.append("Python") #inserts a new object at last of the list


#insert

my_list.insert(1, "Male") #insets a object ina specific index, and other will be shifted to the left

print(my_list)