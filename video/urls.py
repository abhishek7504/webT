from django.urls import path,include
from video import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('create/',views.Create),
    path('details/<int:id>/', views.DetailView, name='detail'),
    path('form/',views.userform,name='form'),
    path('accounts/', include('allauth.urls')),
    path('user_upload/',views.showvideo,name ='showvideo' )

]
