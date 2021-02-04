from django.shortcuts import render
from .models import Member
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    return render(request, 'member/index.html')

def insert(request):
    if request.method == 'GET':
        return render(request, 'member/insert.html')
    else:
        username = request.POST['username']
        pw = request.POST['pw']
        pw2 = request.POST['pw']
        email = request.POST['email']
        hp = request.POST['hp']
        regdate = request.POST['regdate']
        msg = {}

        if not (username and pw and pw2 and hp):
            msg['err'] = '필수입력에 값을 채우세요'

        m = Member(
            username = username,
            pw = make_password(pw),
            email = email,
            hp = hp,
            regdate = regdate
        )
        m.save()

        return render(request, 'member/insert.html')

# def index(request):
#     qlist=Question.objects.all()
#     return render(request,'polls/index.html',{'qlist':qlist})
#     # return render(request,'polls/index.html')  #render(요청,반환할 페이지 [,딕션어리])
# def detail(request,qid):
#     # q=Question.objects.get(id=qid)  #select * from question where id=qid
#     q=get_object_or_404(Question,id=qid)
#     return render(request,'polls/detail.html',{'q':q})
# def vote(request,qid):
#     return render(request,'polls/result.html')
# def dbtest(request):   #http://127.0.0.1:8000/polls/dbtest/
#     # 1)삽입,수정 save()
#     # q=Question(question_text='좋아하는 운동은', pub_date='2021-01-07')
#     # q.save()
#     # q=Question(id=1, question_text='싫어하는 색은?', pub_date='2021-01-07')
#     # q.save()
#     # return render(request,'polls/dbtest.html')
#     # 2)조회
#     # qlist=Question.objects.all()  #모든 데이터
#     # qlist=Question.objects.get(id=3)  #조건에 맞는 데이터
#     # print(qlist)
#     # return render(request,'polls/dbtest.html')
#     # return render(request,'polls/dbtest.html',{'aa':'bb'})
#     # qlist=Question.objects.all()  #모든 데이터
#     # return render(request,'polls/dbtest.html',{'qlist':qlist})
#     # 3)삭제 delete()
#     q=Question.objects.get(id=1)   #해당 데이터를 가져온후
#     q.delete()
#     return render(request,'polls/dbtest.html')



