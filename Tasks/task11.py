list1 = list(str(input("Please type your first word: ", )))
list2 = list(str(input("Please type in your second word: ", )))

list1 = [item.lower() for item in list1]
list2 = [item.lower() for item in list2]

for i in list1:
    if i in list2:
        print(i)