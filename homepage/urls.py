from django.urls import path, include
from . import views
urlpatterns = [
    # path('', include('social_django.urls', namespace='social')),
    path('', views.index, name='frontend.index'),
    path('contact/', views.contact, name="frontend.contact"),
    path('login/', views.login, name="frontend.login"),
    path('signup/', views.signup, name="frontend.signup"),
    path('admin/', views.admin, name="frontend.admin"),
    path('forum/', views.forum, name="frontend.forum"),
    path('blog/', include('homepage.blog.urls')),
    path('login/post', views.login_post, name='frontend.login.post'),
    path('logout/', views.logout_post, name='frontend.logout'),
    path('profile/', views.profile, name='frontend.profile'),
    path('update/', views.update, name='frontend.update'),
    path('edit_profile/', views.edit_profile, name='frontend.edit_profile'),
    # path('signup/', views.signup, name='frontend.signup'),
    # path('login/', views.login, name='frontend.login'),
    # path('login/post', views.login_post, name='frontend.login.post'),
    # path('logout/', views.logout_post, name='frontend.logout'),

    # path('account/', include('frontend.account.urls')),
    # path('webplayer/', include('frontend.webplayer.urls')),
]
