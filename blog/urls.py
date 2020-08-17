from django.urls import path
from . import views

urlpatterns=[
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name='post_delete'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/',views.add_comments_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/delete/',views.comment_delete,name='comment_delete'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),
]
