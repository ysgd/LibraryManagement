
from django.urls import path
from .views import home, UserView, categories, AddBook, AuthorViewSet, CategoryViewSet

urlpatterns = [
    path('', home, name="home"),
    path('categories/',categories, name="categories"),
    path('category/',CategoryViewSet.as_view({'get':'list','post':'create'})),
    path('category/<int:pk>',CategoryViewSet.as_view({'get':'retrieve','put':'update','destroy':'delete'})),
    path('author/',AuthorViewSet.as_view({'get':'list','post':'create'}),name="author"),
    path('author/<int:pk>',AuthorViewSet.as_view({'get':'retrieve','put':'update','destroy':'delete'}),name="author-edit"),
    path('add-book/',AddBook.as_view({'get':'list','post':'create'}),name="add-book"),
    path('add-book/<int:pk>',AddBook.as_view({'get':'retrieve','put':'update','destroy':'delete'})),
    path('register/',UserView.as_view({'post':'register'}),name='register'),
    path('login/',UserView.as_view({'post':'login'}),name='login'),
]
