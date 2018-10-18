

from django.urls import path
from . import Views


urlpatterns = [
    path('' , Views.Hellow),
    path('count/',Views.count,name="count")

]
