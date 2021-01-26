from django.urls import path
from django.conf.urls import url
from .import views
from .views import PostListView,PortfolioView
urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('blog/',PostListView.as_view(),name='blog'),
    path('contactview/',views.contactview,name='contactview'),
    path('portfolio/',PortfolioView.as_view(),name='portfolio'),
    url(r'^(?P<pk>\d+)/$', views.blogpost, name='blogpost'),
]
