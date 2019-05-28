from django.urls import path
from User import views

urlpatterns = [
    path('log/', views.user_detail, name='user.username.print'),
    path('following/list', views.follow_list, name='user.username.following.list'),
    path('follow/<str:__username>', views.follow, name='user.username.follow.username'),
    path('publish', views.publish, name='user.username.publish'),
    path('articles', views.article_list, name='user.username.articles'),
    path('article/<int:post_id>', views.view_article, name='user.username.view_article.post_id'),
    path('feeds', views.feed_pull, name='user.username.feed_pull'),
]