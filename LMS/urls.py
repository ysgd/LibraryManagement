
from django.urls import path
from .views import home, UserView, categories, AddBook, AuthorViewSet

urlpatterns = [
    path('home/', home, name="home"),
    path('add-book/',AddBook.as_view({'post':'create'}),name="add-book"),
    path('author',AuthorViewSet.as_view({'post':'create'}),name="author"),
    path('register/',UserView.as_view({'post':'register'}),name='register'),
    path('login/',UserView.as_view({'post':'login'}),name='login'),
    path('categories/',categories, name="categories"),
]
