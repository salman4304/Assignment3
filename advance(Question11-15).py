# Advance Dictionary Usage
# 11.Merge the following two dictionaries and print the result
dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
dict1.update(dict2)
print(dict1)

# 12.Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
tuple_list=[('name', 'Alice'), ('age', 25), ('city', 'Paris')]
dictionary=dict(tuple_list)
print(dictionary)

# 13.Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.
dict1={'z': 1, 'a': 2, 'c': 3}
# by default sort in ascending order
sorted_dict=dict(sorted(dict1.items()))  
print(sorted_dict)

# 14. Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.
dic={'a': 1, 'b': 2, 'c': 3}
reverse_dict={each_value:each_key for each_key,each_value in dic.items()}
print(reverse_dict)

#15.Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).
dicionary1={"name":"salman","city":"Faisalabad"}
dictionary2={"name":"salman","city":"Faisalabad"}
status=dicionary1==dictionary2
if status==True:
    print("Dictionaries are identical")
else:
    print("Dictionaries are not identical")
