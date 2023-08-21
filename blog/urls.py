from django.urls import path
from .views import *

urlpatterns=[
	path('',HomePageView,name='home'),
	path('blog',BlogPageView,name='blog'),
	path('contact',ContactPage,name='contact'),
	path('create_post',PostCreate,name='create'),
	path('post/<int:ID>',PostDetail,name='detail'),
	path('post/<int:ID>/delete',PostDelete,name='delete'),
	path('post/<int:ID>/edit',PostEdit,name='edit'),
]
