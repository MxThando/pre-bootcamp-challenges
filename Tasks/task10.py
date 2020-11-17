def task10(alist):

    alist = (item.lower() for item in alist)
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in alist:
            if i in vowels:
                print(i)
task10('ThAmayIuoE')