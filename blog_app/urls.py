from django.urls import path
from . import views
urlpatterns= [
    
    path('',views.post_list,name="post-list"),
    path('post-detail/<int:pk>/',views.post_detail,name="post-detail"),
    path('draft-list/',views.post_draft,name="post-draft"),
    path("draft-detail/<int:pk>/",views.draft_detail,name="draft-detail"),
    path("post-create/",views.post_create,name="post-create"),
    path("post-update/<int:pk>/",views.post_update,name="post-update"),
]