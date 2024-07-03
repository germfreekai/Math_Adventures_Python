#! /usr/bin/python3

def factors(num):
    res = []
    for i in range(1, num + 1):
        if not num % i:
            res.append(i)
    return res
def gcf(n1, n2):
    f1 = factors(n1)
    f2 = factors(n2)
    
    res = [x for x in f1 if x in f2]
    return res.pop()

print(gcf(150,138))
