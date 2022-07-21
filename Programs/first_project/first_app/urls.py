from django.urls import path
from . import views
#url patterns specific to this application

urlpatterns =[
    path('',views.index,name="index"),
    path('about_me',views.about_me,name="about_me"),
    path('<age>',views.age_page,name='age')
]