# 21.Use a dictionary to count the occurrences if each word in the string "hello world hello Python world"
# string="hello world hello Python world"
# words=string.split()
# word_count={}
# for word in words:
#     if word in word_count:
#         word_count[word]=word_count[word]+1
#     else:
#         word_count[word]=1
# print(word_count)

#22. Write a Python program to find the key with the maximum value in the dictionary {'a':10 , 'b':15 , 'c':7}
# max_find_dictionary={'a':10 , 'b':15 , 'c':7}
# print(max(max_find_dictionary,key=max_find_dictionary.get))

#23. Create a dictionary to map numbers 1 to 5 to their squares
# num={1,2,3,4,5}
# num_square={x:x**2 for x in num}
# print(num_square)   

#24. Write a Python program to remove duplicate values from the dictionary
# dict2={'a':10,'b':15, 'd':15}
# unique_dictionary={}
# seen_values=set()
# for key,value in dict2.items():
#     if value not in seen_values:
#         unique_dictionary[key]=value
#         seen_values.add(value)
# print(unique_dictionary)

# 25.Write a Python function that accepts a dictionary and a key, and returns the value 
# associated with the key. If the key doesn’t exist, return "Key not found".

# def dict_value(my_data,key):
#     return my_data[key]

# my_data={"name":"Muhammad Salman","age":30,"qualification":"BS Software Engineering"}
# print(dict_value(my_data,key="name"))

# 26.Given two dictionaries dict1 = {'a': 5, 'b': 10} and dict2 = {'a': 3, 'b': 7}, 
# write a Python program to add the values of matching keys and print the result.

# dict1 = {'a': 5, 'b': 10}
# dict2 = {'a': 3, 'b': 7}
# addition=0
# result_dic={}
# for key1,value1 in dict1.items():
#     for key2,value2 in dict2.items():
#         if key1==key2:
#             addition=addition+dict1[key1]+dict2[key2]
#             result_dic[key1]=addition
#             addition=0
# print("Sum=",result_dic)

# 27.Write a Python program to create a dictionary where the keys are the first n positive integers
# , and the values are their cubes. Take n as user input.

# n=int(input("How many positive integer do you want to enter"))
# result={x:x**3 for x in range(1,n+1)}
# print(result)

# 28.Flatten the following nested dictionary into a single-level dictionary:
#  {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}  
# def flattening_dic_fun(d,outer_key='',sep='_'):
#     flatten_dic={}
#     for key,value in d.items():
#         new_key=f"{outer_key}{sep}{key}" if outer_key else key
#         if isinstance(value,dict):
#             flatten_dic.update(flattening_dic_fun(value,new_key,sep=sep))
#         else:
#             flatten_dic[new_key]=value
#     return flatten_dic

# nested_dic={'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}
# print(flattening_dic_fun(nested_dic))

#29.Write a Python program to split a dictionary into two based on whether the values are odd or even.
# w_dict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
# odd_dict={}
# even_dict={}
# for w_key,w_value in w_dict.items():
#     if w_value%2==0:
#         even_dict[w_key]=w_value
#     else:
#         odd_dict[w_key]=w_value
# print(even_dict)
# print(odd_dict)

# 30.Create a dictionary comprehension to filter out all keys in {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
# where the value is less than 3.
un_comprehense={'a': 1, 'b': 2, 'c': 3, 'd': 4}
comprehense={un_key:un_value for un_key,un_value in un_comprehense.items() if un_value<3}
print(comprehense)