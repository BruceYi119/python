a = [15,6,2,3,5,8,9,1,23]
# 추가
# a.append('seven')
# print(a)
# 뒤로 추가
# a.insert(3, '*')
# print(a)
# a[3] = '!!'
# print(a)
# 삭제
# del a[3:6]
# print(a)
# 객체 삭제
# del a

# for문
# for i in a:
#     print(a)
#     print('*')
# print(a)

a = []
# for i in range(0, 100):
#     print(i)
#     print('*')
# print(a)

# 형변환
# b = '3'
# print(int(b), type(int(b)))
#
# print(list(range(1, 15, 2)))
# print(tuple(range(1, 15, 2)))
# print(set(range(1, 15, 2)))

# a = ['one','two','three','four','five']

# for i in range(5):
#     print(i, a[i])

# a에 길이만큼
# for i in range(len(a)):
#     print(a[i])

# 0~5까지 2씩증감
# for i in range(0, 5, 2):
#     print(i)

# 구분값 변경 기본\n
# for i in range(1, 101):
#     print(i, end='/')

# 컴프리핸션
# a = [i for i in range(0, 101)]
# print(a)
# a = [7 for i in range(100)]
# print(len(a), a)

# 출력물 갯수만큼 출력
# print('*' * 7)
d = ['good' for i in range(5)]
print(d)
c = [i for i in range(0, 21, 2)]
print(c)
e = ['good' + str(i) for i in range(0, 21, 2)]
print(e)