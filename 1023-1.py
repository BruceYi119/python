# 파이썬에 모든 것은 객체
# 변수 앞에 아무것도 없음
# 문자의 끝에 ; 없음
# 따옴표 '',""
# 문장의 세로줄을 맞추어야 함
# self는 자바의 this

# a = 3
# print(a)
#
# a = 'adsasdf'
# print(a)
#
# a = 0.1231231243
# print(a)
#
# a = True
# print(a)
#
# a = False
# print(a)
# print("a의값은",a,"그럼이만")
# print("a의값은", a, "그럼이만", sep='')
# print("a의값은", a, "그럼이만", sep='', end='')
# print("새로운 줄")

# print('-'*30)
# a = 30
# b = 5
# c = 'machin'
# print(a + b)
# print(type(a))
# print(type(c))
#
# 형변환
# print('a의 값은=' + str(a))

# a = 7
# b = 99
# print(a, b)
#
# a,b = b,a;
# print(a, b)
#
# a, b, c, d = 5, 6, True, '8'
# print(a, b, c, d)
# print(type(a), type(b), type(c),type(d))
#
# print(bool(0))
# print(int(d))

# 연산자
# a = 3
# b = 99
# print("a + b", a + b)
# print("a - b", a - b)
# print("a * b", a * b)
# print("a ** b", a ** b)     #제곱
# print("a / b", a / b)
# print("a // b", a // b)     #몫
# print("a % b", a % b)       #나머지

# age = 20
# b1 = age<10
# b2 = age>20
#
# print(age, b1, b2)
# print(10<=age<=30)

#인덱스
# [시작인덱스:끝인덱스]   시작인덱스<=x<끝인덱스
# a = '123456789'
# print(a[3])
# print(a[-3])
# print(a[3:7])
# print(a[3:-3])
# print(a[:-3])
# print(a[3:])
# print(a[:])
#
# a = 'python'
# print(a[:1] + 'y' + a[2:])
# print(a[2:-1])

# 문자열 : '..',"..",''' ...''',"""..."""
# a='문자열 표현방"법 @123!'
# print(a)
# a='문자열 표현방\'법 @123!'
# print(a)
# a='''IDLE로 파이썬 프로그램 작성하기

# 포멧팅
a = 10
b = 20
c = 'green'
# 2버전
# print('[%s + $s = %s]'%(a, b, c))
# print('[%d + $d = %d %%]'%(a, b, c))
# %s 문자열, $d 정수, $s 실수, $o 8진수, %x 16진수

# 3버전
print('{} + {} = {}'.format(a,b,c))

a = '198263951286398123981236'
print(a.count('6'))
# 맨처음찾은 인덱스 반환 없을시 -1
print(a.find('0'))
print(a.find('6'))
# 맨처음찾은 인덱스 반환 없을시
print(a.index('6'))