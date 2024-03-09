
from django.urls import path
from .views import home, UserView, categories, AddBook

urlpatterns = [
    path('home/', home, name="home"),
    path('add-book/',AddBook,name="add-book"),
    path('register/',UserView.as_view({'post':'register'}),name='register'),
    path('login/',UserView.as_view({'post':'login'}),name='login'),
    path('categories/',categories, name="categories"),
]
