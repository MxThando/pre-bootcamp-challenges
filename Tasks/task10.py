mylist = list(str(input("Pleaase enter the word: ", )))

mylist = (item.lower() for item in mylist)
vowels = ['a', 'e', 'o', 'u']

for i in mylist:
    if i in vowels:
        print(i)