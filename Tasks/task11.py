def task11(word1,word2):

    word1 = [item.lower() for item in word1]
    word2 = [item.lower() for item in word2]
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in word1:
        if i in word2:
            if i in vowels:
                print(i)

if __name__ == '__main__':
    task11('ThandOu','MapHeUo')
