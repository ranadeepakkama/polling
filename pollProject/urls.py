"""
URL configuration for pollProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/',views.logoutRequest,name = 'logout'),
    path('',views.register,name = 'register'),
    path('login/',views.loginPage,name = 'login'),
    path('home/',views.homePage,name = 'home'),
    path('poll/',views.pollPage,name = 'poll'),
    path('createPoll/',views.createPoll,name = 'create'),
    path('delete/<int:id>',views.deletePoll,name = 'delete'),
    path('vote/<int:id>',views.votePage,name='vote'),
    path('search/',views.search,name = 'search'),
    path('result/<int:id>',views.result,name = 'result'),
    path('user/',views.user,name = 'user'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
