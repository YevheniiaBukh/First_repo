# class A:
#     x = 'a'

# class B(A):
#     pass

# class C(A):
#     ...

# class D(B, C):
#     x = 'd'

# print(B.x)
# print(D.x)
# print(D.__mro__) #mro 3 (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
#mro 2 (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>)