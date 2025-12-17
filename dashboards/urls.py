from django.urls import path
from . import views


urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    #Categories
    path('categories/',views.categories,name='categories'),
    path('categories/add',views.add_category,name='add_category'),
    path('categories/edit/<int:pk>',views.edit_category,name='edit_category'),
    path('categories/delete/<int:pk>',views.delete_category,name='delete_category'),

    #Posts/Blogs
    path('blogs/',views.blogs,name='blogs'),
    path('blogs/add',views.add_blog,name='add_blog'),
    path('blogs/edit/<int:pk>',views.edit_blog,name='edit_blog'),
    path('blogs/delete/<int:pk>',views.delete_blog,name='delete_blog'),
]
