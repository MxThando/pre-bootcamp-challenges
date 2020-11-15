def task11(word1,word2):
    word1 = [item.lower() for item in word1]
    word2 = [item.lower() for item in word2]
    vowels = ['a', 'e', 'o', 'u']

    for i in word1:
        if i in word2 and vowels:
            print(i)
task11('ThandOu','MapheUo')