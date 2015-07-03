import scisoftpy as dnp
import functions as f

class vector(object):
    def update_q(self):
        self.q = np.quaternion(0.0, self.x, self.y, self.z)

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.update_q()

    def __str__(self):
        return '({0}, {1}, {2})'.format(self.x, self.y, self.z)

    def __getitem__(self, index):
        if index == 0:
            return self.q.x
        elif index == 1:
            return self.q.y
        elif index == 2:
            return self.q.z

    def __setitem__(self, index, set_to):
        set_to = float(set_to)
        if index == 0:
            self.x = set_to
            self.update_q()
        elif index == 1:
            self.y = set_to
            self.update_q()
        elif index == 2:
            self.z = set_to
            self.update_q()

    def __mul__(self, other):
        if isinstance(other, vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, np.quaternion):
            return self.q * other
    def __rmul__(self, other):
        print isinstance(other, np.quaternion)
        if isinstance(other, np.quaternion):
            print 'here'
            return self
        if isinstance(other, int):
            return self
        return 5
class rotator(np.quaternion):
    def __mul__(self,other):
        if isinstance(other, vector):
            return self*other.q
        else:
            return self*other
x = vector(1,2)
q = f.rotation_to_quaternion([0,0,1], 45)
q = rotator(1,2,3,4)
print q
a = np.quaternion(0,2,3,4)
y = np.quaternion(1,3,4,5)
# z = vector()
#z = q*x
print type(q)