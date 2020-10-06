class JavaStyle:
    
    ''' A class that utilises "private"
    attributes and Getters and Setters'''

    def __init__(self,x):
        self.x = x

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

JavaStyle_1 = JavaStyle(42)
JavaStyle_2 = JavaStyle(4711)

print(JavaStyle_1.get_x())
print(JavaStyle_2.get_x())


JavaStyle_1.set_x(47)
JavaStyle_1.set_x(JavaStyle_1.get_x()+JavaStyle_2.get_x())

print(JavaStyle_1.get_x())


class PythonicStyle():

    ''' The JavaStyle class refactored in a Pythonic way'''
    
    def __init__(self,x):
        self.x = x


p1 = PythonicStyle(42)
p2 = PythonicStyle(4711)
print(p1.x) # 42

p1.x = 47
p1.x = p1.x + p2.x
print(p1.x) # 4758


class Test():
    ''' Demonstrate the use of Public, "Private" and "Protected" instance variables '''
    def __init__(self):
        self.foo = 10 # Public instance attribute
        self._bar = 20 # "Protected" instance attribute (not enforced)
        self.__baz = 30 # "Private" instance attribute (not enforced)

t = Test()
print(dir(t)) # No __baz but there is a _Test__baz

print(t.foo) # 10
print(t._bar) # 20
print(t.__baz) # AttributeError
# print(t._Test__baz) # 30
# t._Test__baz = 50
# print(t._Test__baz)
# print(t._Test__baz) # 50