from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path('',inicio,name="AppBlogInicio"),
    path('about/',about,name="AppBlogAbout"),
    path('post/list', PostList.as_view(), name='Post/List'),
    path('post/<int:pk>/', PostDetalle.as_view(), name='Post/Detail'),
]


