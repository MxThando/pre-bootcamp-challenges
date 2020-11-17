def task9(x):

    for n in range(x):
        if n % 3 == 0 or n % 5 == 0:
            x += n   
    return x
task9(1000)