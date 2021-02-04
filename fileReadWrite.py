import os
import glob
import cchardet

# 파일내용 읽기 함수
def readFile(dir, text, encoding):
    with open(dir, 'r', encoding=encoding) as f:
        text.append(f.read().replace('\n', ''))

# 파일 쓰기 함수
def writeFile(text):
    with open(os.path.join('data', 'result.txt'), 'w', encoding='utf-8') as f:
        f.write(','.join(text).replace(',', ''))

# data폴더에 모든 파일을 읽어서 result.txt로 데이터를 합치는 함수
def main():
    text = []
    for dir in glob.glob(os.path.join('data', '*')):
        encoding = None;

        with open(dir, 'rb') as f:
            encoding = cchardet.detect(f.read())['encoding']

            readFile(dir, text, encoding)

    writeFile(text)

# fileReadWrite파일에서만 main()을 실행 다른파일에서 import fileReadWrite시 실행이 안되고 펑션들만 import됨
if __name__ == '__main__':
    main()