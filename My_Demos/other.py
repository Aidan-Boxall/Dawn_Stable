x = [[10, 20], (30, 40)]
y = list(x)
x[0]=5
print y
print id(x), id(y)
print id(x[0]),id(y[0])
x = range(20,41)
print x[:-1]