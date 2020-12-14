def task10(astring):
    astring = (item.lower() for item in astring)
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in astring:
        if i in vowels:
            print(i)
task10('ThAmayIuoE')