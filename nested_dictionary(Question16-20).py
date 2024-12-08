# Nested Dictionary
person={"Name":"John","Age":30,
        "Address":{"Street":"123 Elm St","City":"Boston"}}
person["Address"]["City"]
person["Address"]["Phone"]="123-456-7890"
del person["Address"]["Street"]
del person["Address"]["City"]
for each_key,each_value in person.items():
    print(each_key,each_value)