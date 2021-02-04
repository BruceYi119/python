from django.urls import path, include
from . import views
app_name = 'books'
urlpatterns = [
    path('book/', views.BookList.as_view(),name='booklist'),                               # 127.0.0.1:8000/books/book
    path('publisher/', views.PublisherList.as_view(), name='publisherlist'),               # 127.0.0.1:8000/books/publisher
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisherdetail'),
    path('publisher/insert/', views.PublisherCreate.as_view(), name='publisherinsert'),
    # 127.0.0.1:8000/books/publisher/insert
    path('publisher/update/<int:pk>/', views.PublisherUpdate.as_view(), name='publisherupdate'),
    # 127.0.0.1:8000/books/publisher/update/2
    path('publisher/delete/<int:pk>/', views.PublisherDelete.as_view(), name='publisherdelete'),
    # 127.0.0.1:8000/books/publisher/delete/2
    path('', views.BooksIndexView.as_view(), name='index'),    # 127.0.0.1:8000/books/
]





# from django.urls import path,include
# from . import views
# app_name='books'
# urlpatterns = [
#     path('book/', views.BookList.as_view(),name='booklist'),
#     path('publisher/', views.PublisherList.as_view(),name='publisherlist'),
#     path('publisher/<int:pk>', views.PublisherDetail.as_view(),name='publisherdetail'),
#     path('publisher/insert/',views.PublisherCreate.as_view(),name='publisherinsert'),
#     path('publisher/update/<int:pk>/',views.PublisherUpdate.as_view(),name='publisherupdate'),
#     path('publisher/delete/<int:pk>/',views.PublisherDelete.as_view(),name='publisherdelete'),
#     path('',views.BooksIndexView.as_view(),name='index'),
# ]

# as_view()메소드-진입메소드,
# url.py에서 클래스형뷰의 as_view()메소드를 호출