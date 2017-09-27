#!/usr/bin/python
print('hello World!')
x = 1
if x == 1:
  print('x is 1')
else:
  print('x is not 1') 

var1 = 5
var2 = 'hello'
var3 = None
var4 = False

if var1:
    print 'var1 exists and it\'s value is '
    print var1
else:
    print 'var1 does not exist'

if var2:
    print 'var2 exists and it\'s value is '
    print var2
else:
    print 'var2 does not exist'


if var3:
    print 'var3 exists and it\'s value is '
    print var3
else:
    print 'var3 does not exist'

if var4:
    print 'var4 exists and it\'s value is '
    print var4
else:
    print 'var4 does not exist'
    
print "bigger" if var1 > var2 else "smaller"

students = ['one','two','three']
print students[1]
students.append('four')
print students[3]
