# a="  blue  red  green "
# print(len(a))  #길이
# print("["+a+"]")
# print("["+a.lstrip()+"]")   #왼쪽 공백삭제
# print("["+a.rstrip()+"]")
# print("["+a.strip()+"]")
# print("["+a+"]")
# # a.replace('찾는 문자열','바꿀문자열') 문자열치환
# print(a.replace(' ',''))
# print(a.upper(),a.lower())
# a="one-two-three four-five six"
# print(type(a))
# print(a.split('-'))
# print(a.split(' '))
# print(type(a.split(' ')))  #<class 'list'>
# b=a.split(' ')
# print(b)
# # '기호'.join(리스트)
# print('!'.join(b))
# print(type('!'.join(b)))
#-------------
# line=input()
# print(line,type(line))
# print(line.split())
# collection
# [] 리스트:인덱스는 0부터 시작
# () 튜플
# {} 딕션어리, set
# <> not used
# a=[1,56,'blue',['one','two','three'],1111,True]
# print(a,len(a))
# print(a[0])
# print(a[0:3])
# print(a[3:])
# print(a[5])
# print(a[3:5])
# print('-'*30)
# print(a[3])
# print(a[3][1])
# -----
b=['토마토','감','포도']
print(b[1])
b[2]='캠벨'
print(b)
b.append('샤인머스킷')   #추가
print(b)
print(sorted(b)) #정렬
a=[3,78,100,55,4]
print('합계',sum(a))
print('평균',sum(a)/len(a))
print(dir(a))

# print(reversed(b))
# print(list(reversed(b)))
# 컴프리핸션






print('\n\n\n\n\n\n\n\n\n\n\n')
