"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from app.views import DarsViewSet, KursViewSet, IzohViewSet,UserRegisterView,LikeBosishQismi,LikeTextCreateView,EmailJonatishView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()

router.register(r'dars', DarsViewSet)
router.register(r'kurs', KursViewSet)
router.register(r'izoh', IzohViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/send/message/email/',EmailJonatishView.as_view()),
 

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('darsga/<int:pk>/like/', LikeBosishQismi.as_view()),
    path('darsga/like/create/', LikeTextCreateView.as_view()),


    path('register/', UserRegisterView.as_view(), name= 'register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

