def task11(word1,word2):

    word1 = [item.lower() for item in word1]
    word2 = [item.lower() for item in word2]

    store = []

    for i in word1:
        for j in word2:
            if i not in store and i == j:
                store.append(i)
    store = ",".join(store)
    print(f"Common letters {store}")

if __name__ == '__main__':
    task11('ThandOu','MapHeUo')
