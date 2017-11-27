class GetonlyDesc(object):
    "Another useless descriptor"
    
    def __get__(self, obj, typ=None):
        pass

class C(object):
    "A class with a single descriptor"
    d = GetonlyDesc()
    
cobj = C()

x = cobj.d 
print x
cobj.d = "setting a value" 
x = cobj.d 
print x
del cobj.d 

x = C.d 
C.d = "setting a value on class"
print x