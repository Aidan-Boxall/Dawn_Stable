import copy

def addone(x):
    x = x + 1
    return x
a = 100
a = addone(a)
a = [a]
x = list(a)
a[0] = 0


def additem(l):
    l.append(99)


l = [1, 2, 3, 4, 5]
additem(l)


class super_list(list):
    def __init__(self,l):
        self.list = l
        self.cat = 'meow'
    def additem(self):
        self.list.append(99)
    def __str__(self):
        return str(self.list) + str(self.cat)


x = super_list(l)
print x
x.additem()
print x.list