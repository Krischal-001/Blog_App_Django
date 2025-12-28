from django.urls import path
from . import views
urlpatterns= [
    
    path('',views.PostListView.as_view(),name="post-list"),
    path('post-detail/<int:pk>/',views.PostDetailView.as_view(),name="post-detail"),
    path('draft-list/',views.DraftListView.as_view(),name="post-draft"),
    path("draft-detail/<int:pk>/",views.DraftDetailView.as_view(),name="draft-detail"),
    path("post-create/",views.PostCreateView.as_view(),name="post-create"),
    path("post-update/<int:pk>/",views.PostUpdateView.as_view(),name="post-update"),
    path("post-delete/<int:pk>/",views.post_delete,name="post-delete"),
    path("draft-publish/<int:pk>/",views.draft_publish,name="draft-publish")
]