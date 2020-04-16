

from .views import *
from django.urls import path



urlpatterns = [
    path('', MainView.as_view(), name= 'homepage'),
    path('login', LoginFormView.as_view(), name= 'login'),
    path('register', RegisterUserView.as_view(), name= 'register'),
    path('logout', LogoutView.as_view(), name= 'logout'),
    path('import', Post.as_view(), name= 'json_create_urlnew'),
    path('detail', Searching, name = 'GetDataFromJson'),
    path('detail/<AttributeName>/<id>/', Searching_detail, name = 'Searching_detail_url'),
    path('playing', Playing, name= 'playing'),
]