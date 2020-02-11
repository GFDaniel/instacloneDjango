from django.urls import path, include
from .views import (PostListView, PostCreateView,)
# from .views import HomeTemplateView, TestAuthView, LogoutViewEx
# from rest_auth.views import LoginView

app_name = 'insta'

urlpatterns = [
	path('post_list',PostListView.as_view(), name='post_list'),
	# path('', HomeTemplateView.as_view(), name='home', ),
	path('new/',PostCreateView.as_view(), name='post_create'),
    # path('test_auth/', TestAuthView.as_view(), name='test_auth', ),
    # path('rest-auth/logout/', LogoutViewEx.as_view(), name='rest_logout', ),
    # path('rest-auth/login/', LoginView.as_view(), name='rest_login', ),
]
