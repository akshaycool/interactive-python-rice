class Desc(object):
    "A descriptor example that just demonstrates the protocol"
    
    def __get__(self, obj, cls=None): 
        pass

    def __set__(self, obj, val): 
        pass

    def __delete__(self, obj): 
        pass


class C(object):
    "A class with a single descriptor"
    d = Desc() 
    
cobj = C()

print C.__dict__
x = cobj.d 
print x
cobj.d = "setting a value"  
cobj.__dict__['d'] = "try to force a value" 
x = cobj.d 
print x ,cobj.__dict__['d']
del cobj.d 

x = C.d
print x 
C.d = "setting a value on class"