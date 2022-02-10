"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from website.views import welcome, login, allmovies, allcourses, alltvshows, movie, tvshow, course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('<int:id>', welcome, name='home'),
    path('<int:id_client>movies', allmovies, name="movies"),
    path('<int:id_client>tvshows', alltvshows, name="tvshows"),
    path('<int:id_client>courses', allcourses, name="courses"),
    path('<int:id_client>movies<int:id>', movie, name="movie-part"),
    path('<int:id_client>tvshows<int:id>', tvshow, name="serie-part"),
    path('<int:id_client>courses<int:id>', course, name="course-part"),
]
