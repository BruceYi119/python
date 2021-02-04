# 함수정의
# def 함수명(매개변수):
#     내용
# 함수호출
# 함수명(매개변수)

def test(name):
    return name

hi = test(list({'s','b','c',5}))

print(hi)

def test1():
    a = '1'
    b = 'b'
    c = 'C'
    return a,b,c

a,b,c = test1()
print(a,b,c)

def test2():
    a = '1'
    b = 'b'
    c = 'C'
    return (a,b,c)

aa = test2()
print(aa)
a1,a2,a3 = test2()
print(a1,a2,a3)

def test3():
    a = '1'
    b = 'b'
    c = {'c': 'C', 'd': 'd'}
    return {'a': a,'b': b,'c': c}

bb = test3()
print(bb)
bb1,bb2,bb3 = test3()
print(bb1,bb2,bb3)

def test4(x,y):
    print('test4()')

test4(4,5)

def test5(x=1,y=2,z=3):
    print(x,y,z)

test5(z=66)

def test6(*args):
    return args

a = test6('a',123,'★')
print(a, a[0], a[1], a[2])

def test7(**args):
    return args

a = test7(name='dooly',a='test',b='456')
print(a)