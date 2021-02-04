# people = { "name": "둘리", "age": "1억살" }
# print(people)
# print(type(people))
# print(people["age"])
# people[1004] = "yes"
# print(people)
# for i in people.items():
#     print(i)
# for i, v in people.items():
#     print(i, v)
# a = [1,2,5,7,9,4,13,5,76,3,1,2,3,1,23,1,1,1]
# print(a)
# print(set(a))
# b = list(set(a))
# print(b)
a = '''
1 bob 12
3834 kate 333
1423 ko 2035
1235 Alice 535
15481 Kerry 312123
'''

print(a)
import re   #정규식 사용
#re.findall(r'정규식',문자열)
r = re.findall('[*A-Z]?[a-z]+',a)
print(r)

# 정규표현식
# ?	0 or 1
# *	0번 이상
# +	1번 이상
# {최소값,최대값}
# . 글자1개, 줄바꿈 제외
# [^ ]	부정
# ^ 시작
# {3}
# {3,}
# {,3}
# | 선택
# [a-zA-Z0-9%^&*()]
# \s 공백
a='''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''
import re   #정규식 사용
# re.findall(r'정규식',문자열)
r1=re.findall(r'[0-9]',a)
print(r1)
r1=re.findall(r'[0-9]+',a)
print(r1)
r1=re.findall(r'[A-Za-z]+',a)
print(r1)
# T로 시작하지 않는 이름 찾기
r1=re.findall(r'[A-SU-Z][a-z]+',a)
print(r1)