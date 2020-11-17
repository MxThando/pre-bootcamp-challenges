def task5(x,y,z):
    #sp is semiperimeter
    sp = 0.5*(x + y + z)

    area = (sp * (sp-x) * (sp-y) * (sp-z))**0.5

    return area

task5(3,4,5)
