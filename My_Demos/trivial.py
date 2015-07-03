x = 200
if x>100:
    print 'x is big'
print id(x)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print fact(0)