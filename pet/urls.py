from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name="register"),
    path('email',views.email,name="email"),
    path('confirm/<str:num>',views.confirm,name="confirm"),
]
