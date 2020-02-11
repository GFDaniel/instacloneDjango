from django.shortcuts import render
from .forms import PostForm
from .models import Post
from .models import User
from django.views.generic import (ListView, CreateView, TemplateView,)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_auth.views import LogoutView

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'insta/home.html'


class TestAuthView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        return Response("Hello {0}!".format(request.user))


class LogoutViewEx(LogoutView):
    authentication_classes = (authentication.TokenAuthentication,)


class PostListView(ListView):
	template_name = "insta/post_list.html"
	queryset = Post.objects.all()
	context_object_name = 'posts'

class PostUpdateProfileView(CreateView):
	template_name = "insta/post_create.html"
	form_class = PostForm
	queryset = Post.objects.all()
	success_url = '/'

	def form_invalid(self, form):
		print(form.cleaned_data)
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostCreateView(CreateView):
	template_name = "insta/post_create.html"
	form_class = PostForm
	queryset = Post.objects.all()
	success_url = '/'

	def form_invalid(self, form):
		print(form.cleaned_data)
		form.instance.author = self.request.user
		return super().form_valid(form)