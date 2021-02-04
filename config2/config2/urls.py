from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from  . import settings
from  . import views
urlpatterns = [
    path('admin/', admin.site.urls),         #127.0.0.1:8000/admin
    path('books/',include('books.urls')),    #127.0.0.1:8000/books
    path('',views.HomeView.as_view(),name='home')
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




