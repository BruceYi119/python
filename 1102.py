# n = int(input('숫자(1-3)'))
# if n == 1:
#     print('안녕')
# elif n == 2:
#     print('안녕' * 2)
# elif n == 3:
#     print('안녕' * 3)
# else:
#     print('메롱')

# n = int(input('숫자='))
# a = list()
# for i in range(n):
#     a.append('안녕')
#
# a = ['안녕' for _ in range(n)]
# print(a)

# b = list()
# for i in range(1, 21):
#     if i % 3 == 0:
#         b.append(i)
# print(b)

# 컴프리핸션:컬렉션을 만드는 한줄짜리 반복문
# c = [i for i in range(1, 21) if i % 3 == 0]
# print(c)

# 튜플은 값변경X tuple()
# 파이썬이 주로 사용한다. 매개변수전달시, 반환값 리턴시
# a = ('감', '사과', '대추')
# print(a)
# for i in enumerate(a):
#     print(i)
# for i, v in enumerate(a):
#     print(i, v)

# a, b, c = 1, 'two', '셋'
# d = 1, 'two', '셋';
# print(d)
# print(d[1])

# a = range(10)
# print(list(a))
# print(tuple(a))
# a = list(range(1, 10, 2))
# print(a)

# 딕션어리{}
f = { 'name': 'kim', 'age': 20, 1004: True }
# print(f, type(f))
# print(f[1004])
# for i in f:
#     print(f[i])
# print(f.values(), f.keys())
# for i in f.items():
#     print(i)
# for i, v in f.items():
#     print(i, v)

a = 'javaqscript'
# for i in a:
#     print(i)
# r = [i for i in a]
# print(r)
d = {}
# for i, v in enumerate(a):
#     d[i] = v
# for i in enumerate(a):
#     d[i[0]] = i[1]
# print(d)

d = {i[0]:i[1] for i in enumerate(a)}
print(d)