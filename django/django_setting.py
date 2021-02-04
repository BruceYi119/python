# django 설치
# pip install django

# 프로젝트 생성
# django-admin startproject 프로젝트명
# django-admin startproject config

# 앱생성
# cd config
# python manage.py startapp 앱이름
# python manage.py startapp board

# 장고에서의 MTV(자바의 MCV)
# MTV (Model Template View) 자바의(MVC)
# template생성
# board/templates 폴더 생성

# 셋팅에 앱 추가
# config/settings.py INSTALLED_APPS

# models.py 작성
# config/manage.py 테이블 생성코드 작성
# python manage.py makemigrations
# migrations/0001_initial.py 생성됨

# 테이블 생성
# python manage.py migrate

# 테이블 생성 확인
# C:\sqlite>sqlite3.exe D:\pythonAna\config\db.sqlite3

# 테이블 수정 코드작성
# python manage.py makemigrations
# 특정 앱의 테이블 수정 코드작성
# python manage.py makemigrations member

# 테이블 생성
# python manage.py migrate
# 특정 앱의 테이블 생성
# python manage.py migrate member

# 서버 실행
# python manage.py runserver

# 관리자 생성
# python manage.py createsuperuser

# 관리자 페이지 접속
# localhost/admin

# 템플릿 파일 작성
# /templates/member/index.html
# views.py

# 관리자에 앱등록
# admin.py