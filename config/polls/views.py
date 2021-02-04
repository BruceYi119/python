from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    return render(request, 'member/index.html')

def dbtest(request):
    # insert/update id가있으면 update
    # Question(id=5,question='어느 붕어빵이 맛있나요?!!', pub_date='2021-01-07 12:30:00').save()
    # 조회
    # list = Question.objects.get(id=3)
    # 전체조회
    list = Question.objects.all()
    print(list)
    return render(request, 'member/dbtest.html', { 'list': list, 'key': 'value' })