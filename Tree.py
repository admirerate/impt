import turtle as t

def main():
    treesize=input("Size :")
    t.speed(0)
    t.seth(90)
    t.fd(treesize)
    vee(treesize*0.75)

def vee(length):
    for i in range(length>10):
        t.lt(50)
        t.fd(length)
        vee(length*0.75)
        t.bk(length)
        t.rt(100)
        t.fd(length)
        vee(length*0.75)
        t.bk(length)
        t.lt(50)

def vee_old(length):
    t.lt(50)
    t.fd(length)
    t.bk(length)
    t.rt(100)
    t.bk(length)
    t.lt(50)

if __name__ == '__main__':
    main()
