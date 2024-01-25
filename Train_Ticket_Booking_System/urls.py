
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about_us/', views.about_us, name='about_us'),
    path('category/<slug:category_slug>/', views.home, name='category_wise_post'),
    path('account/', include("passenger.urls")),
    path('train/', include("train.urls")),

]
