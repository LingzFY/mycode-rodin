from django.conf.urls import url
from rodin import views

urlpatterns = [
    url('api/rodin_apiv1/news$', views.news_list),
    url('api/rodin_apiv1/news/(?P<pk>[0-9]+)$', views.news_detail),
    url('api/rodin_apiv1/news/published$', views.news_list_published)
]