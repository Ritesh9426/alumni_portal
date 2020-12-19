from django.urls import path 

from . import views

urlpatterns = [
  # /
  path('', views.home, name='home'),
  # TEMPORARY
  path('signin', views.sign_in, name='signin'),
  path('signout', views.sign_out, name='signout'),
  path('callback', views.callback, name='callback'),
  #path('test',views.test),
  #path('test-signup/<name>/<email>',views.test_signup),
  path('test-signin/<name>',views.test_signin),
  path('follow/<name>',views.follow),
  path('unfollow/<name>',views.unfollow),
  path('followers',views.followers),
  path('following',views.following),
]