from django.contrib import admin
from django.urls import path
from aws.views import MatterList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aws/', MatterList.as_view(template_name="matter_list.html"), name="awsapp"),
]
