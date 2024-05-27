from django.contrib import admin
from django.urls import path, include
from .views import HomeClass, LoginClass,InstructorDetailView, ArticlePost, ArticleDetailView, ForumView, ForumDetailViewIns, ArticleViewIns, ArticleViewAdmin, AboutUsAdmin, AboutUsIns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', LoginClass.as_view(), name='login'),
    path('home/', HomeClass.as_view(), name='home'),    
    path('instructor/<str:instructor_id>/', InstructorDetailView.as_view(), name='instructor'),
    path('articlepost/', ArticlePost.as_view(), name='articlepost'),
    path('article/<str:instructor_id>/', ArticleDetailView.as_view(), name='article'),
    path('forumad/', ForumView.as_view(), name='forumad'),
    path('forumins/<str:instructor_id>/', ForumDetailViewIns.as_view(), name='forumins'),
    path('forumad/<str:article_id>/', ArticleViewAdmin.as_view(), name='articlead'),
    
    path('article/<str:instructor_id>/<str:article_id>/', ArticleViewIns.as_view(), name='articleins'),
    path('forumins/<str:instructor_id>/<str:article_id>/', ArticleViewIns.as_view(), name='articleins'),
    path('aboutusins/<str:instructor_id>/<str:article_id>/', ArticleViewIns.as_view(), name='articleins'),
    
    path('aboutus/', AboutUsAdmin.as_view(), name='aboutusadmin'),
    path('aboutusins/<str:instructor_id>/', AboutUsIns.as_view(), name='aboutusins'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        