
from django.urls import path
from .views import home, UserView

urlpatterns = [
    
    path('', home),
    path('register/',UserView.as_view({'post':'register'}),name='register'),
    path('login/',UserView.as_view({'post':'login'}),name='login')
]
