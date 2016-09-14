__author__ = 'kathiria'

class A(object):
        def spam(self):
            print('A.spam')

class B(A):
        def spam(self):
            print('B.spam')
            super(B, self).spam()

class C(B):
        def spam(self):
            print('C.spam')
            super(C, self).spam()


print(C.__mro__)
c = C()
c.spam()


class W(object):
        def spam(self):
            print('W.spam')

class X(W):
        def spam(self):
            print('X.spam')
            super(X, self).spam()

class Y(W):
        def spam(self):
            print('Y.spam')
            super(Y, self).spam()

class Z(W):
        def spam(self):
            print('Z.spam')
            super(Z, self).spam()

class M(X,Y,Z):
        pass

print(M.__mro__)
m = M()
print(m.spam())

class N(Z,Y,X):
        pass
