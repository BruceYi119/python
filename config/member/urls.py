from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('insert/', views.insert)
]

# urlpatterns = [
#     # path(url패턴, url이 매칭되면 호출되는 뷰함수 [, 이름]),
#     path('',views.index),    #127.0.0.1:8000/polls
#     path('<int:qid>/',views.detail),  #127.0.0.1:8000/polls/2
#     path('vote/<int:qid>/', views.vote),  # http://127.0.0.1:8000/polls/vote/3
#     path('dbtest/', views.dbtest),  # 127.0.0.1:8000/polls/dbtest
#     # path('insert/', views.insert),   #127.0.0.1:8000/polls/insert
# ]