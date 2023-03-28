from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index/', views.index, name='index'),
    path('review/',views.review,name='review'),
    path('contact/',views.contact,name='contact'),
    path('add', views.addTodo, name='add'),
    path('addReview', views.addReview, name='addReview'),
    path('addContact', views.addContact, name='addContact'),
    
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
]