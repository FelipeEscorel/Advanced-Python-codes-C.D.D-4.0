def piramide(num):
    for a in range (1, num+1):
        for b in range (1, a+1):
            print(a, end = " ")
        print()

def piramide2(num):
    for a in range(1, num+1):
        for b in range(1, a+1):
            print(b, end = " ")
        print()
