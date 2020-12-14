def task11(word1,word2):
    
    word1 = [item.lower() for item in word1]
    word2 = [item.lower() for item in word2]
    
    for i in word1:
        if i in word2:
            print(i)

task11('ThandOu','MapHeUo')