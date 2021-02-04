# def f1(n):
#     return n * 10

# print(f1(10))

# 람다함수 : 메모리절약, 가독성 향상, 코드 간결
# b = lambda n:n * 10
#
# print(b(22))
#
# def f2(x, y, f):
#     print(x * y * f(x + y))
#
# f2(10, 100, lambda x:x + 1)

# a = [1,2,3,5,6]
# result = [];
#
# def f(list):
#     result = [(v * 3) for v in list]
#     print(result)
#
# f(a)

# map(함수명,반복가능객체) : 매개변수로 함수와 반복가능한객체 입력
# def f4(x):
#     return x * 3
#
# print(f4(7))
# print(f4([1,2,3]))
# print(map(f4, [1,2,3]))
# print(list(map(f4, [1,2,3])))
# print(list(map(lambda n, z:n * 3 + z, [1,2,3], [3,2,1])))

# os모듈:디렉토리, 파일등의 os자원 제어
import os
# print(os.getcwd())
# print(os.listdir('d:\\'))
# print(os.listdir('C:\Program Files'))
# print(os.path.join('..', 'test1'))
# print(os.listdir(os.path.join('img')))

# glob모듈
import glob
# print(glob.glob('*.py'))
# print(os.path.join('..', 'img', '*.jpg'))
#
# print(os.path.dirname(os.path.join('d:','study','pj1','data','tt.txt')))
# print(os.path.basename(os.path.join('d:','study','pj1','data','tt.txt')))

# with open(os.path.join('data','tt.txt'), 'r', encoding='utf-8') as f:
#     while True:
#         l = f.readline()
#         if not l:
#             break
#         print(l, end = '')

# for dir in glob.glob(os.path.join('data', '*')):
#     with open(dir, 'r', encoding='utf-8') as f:
#         print(f.readlines())

import cchardet
# for dir in glob.glob(os.path.join('data', '*')):
#     encoding = None;
#
#     with open(dir, 'rb') as f:
#         encoding = cchardet.detect(f.read())['encoding']
#         with open (dir, 'r', encoding=encoding) as ff:
#             print(ff.readlines())

# with open(os.path.join('data','data3.csv'), 'r', encoding='utf-8') as f:
#     for v in f:
#         print(v.replace('\n',''), end='')

# text = [];
# for dir in glob.glob(os.path.join('data', '*')):
#     encoding = None;
#
#     with open(dir, 'rb') as f:
#         encoding = cchardet.detect(f.read())['encoding']
#         with open (dir, 'r', encoding=encoding) as ff:
#             text.append(ff.read().replace('\n',''))
#
# with open(os.path.join('data','result.txt'), 'w', encoding='utf-8') as f:
#     f.write(','.join(text).replace(',',''))

def readFile(dir, text, encoding):
    with open(dir, 'r', encoding=encoding) as f:
        text.append(f.read().replace('\n', ''))

def writeFile(text):
    with open(os.path.join('data', 'result.txt'), 'w', encoding='utf-8') as f:
        f.write(','.join(text).replace(',', ''))

def main():
    text = []
    for dir in glob.glob(os.path.join('data', '*')):
        encoding = None;

        with open(dir, 'rb') as f:
            encoding = cchardet.detect(f.read())['encoding']

            readFile(dir, text, encoding)

    writeFile(text)

if __name__ == '__main__':
    main()