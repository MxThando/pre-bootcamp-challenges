def task5(x,y,z):

    semiperimeter = 0.5*(x + y + z)

    area = (semiperimeter * (semiperimeter-x) * (semiperimeter-y) * (semiperimeter-z))**0.5

    return area

task5(3,4,5)
