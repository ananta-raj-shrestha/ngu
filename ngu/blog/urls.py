from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name="blog-index"),
   #d for integer in capturing id and + for two digits w for words with hyfun(-)
     path('blog/<int:id>/',views.post_detail,name="view"),
     path('blog/<int:id>/update/',views.post_edit,name="post_edit"),
    path('post-upload/',views.post_upload,name="post_upload"),
    path('<int:id>/post-delete/',views.post_delete,name="post_delete"),
    path('success/',views.success,name="success")
]
