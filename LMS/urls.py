
from django.urls import path
from .views import UserView, AddBook, AuthorViewSet, CategoryViewSet, GroupView

urlpatterns = [
    # path('', home, name="home"),
    # path('categories/',categories, name="categories"),
    path('category/',CategoryViewSet.as_view({'get':'list','post':'create'})),
    path('category/<int:pk>/',CategoryViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('author/',AuthorViewSet.as_view({'get':'list','post':'create'}),name="author"),
    path('author/<int:pk>/',AuthorViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name="author-edit"),
    path('add-book/',AddBook.as_view({'get':'list','post':'create'}),name="add-book"),
    path('add-book/<int:pk>/',AddBook.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('register/',UserView.as_view({'post':'register'}),name='register'),
    path('login/',UserView.as_view({'post':'login'}),name='login'),
    path('role/',GroupView.as_view({'get':'list'}),name='role')
]
