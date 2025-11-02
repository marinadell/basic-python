# C.1. Implicit Type Conversion
print(2 + 10/5)
# 2 + 10 / 5
# 2 + 2
# 4.0
# print("2" + 2)
# # can not concatenate string w/ integer 

a = 3
print(a)
# print 3
a = 5 + 6 / 2
print(a)
# print 9
a = 5 + 6 % 2
print(a)
# print 5
a = "Once upon a time"
print(a)
# print "Once upon a time"

# C.2. Explicit Type Conversion
print(int(3.5))
# 3
print(int('34'))
# 34
print(float(3))
# 3
print(str(3) + str(5))
# 35
print(str(14) + '6')
# 146
# print(str(14) + 6)
# will error because you can not concatenate string w/ integer 
# print(int('14') + '6')
# will error because you can not concatenate string w/ integer 
print(int('14') + 6)
# 20
print(float(3) + int(3.5))
# 6.0
# print(str(3) * 3)
# will error can not multiple with string
print(int('3') * 3)
# 9
