from django.conf.urls import url, include
from . import views
from django.urls import path
#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('customer', views.CustomerView)

urlpatterns = [
    #url(r'^$', include(router.urls), name="homepage"),
    #path('', include(router.urls)),
    #path('create/', views.add_items, name='add-items'),
    path('', views.view_items, name='view_items'),
    path('update/<int:pk>/', views.update_items, name='update-items'),
    path('cust/<int:pk>/delete/', views.delete_items, name='delete-items'),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^signup/$', views.signup_view, name="signup"),
]