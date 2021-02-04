# from django.shortcuts import render
# from .models import Question
# from django.shortcuts import get_object_or_404
# def index(request):
#     qlist=Question.objects.all()
#     return render(request,'polls/index.html',{'qlist':qlist})
#     # return render(request,'polls/index.html')  #render(요청,반환할 페이지 [,딕션어리])
# def detail(request,qid):
#     # q=Question.objects.get(id=qid)  #select * from question where id=qid
#     q=get_object_or_404(Question,id=qid)
#     c=q.choice_set.all()
#     print(c,len(c),'*****************')
#     msg={}
#     msg['q']=q
#     if len(c)<1:
#         msg['err']='선택할 항목이 없습니다.'
#     return render(request,'polls/detail.html',msg)
# def vote(request,qid):
#     q=Question.objects.get(id=qid)
#     # q=get_object_or_404(Question,pk=qid)
#     cid=request.POST['choice']
#     # Question과 Choice는 1:N관계, 외래키로 연결된 경우 모델소문자_set속성이 제공됨
#     # q.choice_set.all()
#     c=q.choice_set.get(id=cid)
#     c.votes=c.votes+1
#     c.save()
#     return render(request,'polls/result.html',{'q':q})
# # 과제
# # 1)tips데이터를 이용하여 요일을 행인덱스,성별을 열인덱스로 하여 식사금액의 합을 출력하세요
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
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
#     <link rel="stylesheet" href="/static/spring.css" />
# </head>
# <body>
# <h1>detail.html</h1>
# <hr>
# <h3>{{q.question_text}}-{{q.pub_date}}</h3>
# <!--Question과 Choice는 1:N관계, 외래키로 연결된 경우 모델소문자_set속성이 제공됨 즉)q.choice_set.all()
# 템플릿 문법상 ()생략-->
# {% if err %}
#     <h3>{{err}}</h3>
# {%else %}
#     <form method="post" action="{%url 'polls:vote1' q.id%}">
#         {%csrf_token%}
#         {%for  c in q.choice_set.all   %}
#             <input type="radio" name="choice" value="{{c.id}}"> {{c.choice_text}}<br>
#         {%endfor%}
#         <input type="submit" value="투표하기">
#     </form>
# {%endif%}
# </body></html>
#
#
#



# from django.shortcuts import render
# from django.views.generic import ListView,DetailView
# from django.views.generic.edit import CreateView,UpdateView,DeleteView
# from django.views.generic.base import TemplateView
# from .models import Book,Publisher,Author
# class BookList(ListView):
#     model = Book
# class PublisherCreate(CreateView):
#     model=Publisher
#     fields = ['name','addr'] #입력받을 컬럼지정
#     template_name= 'books/publisherinsert.html'
# class PublisherList(ListView):
#     model = Publisher
# class PublisherDetail(DetailView):
#     model = Publisher
# class BooksIndexView(TemplateView):
#     template_name = 'books/index.html'
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['mlist']=['book','publisher','author']
#         return context



# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
# <h1>books/index.html</h1>
# <hr>
# <ul>
#     {%for m in mlist%}
#     <li><a href="/books/{{m}}">{{m}}</a></li>
#     {% endfor %}
# </ul>
# </body>
# </html>


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
# <h1>books/publisherinsert.html</h1>
# <hr>
# <form id="frm1" method="post">
# {%csrf_token%}
# <table border="1">
# {{form.as_table}}  <!--form.as_p , form.as_ul-->
# <tr>
#     <td colspan="2"><input type="submit" value="등록"></td>
# </tr>
# </table>
# </form>
# </body>
# </html>


############################################
# CreateView
# InsertView
# UpdateView
# DeleteView
# 템플릿
# {{변수}}
# {%csrf-token%}
# {%comment 주석내용%} {%endcomment%}
# 기준 레이아웃 작성, 상속받아 사용
