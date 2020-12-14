def task9(x):

    count = 0
    for n in range(x):
        if n % 3 == 0 or n % 5 == 0:
            count += n   
    print(count)
task9(1000)