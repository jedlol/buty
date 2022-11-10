from django.urls import path
from . import views
from django.urls import include

urlpatterns = [

]

urlpatterns += [
    path('ogclick/', include('ogclick.urls')),
]

urlpatterns = [
    path('', views.index, name='index'),
]