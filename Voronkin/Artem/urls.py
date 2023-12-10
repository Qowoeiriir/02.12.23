from django.urls import path
from Artem import views

urlpatterns = [
  path('',views.index,kwargs={"name":"Воронкин Артём Александрович","age":"16","interests":"программирование"}),
  path('about',views.abaut,kwargs={"where":"Москва","academic":"хорошист","like":"люблю"}),
  path('contacts',views.contacts,kwargs={"telephone":"+7 903 113 90 06"}),
]