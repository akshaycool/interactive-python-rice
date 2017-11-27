
def format(t):
    a,b,c,d=0,0,0,0
    
    if(t==0):
        return str(a)+':'+str(b)+str(c)+'.'+str(d)
    d=t%10
    c=((t/10)-(t/600)*60)%10
    b=((t/10)-(t/600)*60)/10
    a=t/600                    
    return str(a)+':'+str(b)+str(c)+'.'+str(d)


print format(0)
print format(7)
print format(17)
print format(60)
print format(63)
print format(214)
print format(599)
print format(600)
print format(602)
print format(667)
print format(699)
print format(700)


print format(999)

print format(1325)
print format(4567)
print format(5999)
print format(6000)
