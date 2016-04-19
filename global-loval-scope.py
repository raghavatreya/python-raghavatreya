x = 6

def example():
    z=3
    print(z)
    global x
    x=x+6
    print(x)

    globalx =x
    print(globalx)
    globalx +=10
    print(globalx)


    #return globalx
    #x = example()
example()

print(example())
