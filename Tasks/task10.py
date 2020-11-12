mylist = list(str(input("Pleaase enter the word: ", )))

mylist = (item.lower() for item in mylist)

for i in mylist:
    print(i)