# Basic Operation
student={"name":"Muhammad Salman","age":30,"grade":"A"}
student["grade"]
student["city"]="New York"
student["age"]=20
del student["city"]
# ------------------------------------------------------
# ------------------------------------------------------
# Iterating through Dicitonaries

for each_key in student.keys():
    print(each_key,end=' ')
for each_value in student.values():
    print(each_value,end=' ')
print()
print("Key-Value Pair")
for each_key,each_value in student.items():
    print(each_key,each_value,end=' ')
print()
# Check if the key grade exists in the student dictionary and print True or False.
print('grade' in student)
# Count the total number of keys in the student dictionary.
key_count=0
for each_key in student.keys():
    key_count=key_count+1
print("Total No of Keys",key_count)